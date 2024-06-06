import requests

# GET Rates:
rates = requests.get("http://localhost:8000/api/v2/rates/")
print(rates.status_code)
print(rates.json(), "\n")

# GET Rate:
rate = requests.get("http://localhost:8000/api/v2/rates/7/")
print(rate.status_code)
print(rate.json(), "\n")

# GET Courses (Authentication required):
headers = {"Authorization": "Token 1f284f8fb51f911be9ae9153b89dc098f161122a"}
courses = requests.get(url="http://localhost:8000/api/v2/courses/", headers=headers)
print(courses.status_code)
print(courses.json(), "\n")
