"""
import pytest
import requests

@pytest.mark.positive
def test_create_booking_positive():
    print("create booking TC")
    URL = "https://restful-booker.herokuapp.com/booking"
    headers = {"Content-Type" : "application/json"}
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
    print(type(URL))
    print(type(headers))
    print(type(json_payload))
    assert response.status_code == 200
    data = response.josn()
    booking_id = data ["bookingid"]
    print(booking_id)
    assert data["bookingid"] is not None
    assert data["booking"]["firstname"] == "jim", "incorrect firstname"

@ pytest.mark.negative
def test_create_booking_negative():
    print("create booking TC")
    URL = "https://restful-booker.herokuapp.com/booking"
    headers = {"Content-Type" : "application/json"}
    json_payload = {
    }
    response = requests.post(url=URL, headers=headers, json=json_payload)
    print(type(URL))
    print(type(headers))
    print(type(json_payload))
    assert response.status_code == 500
"""

