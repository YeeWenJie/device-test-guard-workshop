import unittest

from device_test_guard.disposition import decide_disposition
from device_test_guard.models import DeviceTestRecord


def record(device_id: str, passed: bool = True, retest_count: int = 0) -> DeviceTestRecord:
    return DeviceTestRecord(
        device_id,
        25.0,
        1.0,
        {"logic": passed},
        retest_count,
    )


class Module5DuplicateIdentifierTests(unittest.TestCase):
    def test_duplicate_identifiers_hold_passing_batch(self):
        records = [record("DEVICE-A"), record("DEVICE-A")]
        self.assertEqual(decide_disposition(records, 90.0)[0], "HOLD")

    def test_duplicate_identifiers_hold_below_target_batch(self):
        records = [
            record("DEVICE-B"),
            record("DEVICE-B", passed=False, retest_count=0),
        ]
        self.assertEqual(decide_disposition(records, 90.0)[0], "HOLD")


if __name__ == "__main__":
    unittest.main()
