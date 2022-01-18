from requests import get, exceptions

def check_internet_connection():
    try:
        get('http://google.com', timeout = 3)
        print('OK')
    except exceptions.ConnectionError:
        print('F')

check_internet_connection()
