import requests

headers = {"Authorization": "Token 1f284f8fb51f911be9ae9153b89dc098f161122a"}
base_url_courses = "http://localhost:8000/api/v2/courses/"

updated_course = {
    "title": "Updated course",
    "url": "https://www.metropoledigital.ufrn.br/portal/",
}

result = requests.put(url=f"{base_url_courses}3/", headers=headers, data=updated_course)
assert result.status_code == 200
assert (
    result.json()["title"] == updated_course["title"]
    and result.json()["url"] == updated_course["url"]
)
