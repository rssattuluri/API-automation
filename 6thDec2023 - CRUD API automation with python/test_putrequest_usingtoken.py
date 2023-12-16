from typing import Any

import pytest
import requests

# Create token
@pytest.mark.createtoken
def create_token():
    url = "https://restful-booker.herokuapp.com/auth"
    headers = {"Content-Type": "application/json"}
    json_payload = {
        "username": "admin",
        "password": "password123"
    }
    response = requests.post(url=url, headers=headers, json=json_payload)
    data = response.json()
    token = data["token"]
    print(token)
    return token


def create_booking():
    print("create booking TC")
    URL = "https://restful-booker.herokuapp.com/booking"
    headers = {"Content-Type": "application/json"}
    json_payload = {
        "firstname": "Jim",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }
    response = requests.post(url=URL, headers=headers, json=json_payload)
    assert response.status_code == 200
    data = response.json()
    booking_id = data["bookingid"]
    return booking_id

@pytest.mark.put
def test_put_request():
    URL = "https://restful-booker.herokuapp.com/booking/"
    booking_id = create_booking()
    PUT_URL = URL + str(booking_id)
    headers = {"Content-Type" : "application/json" , "Cookie": ("token=" + create_token())}
    print(headers)
    json_payload = {
        "firstname": "Jim",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }
    response = requests.put(url=PUT_URL, headers=headers, json=json_payload)
    # Assertions
    assert response.status_code == 200
    data = response.json()
    assert data["firstname"] == "Jim", "Incorrect firstname"

@pytest.mark.delete
def test_delete():
    URL = "https://restful-booker.herokuapp.com/booking/"
    booking_id = create_booking()
    PUT_URL = URL + str(booking_id)
    headers = {"Content-Type": "application/json", "Cookie": ("token=" + create_token())}
    response = requests.delete(url=PUT_URL, headers=headers)
    # Assertions
    assert response.status_code == 201