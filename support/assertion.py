class Assertion:
    @staticmethod
    def assert_equal(actual, expected):
        assert actual == expected, f"Expected: {expected}, but actually we got {actual}"
