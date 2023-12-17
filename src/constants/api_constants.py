# Add your constants here
def base_url():
    return "https://restful-booker.herokuapp.com"


def url_create_booking():
    return "https://restful-booker.herokuapp.com/booking"


def url_create_token():
    return "https://restful-booker.herokuapp.com/auth"


# update, PUT, PATCH, DELETE - booking id (as URL changes with the booking id)
def url_patch_put_delete_booking(booking_id):
    return "https://restful-booker.herokuapp.com/booking/" + str(booking_id)

# using class(OOPS concept)

#Type of constants:
BASE_URL = "https://restful-booker.herokuapp.com"  # Normal constant

def base_url():
    return "https://restful-booker.herokuapp.com"  # function constant

# within the class constant
class APIConstants(object):
  @staticmethod  # A method which can be used by using the class name => APIConstants.base_url directly. No need to create a instance of static method.
  def base_url():
    return "https://restful-booker.herokuapp.com"
    
  @staticmethod  # Static is common for all the test cases
  def url_create_booking():
    return "https://restful-booker.herokuapp.com/booking"

  @staticmethod  # Dont need self for static function
  def url_create_token():
    return "https://restful-booker.herokuapp.com/auth"

  def url_patch_put_delete_booking(self, booking_id):
    return "https://restful-booker.herokuapp.com/booking/" + str(self.booking_id)

