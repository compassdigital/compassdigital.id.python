
from hashids import Hashids
import binascii

_hashid = Hashids(salt = "Compass Digital")

_short_to_long = {
    "L": "location",
    "M": "menu",
    "I": "item",
    "C": "shoppingcart",
    "O": "order"
}

_long_to_short = {
    "location": "L",
    "menu": "M",
    "item": "I",
    "shoppingcart": "C",
    "order": "O"
}

def _to_hashid(s):
    hex = binascii.hexlify(s.encode("utf-8")).decode("utf-8")
    return _hashid.encode_hex(hex)

def _from_hashid(s):
    hex = _hashid.decode_hex(s)
    return binascii.unhexlify(hex.encode("utf-8")).decode("utf-8")

def encode(service, provider, type, id = None):
    parts = [service, provider, type]
    if id is not None:
        parts.append(id)
    for i, value in enumerate(parts):
        value = str(value).lower()
        if "." in value:
            raise ValueError("value cannot contain period: {}".format(value))
        if value in _long_to_short:
            value = _long_to_short[value]
        parts[i] = value
    return _to_hashid(".".join(parts))

def decode(id):
    parts = _from_hashid(id).split(".")
    if len(parts) < 3 or len(parts) > 4:
        raise ValueError("invalid id: {}".format(id))
    for i, value in enumerate(parts):
        if value.upper() in _short_to_long:
            parts[i] = _short_to_long[value.upper()]
    decoded = {
        "service": parts[0],
        "provider": parts[1],
        "type": parts[2],
    }
    if len(parts) == 4:
        decoded["id"] = parts[3]
    return decoded
