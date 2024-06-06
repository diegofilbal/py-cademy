import requests


class TestCourses:
    headers = {"Authorization": "Token 1f284f8fb51f911be9ae9153b89dc098f161122a"}
    base_url_courses = "http://localhost:8000/api/v2/courses/"

    def test_get_courses(self):
        response = requests.get(url=self.base_url_courses, headers=self.headers)
        assert response.status_code == 200

    def test_get_course(self):
        response = requests.get(url=f"{self.base_url_courses}3/", headers=self.headers)
        assert response.status_code == 200

    def test_post_course(self):
        new = {"title": "New course1", "url": "https://newcourse1.com"}
        response = requests.post(
            url=self.base_url_courses, headers=self.headers, data=new
        )
        assert response.status_code == 201
        assert response.json()["title"] == new["title"]

    def test_put_course(self):
        to_update = {"title": "course to update 1", "url": "https://toupdate1.com"}
        response = requests.put(
            url=f"{self.base_url_courses}3/", headers=self.headers, data=to_update
        )
        assert response.status_code == 200

    def test_put_title_course(self):
        to_update = {"title": "course to update 2"}
        response = requests.put(
            url=f"{self.base_url_courses}3/", headers=self.headers, data=to_update
        )
        assert response.json()["title"] == to_update["title"]

    def test_delete_course(self):
        response = requests.delete(
            url=f"{self.base_url_courses}3/", headers=self.headers
        )
        assert response.status_code == 204 and len(response.text) == 0
