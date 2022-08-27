import requests

class BlahajWrapper:
    def init(self, url):
        self.base_url = url


    def create_unit(self, name, code, level, semesters, academic_unit, cp, desc):
        location = "/units"
        data = {
            "name": name,
            "code": code,
            "level": level,
            "semesters": semesters,
            "academic_unit": academic_unit,
            "cp": cp,
            "desc": desc
        }

        endpoint = self.base_url + location
        r = requests.post(endpoint, data)

    def create_unit_groups(self, group_id, unit_id):
        location = f"/unit-groups/{group_id}/unit/{unit_id}"

        endpoint = self.base_url + location
        r = requests.post(endpoint)

    def create_group(self, name):
        location = "/units"
        data = {
            "name": name
        }
        
        endpoint = self.base_url + location
        r = requests.post(endpoint, data)

    def create_prerequisite(self, unit_id, prerequisites):
        location = f"/unit/{unit_id}/prerequisuites"
        data = {
            "prerequisuites": prerequisites
        }
        
        endpoint = self.base_url + location
        r = requests.post(endpoint, data)

    def create_prohibition(self, unit_id, prohibitions):
        location = f"/unit/{unit_id}/prohibitions"
        data = {
            "prohibitions": prohibitions
        }
        
        endpoint = self.base_url + location
        r = requests.post(endpoint, data)

    def create_corequisite(self, unit_id, corequisites):
        location = f"/unit/{unit_id}/corequisites"
        data = {
            "corequisites": corequisites
        }
        
        endpoint = self.base_url + location
        r = requests.post(endpoint, data)

    def create_aknowledge(self, unit_id, aknowledge):
        location = f"/unit/{unit_id}/assumed_knowledge"
        data = {
            "aknowledge": aknowledge
        }
        
        endpoint = self.base_url + location
        r = requests.post(endpoint)