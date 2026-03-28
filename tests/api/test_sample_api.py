
import requests

def test_sample_api():
    res = requests.get("https://reqres.in/api/users?page=2")
    assert res.status_code == 200
