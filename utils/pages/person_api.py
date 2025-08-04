import requests
from utils.endpoints import import_endpoints
from utils.logger import logger

class PersonAPI:
    def __init__(self, token):
        self.headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {token}"
        }

    def post_person(self, person_id):
        """
        Helper function to send POST request.
        """
        payload = [{"personId": person_id}]
        endpoints = import_endpoints.ImportEndpoints()
        endpoint = endpoints.get_import_endpoint()
        logger.info(f"Sending headers: {self.headers}")
        logger.info(f"Sending body: {payload}")
        logger.info(f"Sending request with url: {endpoint} and personId as: {person_id}")
        try:
            response = requests.post(
                url=endpoint,
                json=payload,
                headers=self.headers)
            return response
        except requests.exceptions.RequestException as e:
            logger.info(f"Request failed: {e}")
            return None
