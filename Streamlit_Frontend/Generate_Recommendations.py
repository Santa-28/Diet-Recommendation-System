# from urllib import response
# import requests
# import json

# backend_url = 'http://127.0.0.1:8000/predict/'
# class Generator:
#     def __init__(self,nutrition_input:list,ingredients:list=[],params:dict={'n_neighbors':5,'return_distance':False}):
#         self.nutrition_input=nutrition_input
#         self.ingredients=ingredients
#         self.params=params

#     def set_request(self,nutrition_input:list,ingredients:list,params:dict):
#         self.nutrition_input=nutrition_input
#         self.ingredients=ingredients
#         self.params=params

#     def generate(self,):
#         request={
#             'nutrition_input':self.nutrition_input,
#             'ingredients':self.ingredients,
#             'params':self.params
#         }
#         response = requests.post(url='http://127.0.0.1:8000/predict/', data=json.dumps(request))
#     if response.status_code == 200:
#         recommendations = response.json()['output']
#         print("Recommendations:", recommendations)
#     else:
#         print("Failed to fetch recommendations:", response.status_code, response.text)

# import requests
# import json

# backend_url = 'http://127.0.0.1:8000/predict/'

# class Generator:
#     def __init__(self, nutrition_input: list, ingredients: list = [], params: dict = {'n_neighbors': 5, 'return_distance': False}):
#         self.nutrition_input = nutrition_input
#         self.ingredients = ingredients
#         self.params = params

#     def set_request(self, nutrition_input: list, ingredients: list, params: dict):
#         self.nutrition_input = nutrition_input
#         self.ingredients = ingredients
#         self.params = params

#     def generate(self):
#         request_data = {
#             'nutrition_input': self.nutrition_input,
#             'ingredients': self.ingredients,
#             'params': self.params
#         }
#         headers = {'Content-Type': 'application/json'}
#         response = requests.post(url=backend_url, data=json.dumps(request_data), headers=headers)

#         if response.status_code == 200:
#             recommendations = response.json().get('output')
#             print("Recommendations:", recommendations)
#         else:
#             print("Failed to fetch recommendations:", response.status_code, response.text)
import requests
import json

backend_url = 'http://127.0.0.1:8000/predict/'

class Generator:
    def __init__(self, nutrition_input: list, ingredients: list = [], params: dict = {'n_neighbors': 5, 'return_distance': False}):
        self.nutrition_input = nutrition_input
        self.ingredients = ingredients
        self.params = params

    def set_request(self, nutrition_input: list, ingredients: list, params: dict):
        self.nutrition_input = nutrition_input
        self.ingredients = ingredients
        self.params = params

    def generate(self):
        request_data = {
            'nutrition_input': self.nutrition_input,
            'ingredients': self.ingredients,
            'params': self.params
        }
        headers = {'Content-Type': 'application/json'}
        try:
            response = requests.post(url=backend_url, data=json.dumps(request_data), headers=headers)
            response.raise_for_status()  # Raises HTTPError for bad responses
        except requests.RequestException as e:
            print(f"Request failed: {e}")
            return None  # or handle the error as needed

        if response.status_code == 200:
            return response.json()  # Return JSON data if successful
        else:
            print("Failed to fetch recommendations:", response.status_code, response.text)
            return None

