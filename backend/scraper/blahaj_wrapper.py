from uuid import uuid1
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

    def create_unit_groups(self, group_id, unit_id):
        guuid = self.get_guuid(group_id)
        uuid = self.get_uuid(unit_id)
        location = f"/unit-groups/{guuid}/units/{uuid}"

        endpoint = self.base_url + location
        r = requests.post(endpoint)

    def create_group(self, name):
        location = "/groups"
        data = {
            "name": name
        }
        
        endpoint = self.base_url + location
        r = requests.post(endpoint,headers=self.headers,params=data)

    def get_uuid(self, unit_id):
        location = f"/units/code/{unit_id}"

        endpoint = self.base_url + location
        r = requests.get(endpoint)
        return r.json()["id"]

    def get_guuid(self, group_name):
        location = f"/groups/group/{group_name}"

        endpoint = self.base_url + location
        r = requests.get(endpoint)
        return r.json()["id"]

    def create_prerequisite(self, unit_id, prerequisites):
        uuid = self.get_uuid(unit_id)
        location = f"/units/{uuid}/prerequisites"
        data = {
            "prerequisite_list": prerequisites
        }
        
        endpoint = self.base_url + location
        r = requests.post(endpoint,headers=self.headers,params=data)
    
    def create_prohibition(self, unit_id, prohibitions):
        uuid = self.get_uuid(unit_id)
        location = f"/units/{uuid}/prohibitions"
        data = {
            "prohibition_list": prohibitions
        }
        
        endpoint = self.base_url + location
        r = requests.post(endpoint,headers=self.headers,params=data)

    def create_corequisite(self, unit_id, corequisites):
        uuid = self.get_uuid(unit_id)
        location = f"/units/{uuid}/corequisites"
        data = {
            "corequisite_list": corequisites
        }
        
        endpoint = self.base_url + location
        r = requests.post(endpoint,headers=self.headers,params=data)

    def create_aknowledge(self, unit_id, aknowledge):
        uuid = self.get_uuid(unit_id)
        location = f"/units/{uuid}/assumed_knowledge"

        if aknowledge is None:
            aknowledge = ['No assumed knowledge']

        data = {
            "assumed_knowledge_list": aknowledge
        }
        
        endpoint = self.base_url + location
        r = requests.post(endpoint,headers=self.headers,params=data)