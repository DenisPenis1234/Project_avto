import configuration

import data

import requests

# Определение функции post_new_user для отправки POST-запроса на создание нового пользователя
def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH, json=body, headers=data.headers_user)


token = post_new_user(data.user_body).json()

#делаем токен, который можно добавить будет в заголовок headers_kit
token["authToken"] = "Bearer " + token["authToken"]

#меняем значение параметра Authorization заголовка headers_kit
def put_new_token_to_kit(authToken):
    data.headers_kit["Authorization"] = authToken

put_new_token_to_kit(token["authToken"])

def put_new_name_to_kit_body(name):
    data.kit_body["name"] = name


# Определение функции post_new_client_kit для отправки POST-запроса на создание нового набора для пользователя
def post_new_client_kit(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_KIT_PATH, json=body, headers=data.headers_kit)

