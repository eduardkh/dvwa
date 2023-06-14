import requests
from bs4 import BeautifulSoup


def login(url, username, password):
    # make a GET request to the login page
    session = requests.Session()
    response = session.get(url)

    # parse the HTML response to find the CSRF token
    soup = BeautifulSoup(response.text, "html.parser")
    csrf_token = soup.find("input", attrs={"name": "user_token"})["value"]

    # now make a POST request to login, including the CSRF token
    login_data = {
        "username": username,
        "password": password,
        "Login": "Login",
        "user_token": csrf_token,
    }
    response = session.post(url, data=login_data, allow_redirects=False)

    # convert the cookie jar to a dictionary
    cookies_dict = {}
    for cookie in session.cookies:
        cookies_dict[cookie.name] = cookie.value

    # return the cookies and the CSRF token
    return cookies_dict, csrf_token


cookies, csrf_token = login(
    "http://10.200.13.100:8080/login.php", "admin", "password")
print(cookies)
print(csrf_token)
