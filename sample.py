import requests
from requests import RequestTest


def exercise():
    return requests.post("http://www.google.com")


def test_method():

    requests.post = RequestTest.set_post(expected_value="afd7s980f7sd98")
    r = exercise()
    print(r)


if __name__ == '__main__':
    test_method()
