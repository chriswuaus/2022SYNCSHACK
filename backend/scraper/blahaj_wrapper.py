import requests

class BlahajWrapper:
    def __init__(self, url):
        self.base_url = url
        self.headers = {
            "content-type": "application/json"
        }


    def create_unit(self, name, code, level, semesters, academic_unit, cp, desc):
        location = "/units"
        data = {
            "name": name,
            "code": code,
            "level": level,
            "semesters": semesters,
            "academic_unit": academic_unit,
            "cp": cp,
            "description": desc
        }

        endpoint = self.base_url + location
        r = requests.post(endpoint,headers=self.headers,params=data)
        print(r.text)

    def create_unit_groups(self, group_id, unit_id):
        location = f"/unit-groups/{group_id}/unit/{unit_id}"

        endpoint = self.base_url + location
        r = requests.post(endpoint)
        print(r.text)

    def create_group(self, name):
        location = "/units"
        data = {
            "name": name
        }
        
        endpoint = self.base_url + location
        r = requests.post(endpoint,headers=self.headers,params=data)
        print(r.text)

    def create_prerequisite(self, unit_id, prerequisites):
        location = f"/unit/{unit_id}/prerequisites"
        data = {
            "prerequisuites": prerequisites
        }
        
        endpoint = self.base_url + location
        r = requests.post(endpoint,headers=self.headers,params=data)
        print(r.text)

    def create_prohibition(self, unit_id, prohibitions):
        location = f"/unit/{unit_id}/prohibitions"
        data = {
            "prohibitions": prohibitions
        }
        
        endpoint = self.base_url + location
        r = requests.post(endpoint,headers=self.headers,params=data)
        print(r.text)

    def create_corequisite(self, unit_id, corequisites):
        location = f"/unit/{unit_id}/corequisites"
        data = {
            "corequisites": corequisites
        }
        
        endpoint = self.base_url + location
        r = requests.post(endpoint,headers=self.headers,params=data)
        print(r.text)

    def create_aknowledge(self, unit_id, aknowledge):
        location = f"/unit/{unit_id}/assumed_knowledge"
        data = {
            "assumed_knowledge": aknowledge
        }
        
        endpoint = self.base_url + location
        r = requests.post(endpoint)
        print(r.text)