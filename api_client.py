import requests

from data import Urls


class ApiClient:
    def __init__(self):
        self.base_url = Urls.BASE_URL.rstrip('/')
        self.headers = {"Content-Type": "application/json"}
        self.token = None

    def login(self, email, password):
        response = requests.post(f"{self.base_url}/api/auth/login", json={"email":email, "password": password}, headers=self.headers)
        response.raise_for_status()
        self.token = response.json()["accessToken"]
        self.headers["Authorization"] = self.token
        return self

    def get_user_orders(self):
        response = requests.get(f"{self.base_url}/api/orders", headers=self.headers)
        response.raise_for_status()
        return response.json()

    def get_valid_ingredients(self):
        response = requests.get(f"{self.base_url}/api/ingredients", headers=self.headers)
        response.raise_for_status()
        data = response.json()
        return [ingredient["_id"] for ingredient in data["data"]]

    def create_order(self, ingredient_ids):
        response = requests.post(f"{self.base_url}/api/orders", json={"ingredients": ingredient_ids}, headers=self.headers)
        response.raise_for_status()
        return response.json()