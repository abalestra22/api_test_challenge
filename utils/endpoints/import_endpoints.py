""" Module to store import endpoints. """
class ImportEndpoints:
    BASE_URL = "https://api.test.worldsys.ar"

    @classmethod
    def get_import_endpoint(cls):
        """ Helper function to return import endpoint. """
        return f"{cls.BASE_URL}/import/"
