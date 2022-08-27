import requests

url = "http://127.0.0.1:5001/units"
headers = {
    "content-type": "application/json"
}

data = {
    "name": "TEST NAME",
    "code": "TEST1001",
    "level": "1000",
    "semesters": "[Semester 1, Semester 2]",
    "academic_unit": "Computer Science",
    "cp": "6",
    "description": "TESTING TESTSINGs"
}

groups = {
    "name": "Table A Electives"
}
r = requests.post(url, headers=headers, params=data)
print(r.text)