import jsonpath
import requests

rates = requests.get("http://localhost:8000/api/v2/rates/")

results = jsonpath.jsonpath(rates.json(), "results")
print(results)

first_element = jsonpath.jsonpath(rates.json(), "results[0]")
print(first_element)

name = jsonpath.jsonpath(rates.json(), "results[0].name")
print(name)

rating = jsonpath.jsonpath(rates.json(), "results[0].rate")
print(rating)

names = jsonpath.jsonpath(rates.json(), "results[*].name")
print(names)

ratings = jsonpath.jsonpath(rates.json(), "results[*].rate")
print(ratings)
