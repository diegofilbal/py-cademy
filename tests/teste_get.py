import requests

headers = {"Authorization": "Token 1f284f8fb51f911be9ae9153b89dc098f161122a"}
base_url_courses = "http://localhost:8000/api/v2/courses/"

result = requests.get(url=base_url_courses, headers=headers)

assert result.status_code == 200
assert result.json()["count"] == 6
assert result.json()["results"][0]["title"] == "RESTful API with Django"
