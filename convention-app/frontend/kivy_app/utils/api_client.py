import requests

class APIClient:
    BASE_URL = "http://api.yourservice.com/"

    @staticmethod
    def get_events():
        response = requests.get(f"{APIClient.BASE_URL}/events")
        return response.json()