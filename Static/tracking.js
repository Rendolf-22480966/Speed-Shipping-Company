/**
 * Live shipment tracking map — Leaflet + OpenStreetMap
 * Polls /api/shipments/<code> for officer updates; animates marker smoothly.
 */
(function (global) {
    'use strict';

    var POLL_MS = 2000;
    var ANIMATION_MS = 2800;
    var DEMO_INTERVAL_MS = 4500;

    function createShipmentIcon() {
        return L.divIcon({
            className: 'tracking-marker-wrap',
            html:
                '<div class="tracking-marker">' +
                '<div class="tracking-marker-pulse"></div>' +
                '<div class="tracking-marker-core">' +
                '<svg viewBox="0 0 24 24" aria-hidden="true">' +
                '<path d="M12 2C8.13 2 5 5.13 5 9c0 5.25 7 13 7 13s7-7.75 7-13c0-3.87-3.13-7-7-7zm0 9.5A2.5 2.5 0 1 1 12 6a2.5 2.5 0 0 1 0 5.5z" fill="currentColor"/>' +
                '</svg></div></div>',
            iconSize: [44, 44],
            iconAnchor: [22, 44],
            popupAnchor: [0, -42],
        });
    }

    function createWaypointIcon(status, index) {
        var cls = 'track-waypoint-icon track-waypoint-icon--' + status;
        return L.divIcon({
            className: cls,
            html: '<span>' + (index + 1) + '</span>',
            iconSize: [28, 28],
            iconAnchor: [14, 14],
        });
    }

    function LiveTrackingMap(containerId, options) {
        this.containerId = containerId;
        this.trackingCode = (options && options.trackingCode) || '';
        this.onUpdate = (options && options.onUpdate) || null;
        this.onLocationChange = (options && options.onLocationChange) || null;
        this.backgroundMode = !!(options && options.backgroundMode);
        this.map = null;
        this.marker = null;
        this.routeLine = null;
        this.waypointMarkers = [];
        this.pollTimer = null;
        this.demoTimer = null;
        this.lastCoords = null;
        this.lastSyncKey = null;
        this.lastRouteKey = null;
        this.animationFrame = null;
        this.shipmentData = null;
    }

    LiveTrackingMap.prototype.initBaseMap = function () {
        var el = document.getElementById(this.containerId);
        if (!el) return Promise.reject(new Error('Map container missing'));
        if (this.map) return Promise.resolve();

        this.map = L.map(this.containerId, {
            zoomControl: !this.backgroundMode,
            scrollWheelZoom: true,
            dragging: true,
            touchZoom: true,
            doubleClickZoom: true,
        }).setView([51.47, -0.45], 5);

        L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
            attribution: '&copy; OpenStreetMap',
            maxZoom: 18,
        }).addTo(this.map);

        this.marker = L.marker([51.47, -0.45], {
            icon: createShipmentIcon(),
            zIndexOffset: 1000,
        }).addTo(this.map);

        var self = this;
        return new Promise(function (resolve) {
            setTimeout(function () {
                if (self.map) self.map.invalidateSize();
                if (self.backgroundMode && !self._resizeBound) {
                    self._resizeBound = true;
                    window.addEventListener('resize', function () {
                        if (self.map) self.map.invalidateSize();
                    });
                }
                resolve();
            }, 150);
        });
    };

    LiveTrackingMap.prototype.init = function () {
        var self = this;
        return this.initBaseMap().then(function () {
            return self.fetchAndRender(true);
        });
    };

    LiveTrackingMap.prototype.normalizeCode = function (raw) {
        return (raw || '').trim().toUpperCase();
    };

    LiveTrackingMap.prototype.readLocalShipment = function (code) {
        try {
            var raw = localStorage.getItem('shipment_' + code);
            if (!raw) return null;
            var data = JSON.parse(raw);
            data.tracking_number = code;
            if (data.latitude == null) data.latitude = 51.47;
            if (data.longitude == null) data.longitude = -0.4543;
            return data;
        } catch (err) {
            return null;
        }
    };

    LiveTrackingMap.prototype.syncLocalToServer = function (code, data) {
        return fetch('/api/shipments/' + encodeURIComponent(code) + '/register', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(data),
        }).catch(function () {
            return null;
        });
    };

    LiveTrackingMap.prototype.fetchShipment = function () {
        var code = this.normalizeCode(this.trackingCode);
        this.trackingCode = code;
        if (!code) return Promise.reject(new Error('No tracking code'));

        var self = this;

        return fetch('/api/shipments/' + encodeURIComponent(code))
            .then(function (res) {
                if (res.ok) return res.json();
                var localData = self.readLocalShipment(code);
                if (!localData) throw new Error('Shipment not found');
                return self.syncLocalToServer(code, localData).then(function () {
                    return localData;
                });
            });
    };

    LiveTrackingMap.prototype.syncKey = function (data) {
        if (!data) return '';
        return [
            data.last_updated || '',
            data.latitude,
            data.longitude,
            data.last_location || '',
            data.shipment_status || '',
            data.airway_bill || '',
            data.flight_no || '',
            data.total_freight || '',
            data.total_value || '',
            data.handling_fee || '',
            data.delivery_type || '',
            data.delivery_address || '',
            data.origin || '',
            data.destination || '',
        ].join('|');
    };

    LiveTrackingMap.prototype.routeKey = function (data) {
        var journey = data.journey || data.route || [];
        return journey.map(function (j) {
            return (j.lat || '') + ',' + (j.lng || '') + ':' + (j.status || j.last_location || '');
        }).join('|');
    };

    LiveTrackingMap.prototype.fetchAndRender = function (initial) {
        var self = this;
        var prevKey = this.lastSyncKey;
        var prevRouteKey = this.lastRouteKey;

        return this.fetchShipment()
            .then(function (data) {
                var changed = !initial && prevKey && prevKey !== self.syncKey(data);
                var routeChanged = initial || prevRouteKey !== self.routeKey(data);
                self.shipmentData = data;
                self.renderRoute(data);
                self.renderDestinations(data, routeChanged);
                self.updateMarker(
                    data.latitude,
                    data.longitude,
                    initial ? 0 : ANIMATION_MS,
                    data
                );
                self.lastSyncKey = self.syncKey(data);
                self.lastRouteKey = self.routeKey(data);

                if (self.onUpdate) self.onUpdate(data, { initial: initial, changed: changed });
                if (changed && self.onLocationChange) self.onLocationChange(data);
                return data;
            })
            .catch(function (err) {
                console.error('[Tracking]', err.message);
                return null;
            });
    };

    LiveTrackingMap.prototype.clearWaypointMarkers = function () {
        var self = this;
        this.waypointMarkers.forEach(function (m) {
            if (self.map) self.map.removeLayer(m);
        });
        this.waypointMarkers = [];
    };

    LiveTrackingMap.prototype.renderRoute = function (data) {
        if (!this.map) return;

        if (this.routeLine) {
            this.map.removeLayer(this.routeLine);
            this.routeLine = null;
        }

        var points = [];
        if (data.journey && data.journey.length) {
            points = data.journey
                .filter(function (j) { return j.lat != null && j.lng != null; })
                .map(function (j) { return [j.lat, j.lng]; });
        } else if (data.route && data.route.length) {
            points = data.route.map(function (wp) { return [wp.lat, wp.lng]; });
        }

        if (points.length < 2) return;

        this.routeLine = L.polyline(points, {
            color: '#c5a028',
            weight: 2,
            opacity: 0.55,
            dashArray: '6 8',
        }).addTo(this.map);
    };

    LiveTrackingMap.prototype.renderDestinations = function (data, fitBounds) {
        if (!this.map) return;
        this.clearWaypointMarkers();

        var journey = data.journey || [];
        var self = this;
        var bounds = [];

        journey.forEach(function (stop, index) {
            if (stop.lat == null || stop.lng == null) return;
            bounds.push([stop.lat, stop.lng]);

            var marker = L.marker([stop.lat, stop.lng], {
                icon: createWaypointIcon(stop.status || 'upcoming', index),
                zIndexOffset: stop.status === 'current' ? 900 : 400,
            }).addTo(self.map);

            marker.bindPopup(
                '<strong>' + stop.label + '</strong><br>' +
                (stop.city || '') + '<br>' +
                '<span style="color:#c5a028;text-transform:uppercase;font-size:11px;">' +
                (stop.status || '') + '</span>'
            );

            self.waypointMarkers.push(marker);
        });

        if (data.latitude != null && data.longitude != null) {
            bounds.push([data.latitude, data.longitude]);
        }

        if (fitBounds && bounds.length > 1) {
            this.map.fitBounds(bounds, { padding: [50, 50], maxZoom: 8 });
        } else if (fitBounds && bounds.length === 1) {
            this.map.setView(bounds[0], 7);
        }
    };

    LiveTrackingMap.prototype.updateMarker = function (lat, lng, duration, data) {
        if (!this.marker || lat == null || lng == null) return;

        var target = { lat: lat, lng: lng };
        var start = this.lastCoords || target;

        if (duration <= 0 || !this.lastCoords) {
            this.marker.setLatLng([target.lat, target.lng]);
            this.updatePopup(data, target);
            this.lastCoords = target;
            return;
        }

        var self = this;
        var startTime = null;

        function easeInOut(t) {
            return t < 0.5 ? 2 * t * t : 1 - Math.pow(-2 * t + 2, 2) / 2;
        }

        function frame(timestamp) {
            if (!startTime) startTime = timestamp;
            var progress = Math.min((timestamp - startTime) / duration, 1);
            var eased = easeInOut(progress);
            var curLat = start.lat + (target.lat - start.lat) * eased;
            var curLng = start.lng + (target.lng - start.lng) * eased;
            self.marker.setLatLng([curLat, curLng]);
            self.map.panTo([curLat, curLng], { animate: false, noMoveStart: true });

            if (progress < 1) {
                self.animationFrame = requestAnimationFrame(frame);
            } else {
                self.lastCoords = target;
                self.updatePopup(data, target);
            }
        }

        if (this.animationFrame) cancelAnimationFrame(this.animationFrame);
        this.animationFrame = requestAnimationFrame(frame);
    };

    LiveTrackingMap.prototype.updatePopup = function (data, coords) {
        if (!this.marker || !data) return;
        var city = data.city || data.last_location || 'In transit';
        var status = data.shipment_status || 'In Transit';
        var next = data.next_destination ? '<br>Next: ' + data.next_destination : '';
        this.marker.bindPopup(
            '<strong>' + (data.tracking_number || '') + '</strong><br>' +
            city + '<br>' +
            '<span style="color:#c5a028">' + status + '</span>' + next
        );
    };

    LiveTrackingMap.prototype.startPolling = function () {
        var self = this;
        this.stopPolling();
        this.pollTimer = setInterval(function () {
            self.fetchAndRender(false);
        }, POLL_MS);
    };

    LiveTrackingMap.prototype.stopPolling = function () {
        if (this.pollTimer) {
            clearInterval(this.pollTimer);
            this.pollTimer = null;
        }
    };

    LiveTrackingMap.prototype.startDemoSimulation = function () {
        var self = this;
        this.stopDemoSimulation();
        this.demoTimer = setInterval(function () {
            fetch('/api/shipments/' + encodeURIComponent(self.trackingCode) + '/advance', {
                method: 'POST',
            })
                .then(function (res) {
                    if (!res.ok) return null;
                    return res.json();
                })
                .then(function (data) {
                    if (data) self.fetchAndRender(false);
                })
                .catch(function () {});
        }, DEMO_INTERVAL_MS);
    };

    LiveTrackingMap.prototype.stopDemoSimulation = function () {
        if (this.demoTimer) {
            clearInterval(this.demoTimer);
            this.demoTimer = null;
        }
    };

    LiveTrackingMap.prototype.destroy = function () {
        this.stopPolling();
        this.stopDemoSimulation();
        if (this.animationFrame) cancelAnimationFrame(this.animationFrame);
        this.clearWaypointMarkers();
        if (this.map) {
            this.map.remove();
            this.map = null;
        }
    };

    global.LiveTrackingMap = LiveTrackingMap;
})(window);
