import os
from datetime import datetime
from functools import wraps

from flask import (
    Flask,
    render_template,
    request,
    redirect,
    url_for,
    session,
    flash,
    abort,
    jsonify,
)

from services_data import SERVICES, get_service
from shipments_store import (
    get_shipment,
    upsert_shipment,
    advance_route,
    reset_store,
    LOCATION_PRESETS,
    valid_codes,
    normalize_code,
)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

app = Flask(
    __name__,
    template_folder=os.path.join(BASE_DIR, 'Templates'),
    static_folder=os.path.join(BASE_DIR, 'Static'),
    static_url_path='/static',
)

# Secret key signs the session cookie. Override in production via env var.
app.secret_key = os.environ.get('RBH_SECRET_KEY', 'change-this-royal-bullion-secret-key')
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config['SESSION_COOKIE_HTTPONLY'] = True
app.config['SESSION_COOKIE_SAMESITE'] = 'Lax'
app.config['PERMANENT_SESSION_LIFETIME'] = 86400

SITE_PORT = int(os.environ.get('PORT', '5080'))
IS_LOCAL = os.environ.get('FLASK_LOCAL', '').lower() in ('1', 'true', 'yes')
ON_RENDER = os.environ.get('RENDER') == 'true' or bool(os.environ.get('RENDER_EXTERNAL_URL'))

if ON_RENDER or (not IS_LOCAL and os.environ.get('PORT')):
    app.config['SESSION_COOKIE_SECURE'] = True

# Demo credentials. In production, replace with a real user store / hashed passwords.
DEFAULT_TRACKING_CODE = 'SS3409536472'
ADMIN_USERNAME = os.environ.get('RBH_ADMIN_USER', 'Rendolf_001')
ADMIN_PASSWORD = os.environ.get('RBH_ADMIN_PASS', 'iwasmadeforthisshid$$')


def login_required(view):
    """Redirect to the login page if the admin is not authenticated."""

    @wraps(view)
    def wrapped(*args, **kwargs):
        if session.get('logged_in'):
            return view(*args, **kwargs)
        if request.path.startswith('/api/') or request.is_json:
            abort(401)
        return redirect(url_for('login', next=request.path))

    return wrapped


def _safe_next_url(candidate):
    if candidate and candidate.startswith('/') and not candidate.startswith('//'):
        return candidate
    return url_for('admin')


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if session.get('logged_in'):
        return redirect(url_for('admin'))

    error = None
    next_url = _safe_next_url(request.args.get('next'))

    if request.method == 'POST':
        username = request.form.get('username', '').strip()
        password = request.form.get('password', '')
        next_url = _safe_next_url(request.form.get('next') or request.args.get('next'))

        if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
            session.permanent = True
            session['logged_in'] = True
            session['user'] = username
            return redirect(next_url, code=303)

        error = 'Invalid credentials. Access denied.'

    return render_template('login.html', error=error, next_url=next_url)


@app.route('/officer')
@app.route('/presider')
def officer_entry():
    """Officer login entry — opens presider panel immediately when already signed in."""
    if session.get('logged_in'):
        return redirect(url_for('admin'))
    return redirect(url_for('login', next=url_for('admin')))


@app.route('/logout')
def logout():
    session.clear()
    flash('You have been securely signed out.')
    return redirect(url_for('login'))


@app.route('/admin')
@login_required
def admin():
    return render_template(
        'admin.html',
        user=session.get('user'),
        default_tracking_code=DEFAULT_TRACKING_CODE,
    )


@app.route('/services/<slug>')
def service_detail(slug):
    service = get_service(slug)
    if not service:
        abort(404)

    related = {
        key: val for key, val in SERVICES.items()
        if key != slug
    }
    # Show only 3 related services on page
    related_items = dict(list(related.items())[:3])

    return render_template(
        'service.html',
        service=service,
        slug=slug,
        related=related_items,
        year=datetime.now().year,
    )


@app.route('/track')
def track():
    from shipments_store import FREIGHT_DEFAULTS, _enrich_shipment

    code = request.args.get('code', '').strip().upper()
    shipment = get_shipment(code) if code else None
    if code and not shipment:
        shipment = _enrich_shipment({
            'tracking_number': code,
            'shipment_status': 'In Transit',
            'asset_description': 'Secure Vault Transfer - Sovereign Cargo',
            'last_location': 'Heathrow Airport',
            'latitude': 51.47,
            'longitude': -0.4543,
            'city': 'Hounslow, UK',
            **FREIGHT_DEFAULTS,
        })
    return render_template(
        'track.html',
        code=code,
        shipment=shipment,
        site_port=SITE_PORT,
        show_port_warning=IS_LOCAL,
    )


@app.route('/api/shipments/<code>', methods=['GET'])
def api_get_shipment(code):
    record = get_shipment(code)
    if not record:
        abort(404)
    return jsonify(record)


@app.route('/api/shipments/<code>', methods=['PUT', 'POST'])
@login_required
def api_update_shipment(code):
    payload = request.get_json(silent=True) or {}
    record = upsert_shipment(code, payload)
    return jsonify(record)


@app.route('/api/shipments/<code>/register', methods=['POST'])
def api_register_shipment(code):
    """Register or update a shipment (used by admin + legacy localStorage sync)."""
    payload = request.get_json(silent=True) or {}
    record = upsert_shipment(code, payload)
    return jsonify(record)


@app.route('/api/shipments/codes')
def api_shipment_codes():
    return jsonify({'codes': valid_codes()})


@app.route('/api/shipments/<code>/advance', methods=['POST'])
def api_advance_shipment(code):
    """Demo endpoint — advances to next route waypoint (simulates officer GPS update)."""
    record = advance_route(code)
    if not record:
        abort(404)
    return jsonify(record)


@app.route('/api/location-presets')
def api_location_presets():
    return jsonify(LOCATION_PRESETS)


if __name__ == '__main__':
    import threading
    import time
    import webbrowser

    def open_browser():
        time.sleep(1.5)
        webbrowser.open(f'http://127.0.0.1:{SITE_PORT}/track?code=SS3409536472')

    threading.Thread(target=open_browser, daemon=True).start()
    app.run(debug=False, host='127.0.0.1', port=SITE_PORT, use_reloader=False)
