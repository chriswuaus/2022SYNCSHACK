import requests

class BlahajWrapper:
    def init(self):
        self.base_url = "localhost:3000"

    def get_unit(self):
        location = "/units"
        endpoint = self.base_url + location

        r = requests.get(endpoint)
        return r


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

    def get_unit_groups(self, unit_id):
        location = f"/unit-groups/{unit_id}/units"
        endpoint = self.base_url + location

        r = requests.get(endpoint)
        return r

    def create_unit_groups(self, group_id, unit_id):
        location = f"/unit-groups/{group_id}/unit/{unit_id}"

        endpoint = self.base_url + location
        r = requests.post(endpoint)

    def get_groups(self):
        location = "/groups"
        endpoint = self.base_url + location

        r = requests.get(endpoint)
        return r

    def create_group(self, group_id, name):
        location = "/units"
        data = {
            "group_id": group_id,
            "name": name
        }
        
        endpoint = self.base_url + location
        r = requests.post(endpoint)

    def get_prerequisites(self, unit_id):
        location = f"/unit/{unit_id}/prerequisuites/prerequisite"
        endpoint = self.base_url + location

        r = requests.get(endpoint)
        return r

    def create_prerequisite(self, unit_id, prerequisites):
        location = f"/unit/{unit_id}/prerequisuites"
        data = {
            "prerequisites": prerequisites
        }
        
        endpoint = self.base_url + location
        r = requests.post(endpoint)

    def get_prohibitions(self, unit_id):
        location = f"/unit/{unit_id}/prohibitions/prohibition"
        endpoint = self.base_url + location

        r = requests.get(endpoint)
        return r

    def create_prohibition(self, unit_id, prohibitions):
        location = f"/unit/{unit_id}/prohibitions"
        data = {
            "prohibitions": prohibitions
        }
        
        endpoint = self.base_url + location
        r = requests.post(endpoint)

    def get_corequisites(self, unit_id):
        location = f"/unit/{unit_id}/corequisites/corequisite"
        endpoint = self.base_url + location

        r = requests.get(endpoint)
        return r

    def create_corequisite(self, unit_id, corequisites):
        location = f"/unit/{unit_id}/corequisites"
        data = {
            "corequisites": corequisites
        }
        
        endpoint = self.base_url + location
        r = requests.post(endpoint)

    def get_aknowledge(self, unit_id):
        location = f"/unit/{unit_id}/assumed_knowledge/assumed_knowledge"
        endpoint = self.base_url + location

        r = requests.get(endpoint)
        return r

    def create_aknowledge(self, unit_id, aknowledge):
        location = f"/unit/{unit_id}/assumed_knowledge"
        data = {
            "aknowledge": aknowledge
        }
        
        endpoint = self.base_url + location
        r = requests.post(endpoint)