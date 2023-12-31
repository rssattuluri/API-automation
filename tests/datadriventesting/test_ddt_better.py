# Read the CSV or EXCEL file
# Create a Function create_token which can take values from the Excel File
# Verify the Expected Result

import pytest
import requests
import openpyxl
from src.constants.api_constants import APIConstants
from src.helpers.utils import common_headers_json

#Step -1: Read the file and put the content into a [array/set/dictionary]
def read_credentials_from_excel(file_path):
    credentials = []
    workbook = openpyxl.load_workbook(file_path)
    sheet = workbook.active

    for row in sheet.iter_rows(min_row=2, values_only=True):
        username, password = row
        credentials.append({"username": username, "password": password})
    return credentials

def make_request_auth(username, password):
    payload = {
        "username": username,
        "password": password
    }
    response = requests.post(APIConstants.url_create_token(), headers = common_headers_json(), json= payload)
    return response

# Create a Function create_token which can take values from the Excel File
@pytest.mark.parametrize("user_cred", read_credentials_from_excel("/Users/pancramy/PycharmProjects/Py1xAPIAutomation/tests/datadriventesting/testdata_ddt.xlsx"))
def test_post_create_token(user_cred):
        username = user_cred["username"]
        password = user_cred["password"]
        print(username, password)
        response = make_request_auth(username, password)
        print(response)
        #Here u can also write the logic for positive and negative
        assert response.status_code == 200