"""Module to store Import Tests - Happy Path scenarios."""
import pytest
from utils.decorators import regression
from utils.pages import person_api
from utils.logger import logger
from utils.assertions import ResponseAssertions
from utils.db import DBClient


class TestImportEndpoints:

    @pytest.fixture(scope="class", autouse=True)
    def setup_client(self, request, api_token):
        """Setup API client once per test class."""
        request.cls.api_client = person_api.PersonAPI(api_token)
        self.person_id = 111

    @regression
    def test_post_person_200(self, db_credentials):
        """
        Validate that sending POST request with valid
        data returns 200 response.
        """
        logger.info(self.test_post_person_200.__doc__)

        response = self.api_client.post_person(self.person_id)

        ResponseAssertions.assert_status_code(response, 200)
        ResponseAssertions.assert_field_equals(response, "status", "success")

    def test_post_person_200_database(self, db_credentials):
        """ Validate personId against database. """
        db = DBClient(**db_credentials)
        result = db.fetch_person_by_id(self.person_id)
        db.close()

        assert len(result) > 0, f" PersonId not found {self.person_id}"
        logger.info(f" Successful personId validation: {self.person_id}")
