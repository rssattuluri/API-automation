# HTTP status verification
def verify_http_status_code(response_data, expect_data):
    print(response_data.status_code)
    print(expect_data)
    assert expect_data == response_data.status_code, "Expected HTTP Status Code" + str(expect_data)


def verify_json_key_for_not_null(key):
    assert key != 0, "Key is non Empty" + key
    assert key > 0, "Key is grater than zero"


# To verify if token is non empty
def verify_response_key_should_not_be_none(key):
    assert key is not None

# To verify verification time
def verify_response_time():
    pass

# We can also verify the following here:
# Common verification
# HTTP status code
# Headers
# Data Verification
# Json schema

