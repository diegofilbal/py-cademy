import requests

headers = {"Authorization": "Token 1f284f8fb51f911be9ae9153b89dc098f161122a"}
base_url_courses = "http://localhost:8000/api/v2/courses/"

new_course = {"title": "Teste course", "url": "https://google.com"}

result = requests.post(url=base_url_courses, headers=headers, data=new_course)
assert result.status_code == 201
assert (
    result.json()["title"] == new_course["title"]
    and result.json()["url"] == new_course["url"]
)
