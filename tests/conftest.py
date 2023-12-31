import pytest
import requests
from src.constants.api_constants import APIConstants
from src.helpers.api_request_wrapper import post_requests
from src.helpers.common_verification import verify_http_status_code, verify_response_key_should_not_be_none
from src.helpers.payload_manager import payload_create_booking, payload_create_token
from src.helpers.utils import common_headers_json


@pytest.fixture(scope = "class")
def create_token():
    response = post_requests(url=APIConstants.url_create_token(), auth=None, payload=payload_create_token(),
                             headers=common_headers_json(), in_json=False)
    verify_http_status_code(response, 200)
    token = response.json()["token"]
    print(token)
    verify_response_key_should_not_be_none(token)
    return token


@pytest.fixture(scope = "class")
def create_booking():
    response = post_requests(url=APIConstants.url_create_booking(), auth=None, headers=common_headers_json(),
                             payload=payload_create_booking(), in_json=False)
    print(response)
    bookingid = response.json()["bookingid"]
    print(bookingid)
    verify_response_key_should_not_be_none(response.json()["bookingid"])
    verify_http_status_code(response, 200)
    return bookingid
