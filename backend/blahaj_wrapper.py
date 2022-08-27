import requests

class BlahajWrapper:
    def init(self, url):
        self.base_url = url


    def create_unit(self, name, code, level, semesters):
        location = "/units"
        data = {
            "name": name,
            "code": code,
            "level": level,
            "semesters": semesters
        }

        endpoint = self.base_url + location
        r = requests.post(endpoint, data)

    def create_unit_groups(self, group_id, unit_id):
        location = f"/unit-groups/{group_id}/unit/{unit_id}"

        endpoint = self.base_url + location
        r = requests.post(endpoint)

    def create_group(self, group_id, name):
        location = "/units"
        data = {
            "group_id": group_id,
            "name": name
        }
        
        endpoint = self.base_url + location
        r = requests.post(endpoint)

    def create_prerequisite(self, unit_id, prerequisites):
        location = f"/unit/{unit_id}/prerequisuites"
        data = {
            "prerequisites": prerequisites
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