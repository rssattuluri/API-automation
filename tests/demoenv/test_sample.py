from dotenv import load_dotenv
import os
def test_auth():
    load_dotenv()
    username = os.getenv("USERNAME")
    password = os.getenv("PASSWORD")
<<<<<<< HEAD
    print(username,password)
=======
    print(username,password)
>>>>>>> f1b566b8ccaf2721c6569f4f0d4856742452b6e4
