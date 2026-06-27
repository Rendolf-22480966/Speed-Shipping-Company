"""Vault custody ledger — client safe-keeping records."""

import json
import os
from copy import deepcopy
from datetime import datetime

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, 'data')
VAULT_FILE = os.path.join(DATA_DIR, 'vault.json')

DEFAULT_VAULTS = {
    'CG201609SP': {
        'tracking_code': 'CG201609SP',
        'transaction_code': 'CGS/XXT/2016/00',
        'depositor_name': 'Mr David Durham',
        'depositor_title': 'Male · Primary Depositor',
        'next_of_kin': 'Mrs Debbie Durham',
        'next_of_kin_title': 'Female · Registered Next of Kin',
        'deposit_date': '16 January 2016',
        'item_deposited': '120kg Gold Bars',
        'item_weight': '120kg',
        'item_class': 'Allocated Bullion — Class I',
        'deposit_purpose': 'Safe Keeping',
        'monthly_charge': '£215.00',
        'agent_name': 'Michael William',
        'vault_number': 'SSSC-534-DE210',
        'agent_id': 'SSSC-U202',
        'membership_type': 'Gold',
        'insurance': 'Full Coverage',
        'account_status': 'Past Due · Rollover Protection Active',
        'account_status_class': 'past-due',
        'outstanding_clearance_fee': '£20,375.00',
        'valuation_reference': '$12.7 Million',
        'recent_payment_date': '16 January 2016',
        'recent_payment_source': 'Bank of America',
        'receipt_number': '367954091112',
        'custody_location': 'Speed-Shipping Secure Vault — Tier IV Bullion Wing',
        'ledger_reference': 'SSSC-VLT-2016-CG201609SP',
    },
}


def normalize_vault_code(code):
    return (code or '').strip().upper()


def _load_from_disk():
    if not os.path.exists(VAULT_FILE):
        return deepcopy(DEFAULT_VAULTS)
    try:
        with open(VAULT_FILE, encoding='utf-8') as handle:
            data = json.load(handle)
        if isinstance(data, dict):
            merged = deepcopy(DEFAULT_VAULTS)
            for key, record in data.items():
                norm = normalize_vault_code(key)
                merged[norm] = {**merged.get(norm, {}), **record, 'tracking_code': norm}
            return merged
    except (json.JSONDecodeError, OSError):
        pass
    return deepcopy(DEFAULT_VAULTS)


def _save_to_disk():
    os.makedirs(DATA_DIR, exist_ok=True)
    with open(VAULT_FILE, 'w', encoding='utf-8') as handle:
        json.dump(_vaults, handle, indent=2)


_vaults = _load_from_disk()
if not os.path.exists(VAULT_FILE):
    _save_to_disk()


def get_vault(code):
    global _vaults
    if os.path.exists(VAULT_FILE):
        try:
            mtime = os.path.getmtime(VAULT_FILE)
            cached = getattr(get_vault, '_cache_mtime', None)
            if cached != mtime:
                _vaults = _load_from_disk()
                get_vault._cache_mtime = mtime
        except OSError:
            pass
    record = _vaults.get(normalize_vault_code(code))
    if not record:
        return None
    record = deepcopy(record)
    record['last_verified'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    return record


def is_vault_code(code):
    return normalize_vault_code(code) in _vaults
