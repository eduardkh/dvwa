import requests
from bs4 import BeautifulSoup

# make a GET request to the login page
URL = "http://192.168.1.165:8080/login.php"
session = requests.Session()
response = session.get(URL)

# parse the HTML response to find the CSRF token
soup = BeautifulSoup(response.text, 'html.parser')
csrf_token = soup.find('input', attrs={'name': 'user_token'})['value']

# now make a POST request to login, including the CSRF token
login_data = {
    'username': 'admin',
    'password': 'password',
    'Login': 'Login',
    # make sure the csrf_token is mapped to 'user_token', not 'csrf_token'
    'user_token': csrf_token,
}
response = session.post(URL, data=login_data, allow_redirects=False)

# create a dictionary of the response
response_dict = {
    'status_code': response.status_code,
    'headers': dict(response.headers),
    'body': response.text
}

print(response_dict)
