import requests

headers = {"Authorization": "Token 1f284f8fb51f911be9ae9153b89dc098f161122a"}
base_url_courses = "http://localhost:8000/api/v2/courses/"

result = requests.delete(url=f"{base_url_courses}3/", headers=headers)
assert result.status_code == 204
assert len(result.text) == 0
