"""Module to store assertions for API testing"""

class ResponseAssertions:

    @staticmethod
    def assert_status_code(response, expected_status):
        """
        Validate the expected status
        code against the actual status code.
        """
        actual = response.status_code
        assert actual == expected_status, (
            f"Expected status code {expected_status}, but got {actual}"
        )

    @staticmethod
    def assert_field_equals(response, field, expected_value):
        """
        Validate the expected fields in response
        against the actual fields in response.
        """
        try:
            actual_value = response.json().get(field)
        except Exception as e:
            raise AssertionError(f"Failed to parse JSON response: {e}")

        assert actual_value == expected_value, (
            f"Expected '{field}' to be '{expected_value}', but got '{actual_value}'"
        )
