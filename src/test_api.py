from urllib import request
import pytest
import requests
import json

# This website is a publicly available REST API for practice/testing
# Scroll down on the home page, and in the section for POST / LOGIN-SUCESSFUL, 
# the login and token details as used here below are found
def main_url():
    return "https://reqres.in"

def test_valid_login(main_url = main_url()):
    url = main_url + "/api/login/"
    # data = {'email': 'abc@xyz.com', 'password': 'qwerty'}
    data = {'email': 'eve.holt@reqres.in', 'password': 'cityslicka'}
    response = requests.post(url, data=data)
    token = json.loads(response.text)
    assert response.status_code == 200
    assert token['token'] == "QpwL5tke4Pnpja7X4"