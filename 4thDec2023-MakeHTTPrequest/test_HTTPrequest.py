"""
# GET request
import requests


def main():
    response_body = requests.get("https://restful-booker.herokuapp.com/booking/1465")
    print(response_body.text)
    print(response_body.status_code)
    print(response_body.json())
    print(response_body.cookies)
    if response_body.status_code == 200:
        print("TC#1 - GET request is successful")
    else:
        print("TC#1 - GET request is not successful")

if __name__ == "__main__":
    main()


# Instead of using main method
response_body = requests.get("https://restful-booker.herokuapp.com/booking/1465")
print(response_body.text)
print(response_body.headers)

# To verify - Assertion(To verify the expected result with the actual result)

# With Assertion
def main():
    id = "68"
    url = "https://restful-booker.herokuapp.com/booking/"
    full_url = url + id
    response_body = requests.get(full_url)
    assert response_body.status_code == 200
    # if it is 200 no output # if id is not present =!200 error is shown

    data = response_body.json()
    print(type(data))
# Verification of key
    assert 'firstname' in data, "Incorrect Firstname"
    assert 'lastname' in data, "Incorrect Lastname"

# Verification of data
    assert data["firstname"] == "Jane", "Incorrect first name"
    assert data["lastname"] == "Doe", "Incorrect last name"
    assert data["bookingdates"]["checkin"] == "2018-01-01", "Incorrect checkin"


if __name__ == "__main__":
    main()

# using Pytest
import pytest

def test_sample():
    4 == 4
"""

import requests


def test_get_request():
    id = "1003"
    url = "https://restful-booker.herokuapp.com/booking/"
    full_url = url + id
    response_body = requests.get(full_url)
    assert response_body.status_code == 200
    # if it is 200 no output # if id is not present =!200 error is shown

    data = response_body.json()
    print(type(data))
    # Verification of key
    assert 'firstname' in data, "Incorrect Firstname"
    assert 'lastname' in data, "Incorrect Lastname"

    # Verification of data
    assert data["firstname"] == "Jim", "Incorrect first name"
    assert data["lastname"] == "B rown", "Incorrect last name"
    assert data["bookingdates"]["checkin"] == "2018-01-01", "Incorrect checkin"

