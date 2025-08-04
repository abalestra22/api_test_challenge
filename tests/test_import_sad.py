"""Module to store Import Tests - Sad Path scenarios."""
import pytest
import uuid
from utils.decorators import regression
from utils.pages import person_api
from utils.logger import logger
from utils.assertions import ResponseAssertions

class TestImportEndpointsNegative:

    @pytest.fixture(scope="class", autouse=True)
    def setup_client(self, request):
        """Setup API client once per test class."""
        token = "xxx"
        request.cls.api_client = person_api.PersonAPI(token)

    @regression
    @pytest.mark.parametrize("person_id", [
        "nonexistent",
        str(uuid.uuid4()),
        -10,
        True,
        None
    ])
    def test_post_person_invalid_id(self, person_id):
        """
        Tests that sending POST request with
        invalid personId returns 4xx error.
        """
        logger.info(self.test_post_person_invalid_id.__doc__)
        logger.info(f" Sending invalid personId: {person_id}")

        response = self.api_client.post_person(person_id)

        assert response is not None, "No answer returned from server."
        ResponseAssertions.assert_status_code(response, 400)
        ResponseAssertions.assert_field_equals(response, "status", "error")
