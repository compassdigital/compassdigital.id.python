import unittest
import cdlid

expected_ids = [
    ["eW0gy25y3BFaYvgPlYgmfPmZloM3d2fE032BvlZDH2g5r6qkYau18BQgWGOGFAQMvl03NkHX80", {
        "service": "location",
        "provider": "cdl",
        "type": "group",
        "id": "7c732f634cbf443092ae6f289d80121f",
    }],
    ["11J3gKPg8BCR3mr5OO92S6EBL4ddEAT17G44eoLPSw0N21gy4OHjQXjDG6LXIrL1MY8B5PHPX9omNMrqFJO", {
        "service": "location",
        "provider": "cdl",
        "type": "multigroup",
        "id": "ec65915647e84bcd83f536ad29c694d2"
    }],
    ["MX85pE82L4sLvrXkw3A2TyaYyemGXQi1JkME8J1GiLBRjBzE8vH1Dzevm1WefD2eRvlXOeFKadpMoEvRtX49Z", {
        "service": "user",
        "provider": "cdl",
        "type": "user",
        "id": "cdl/f6d6816279e64b85bb2670cf04d5dfce"
    }],
    ["p61vEp4g34Tqdjkm54p0f9Lg", {
        "service": "menu",
        "provider": "bamco",
        "type": "item",
        "id": "1234",
    }]
]

class TestEncodingDecodingID(unittest.TestCase):
    def test_encode_decode(self):
        for encoded, decoded in expected_ids:
            print(encoded)
            self.assertDictEqual(decoded, cdlid.decode(encoded))
            self.assertEqual(encoded, cdlid.encode(decoded))

if __name__ == "__main__":
    unittest.main()