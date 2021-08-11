
from hashids import Hashids
import binascii

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

_hashid = Hashids(salt = "Compass Digital")

def _to_hashid(s):
    hex = binascii.hexlify(s.encode("utf-8")).decode("utf-8")
    return _hashid.encode_hex(hex)

def _from_hashid(s):
    hex = _hashid.decode_hex(s)
    return binascii.unhexlify(hex.encode("utf-8")).decode("utf-8")

def encode(id):
    """
    Return the encoded id string.
    The id parameter must be a dictionary with the following keys: service, provider, type, id.
    """
    parts = []
    for key in ["service", "provider", "type"]:
        if key not in id:
            raise ValueError("missing property: {}".format(key))
        parts.append(str(id[key]))
    if "id" in id:
        parts.append(str(id["id"]))
    for i, value in enumerate(parts):
        value = str(value).lower()
        if "." in value:
            raise ValueError("value cannot contain period: {}".format(value))
        if value in _long_to_short:
            value = _long_to_short[value]
        parts[i] = value
    return _to_hashid(".".join(parts))

def decode(id):
    """
    Return the decoded id dictionary.
    The id parameter must be a encoded id string.
    """
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