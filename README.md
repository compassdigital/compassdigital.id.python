# Compass Digital ID - Python

Creates ids for use in the Compass Digital platform. Decodes ids to reveal the meta-data within.

# Requirements

* Python 2.7 & 3
* hashids >= 1.3.1

# Installation

This module has not been uploaded to PyPI or properly packaged.
To use it, copy `cdlid.py` into your project and install hashids.

**Dependencies:**
``` sh
pip install -r requirements.txt
```

# Usage

``` python
import cdlid

cdlid.encode({
    "service": "location",
    "provider": "cdl",
    "type": "group",
    "id": "7c732f634cbf443092ae6f289d80121f",
})
# => "eW0gy25y3BFaYvgPlYgmfPmZloM3d2fE032BvlZDH2g5r6qkYau18BQgWGOGFAQMvl03NkHX80"

cdlid.decode("eW0gy25y3BFaYvgPlYgmfPmZloM3d2fE032BvlZDH2g5r6qkYau18BQgWGOGFAQMvl03NkHX80")
# => {
#     "service": "location",
#     "provider": "cdl",
#     "type": "group",
#     "id": "7c732f634cbf443092ae6f289d80121f",
# }
```