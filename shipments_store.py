"""Shipment ledger — defaults, JSON file persistence, GPS routes."""

import json
import os
from copy import deepcopy
from datetime import datetime

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, 'data')
SHIPMENTS_FILE = os.path.join(DATA_DIR, 'shipments.json')

FREIGHT_DEFAULTS = {
    'airway_bill': '112-576488934',
    'flight_no': 'SS00324',
    'total_freight': '120kg',
    'total_value': '£20,375',
    'handling_fee': 'Unpaid',
    'delivery_type': 'Economy',
    'delivery_address': '170 Deville Hill Road, 71342 Jena, LA',
    'origin': 'Heathrow Airport',
    'destination': "Charlotte Douglas International Airport",
}

LOCATION_PRESETS = {
    'Hounslow Secure Hub (HQ)': {'lat': 51.4700, 'lng': -0.4543, 'city': 'Hounslow, UK'},
    'Heathrow Airport': {'lat': 51.4700, 'lng': -0.4543, 'city': 'Hounslow, UK'},
    'Dover Transit Terminal': {'lat': 51.1279, 'lng': 1.3134, 'city': 'Dover, UK'},
    'Rotterdam Secure Hub': {'lat': 51.9244, 'lng': 4.4777, 'city': 'Rotterdam, Netherlands'},
    'Frankfurt Custody Centre': {'lat': 50.1109, 'lng': 8.6821, 'city': 'Frankfurt, Germany'},
    'Paris Operations Node': {'lat': 48.8566, 'lng': 2.3522, 'city': 'Paris, France'},
    'Zurich Vault Facility': {'lat': 47.3769, 'lng': 8.5417, 'city': 'Zurich, Switzerland'},
    'Dubai Secure Hub': {'lat': 25.2532, 'lng': 55.3657, 'city': 'Dubai, UAE'},
    'Singapore Clearing Port': {'lat': 1.3521, 'lng': 103.8198, 'city': 'Singapore'},
    'Charlotte Douglas International Airport': {'lat': 35.2140, 'lng': -80.9431, 'city': 'Charlotte, NC, USA'},
}

DEFAULT_SHIPMENTS = {
    'SSS-0001': {
        'tracking_number': 'SSS-0001',
        'asset_description': 'Gold Bullion - 12kg',
        'shipment_status': 'In Transit',
        'customs_status': 'Cleared',
        'duties_taxes': '$0',
        'insurance_status': 'Insured',
        'security_level': 'High',
        'receiver_status': 'Pending',
        'last_location': 'Heathrow Airport',
        'customs_agent': 'Agent V',
        'agent_id': 'AG-101',
        'notice_text': 'Handle in secure room. GPS custody active.',
        'shipment_date': '2026-06-01',
        'expected_date': '2026-06-10',
        'latitude': 51.4700,
        'longitude': -0.4543,
        'city': 'Hounslow, UK',
        'route_index': 0,
        'route': [
            {'lat': 51.4700, 'lng': -0.4543, 'city': 'Hounslow, UK', 'last_location': 'Heathrow Airport'},
            {'lat': 35.2140, 'lng': -80.9431, 'city': 'Charlotte, NC, USA', 'last_location': 'Charlotte Douglas International Airport'},
        ],
        **FREIGHT_DEFAULTS,
    },
    'SSS-0002': {
        'tracking_number': 'SSS-0002',
        'asset_description': 'Diamond Shipment - Box A',
        'shipment_status': 'Delivered',
        'customs_status': 'Cleared',
        'duties_taxes': '$0',
        'insurance_status': 'Claimed',
        'security_level': 'Top',
        'receiver_status': 'Signed',
        'last_location': 'Zurich Vault Facility',
        'customs_agent': 'Agent Z',
        'agent_id': 'AG-202',
        'notice_text': '',
        'shipment_date': '2026-05-20',
        'expected_date': '2026-05-22',
        'latitude': 47.3769,
        'longitude': 8.5417,
        'city': 'Zurich, Switzerland',
        'route_index': 0,
        'route': [],
        **FREIGHT_DEFAULTS,
    },
    'SS3409536472': {
        'tracking_number': 'SS3409536472',
        'asset_description': 'Secure Vault Transfer - Sovereign Cargo',
        'shipment_status': 'In Transit',
        'customs_status': 'Awaiting Clearance',
        'duties_taxes': '$18,900',
        'insurance_status': 'Insured',
        'security_level': 'Critical',
        'receiver_status': 'Pending',
        'last_location': 'Hounslow Secure Hub (HQ)',
        'customs_agent': 'Agent K',
        'agent_id': 'AG-421',
        'notice_text': 'Priority cargo under enhanced customs watch.',
        'shipment_date': '2026-06-02',
        'expected_date': '2026-06-12',
        'latitude': 51.4700,
        'longitude': -0.4543,
        'city': 'Hounslow, UK',
        'route_index': 0,
        'route': [
            {'lat': 51.4700, 'lng': -0.4543, 'city': 'Hounslow, UK', 'last_location': 'Hounslow Secure Hub (HQ)'},
            {'lat': 51.1279, 'lng': 1.3134, 'city': 'Dover, UK', 'last_location': 'Dover Transit Terminal'},
            {'lat': 25.2532, 'lng': 55.3657, 'city': 'Dubai, UAE', 'last_location': 'Dubai Secure Hub'},
            {'lat': 1.3521, 'lng': 103.8198, 'city': 'Singapore', 'last_location': 'Singapore Clearing Port'},
        ],
        **FREIGHT_DEFAULTS,
    },
}


def normalize_code(code):
    return (code or '').strip().upper()


def _ensure_defaults(shipments):
    merged = deepcopy(DEFAULT_SHIPMENTS)
    for key, record in shipments.items():
        if key in merged:
            combined = {**merged[key], **record}
        else:
            combined = deepcopy(record)
            combined.setdefault('tracking_number', key)
        combined = _apply_gps_defaults(combined)
        merged[key] = combined
    return merged


def _load_from_disk():
    if not os.path.exists(SHIPMENTS_FILE):
        return deepcopy(DEFAULT_SHIPMENTS)
    try:
        with open(SHIPMENTS_FILE, encoding='utf-8') as handle:
            data = json.load(handle)
        if isinstance(data, dict):
            return _ensure_defaults(data)
    except (json.JSONDecodeError, OSError):
        pass
    return deepcopy(DEFAULT_SHIPMENTS)


def _save_to_disk():
    os.makedirs(DATA_DIR, exist_ok=True)
    with open(SHIPMENTS_FILE, 'w', encoding='utf-8') as handle:
        json.dump(_shipments, handle, indent=2)


def _stamp(record):
    record = deepcopy(record)
    record['last_updated'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    return record


def _apply_gps_defaults(record):
    if record.get('latitude') is None or record.get('longitude') is None:
        record['latitude'] = 51.4700
        record['longitude'] = -0.4543
        record.setdefault('city', 'Hounslow, UK')
        record.setdefault('last_location', 'Hounslow Secure Hub (HQ)')
    record.setdefault('route', [])
    record.setdefault('route_index', 0)
    for key, value in FREIGHT_DEFAULTS.items():
        record.setdefault(key, value)
    return record


def _sync_route_from_gps(record):
    """When an officer moves a shipment, keep route + journey in sync with GPS."""
    lat = record.get('latitude')
    lng = record.get('longitude')
    if lat is None or lng is None:
        return record

    route = list(record.get('route') or [])
    label = record.get('last_location') or record.get('city') or 'Current position'
    city = record.get('city') or ''

    match_idx = None
    for i, wp in enumerate(route):
        if abs(float(wp['lat']) - float(lat)) < 0.02 and abs(float(wp['lng']) - float(lng)) < 0.02:
            match_idx = i
            route[i] = {
                **wp,
                'last_location': label,
                'city': city or wp.get('city', ''),
            }
            break

    if match_idx is not None:
        record['route_index'] = match_idx
    elif route:
        route.append({
            'lat': float(lat),
            'lng': float(lng),
            'city': city,
            'last_location': label,
        })
        record['route_index'] = len(route) - 1
    else:
        route = [{
            'lat': float(lat),
            'lng': float(lng),
            'city': city,
            'last_location': label,
        }]
        record['route_index'] = 0

    record['route'] = route
    return record


def _enrich_shipment(record):
    if not record:
        return None

    record = deepcopy(record)
    route = record.get('route') or []
    idx = min(record.get('route_index', 0), max(len(route) - 1, 0))

    journey = []
    for i, wp in enumerate(route):
        if i < idx:
            status = 'completed'
        elif i == idx:
            status = 'current'
        else:
            status = 'upcoming'
        journey.append({
            'label': wp.get('last_location') or wp.get('city') or f'Stop {i + 1}',
            'city': wp.get('city', ''),
            'status': status,
            'lat': wp.get('lat'),
            'lng': wp.get('lng'),
        })

    record['journey'] = journey
    record['route_index'] = idx

    for key, value in FREIGHT_DEFAULTS.items():
        record.setdefault(key, value)

    if idx + 1 < len(route):
        nxt = route[idx + 1]
        record['next_destination'] = nxt.get('last_location') or nxt.get('city') or '—'
    elif route:
        record['next_destination'] = route[-1].get('last_location') or route[-1].get('city') or 'Final destination'
    else:
        record['next_destination'] = record.get('last_location') or '—'

    return record


_shipments = _load_from_disk()
if not os.path.exists(SHIPMENTS_FILE):
    _save_to_disk()


def get_shipment(code):
    global _shipments
    if os.path.exists(SHIPMENTS_FILE):
        try:
            mtime = os.path.getmtime(SHIPMENTS_FILE)
            cached = getattr(get_shipment, '_cache_mtime', None)
            if cached != mtime:
                _shipments = _load_from_disk()
                get_shipment._cache_mtime = mtime
        except OSError:
            pass
    record = _shipments.get(normalize_code(code))
    return _enrich_shipment(record)


def upsert_shipment(code, payload):
    key = normalize_code(code)
    existing = _shipments.get(key, {'tracking_number': key, 'route': [], 'route_index': 0})
    existing = _apply_gps_defaults(deepcopy(existing))
    merged = {**existing, **(payload or {}), 'tracking_number': key}
    for field, default in FREIGHT_DEFAULTS.items():
        if not merged.get(field):
            merged[field] = existing.get(field) or default
    merged = _apply_gps_defaults(merged)
    merged = _sync_route_from_gps(merged)
    merged = _stamp(merged)
    _shipments[key] = merged
    _save_to_disk()
    return _enrich_shipment(merged)


def advance_route(code):
    key = normalize_code(code)
    record = _shipments.get(key)
    if not record or not record.get('route'):
        return None

    route = record['route']
    next_index = (record.get('route_index', 0) + 1) % len(route)
    waypoint = route[next_index]
    record['route_index'] = next_index
    record['latitude'] = waypoint['lat']
    record['longitude'] = waypoint['lng']
    record['city'] = waypoint.get('city', record.get('city', ''))
    record['last_location'] = waypoint.get('last_location', record.get('last_location', ''))
    record = _stamp(record)
    _shipments[key] = record
    _save_to_disk()
    return _enrich_shipment(record)


def reset_store():
    global _shipments
    _shipments = deepcopy(DEFAULT_SHIPMENTS)
    _save_to_disk()


def all_shipments():
    return deepcopy(_shipments)


def valid_codes():
    return sorted(_shipments.keys())
