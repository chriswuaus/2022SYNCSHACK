from lxml import html
import requests
import sys

class UoSScraper:
    def __init__(self) -> None:
        self.uos_url = None
        self.mode_url = "https://www.sydney.edu.au"

    
    def set_cur_url(self, new_url: str):
            self.uos_url = new_url
    
    #Sets up the tree object that I xpath (idk how to describe it properly)
    def uos_url_tree_setup(self):
        req = requests.get(self.uos_url)
        tree = html.fromstring(req.content)
        return tree

    #scrapes unit name
    def get_unit_name(self):
        tree = self.uos_url_tree_setup()
        req = tree.xpath("//h1[@class='pageTitle b-student-site__section-title']/text()")
        namespl = req[0].split(" ", 1)
        return namespl[1]

    #scrapes unit description
    def get_unit_desc(self):
        tree = self.uos_url_tree_setup()
        req = tree.xpath("//div[@class='pageTitleModule']//div[@class='b-summary']/p/text()")
        return req[0]

    #scrapes unit code
    def get_unit_code(self):
        tree = self.uos_url_tree_setup()
        req = tree.xpath("//div[@id='academicDetails']//tbody/tr[1]/td/text()")
        return req[0][4:]

    #add way to determine unit level
    def get_unit_level(self):
        tree = self.uos_url_tree_setup()
        req = tree.xpath("//div[@id='academicDetails']//tbody/tr[1]/td/text()")
        return req[0][4]

    #scrapes academic unit
    def get_unit_academic_unit(self):
        tree = self.uos_url_tree_setup()
        req = tree.xpath("//div[@id='academicDetails']//tbody/tr[2]/td/text()")
        return req[0]
    
    #scrapes credit point value
    def get_unit_cp_val(self):
        tree = self.uos_url_tree_setup()
        req = tree.xpath("//div[@id='academicDetails']//tbody/tr[3]/td/text()")
        return req[0]

    #scrapes all prerequisites for the unit (single string)
    def get_unit_prereq(self):
        tree = self.uos_url_tree_setup()
        req = tree.xpath("//div[@id='enrolmentRules']//tbody/tr[1]/td/text()")
        req_spl1 = req[0].split("AND")
        req_spl2 = "and".join(req_spl1)
        req_spl3 = req_spl2.split("and")
        return req_spl3
    
    #scrapes all co-requisites for the unit (single string)
    def get_unit_coreq(self):
        tree = self.uos_url_tree_setup()
        req = tree.xpath("//div[@id='enrolmentRules']//tbody/tr[2]/td/text()")
        req_spl1 = req[0].split("AND")
        req_spl2 = "and".join(req_spl1)
        req_spl3 = req_spl2.split("and")
        return req_spl3

    #scrapes all prohibitions for the unit (single string)
    def get_unit_prohib(self):
        tree = self.uos_url_tree_setup()
        req = tree.xpath("//div[@id='enrolmentRules']//tbody/tr[3]/td/text()")
        req_spl1 = req[0].split("AND")
        req_spl2 = "and".join(req_spl1)
        req_spl3 = req_spl2.split("and")
        return req_spl3

    #scrapes all assumned knowledge areas for the unit
    def get_assumed_knowledge(self):
        tree = self.uos_url_tree_setup()
        req = tree.xpath("//div[@id='enrolmentRules']//tbody/tr[4]/td/text()")
        req_spl1 = req[0].split("AND")
        req_spl2 = "and".join(req_spl1)
        req_spl3 = req_spl2.split("and")
        return req_spl3

    #set modeURL to CC for scraping mode specific information (extension) i.e. semester weekly schedule, assessment schedule
    def set_cc_url(self):
        tree = self.uos_url_tree_setup()
        req = tree.xpath("//div[@class='bodyContentContainer']//div[@id='currentOutlines']/ul/li[1]//@href")
        if len(req) != 0:
            self.mode_url = self.mode_url + req[0]
        else:
            self.mode_url = None

        return self.mode_url
    
    #find which semesters current unit is offered in
    def unit_offerings(self):
        tree = self.uos_url_tree_setup()
        req = tree.xpath("//div[@class='bodyContentContainer']//div[@id='currentOutlines']/ul/li")
        new_list = []
        if len(req) > 0:
            for elem in req:
                cur = elem.xpath("./a/text()")[0]
                if cur.find("Remote") == -1:
                    cur2 = cur.split()
                    st_new = str(cur2[0] + " " + cur2[1])
                    new_list.append(st_new[:-1])
        return new_list
    
    #sets up the tree for use in scraping outline content (extension)
    def mode_url_tree_setup(self):
        req = requests.get(self.mode_url)
        tree = html.fromstring(req.content)
        return tree

    
    

t1 = UoSScraper()
t1.set_cur_url("https://www.sydney.edu.au/units/MATH1005")
# print(t1.get_unit_name())
# print(t1.get_unit_desc())
# print(t1.get_unit_code())
# print(t1.get_unit_academic_unit())
# print(t1.get_unit_cp_val())
# print(t1.get_unit_prereq())
# print(t1.get_unit_coreq())
# print(t1.get_unit_prohib())
# print(t1.get_assumed_knowledge())
# print(t1.set_cc_url())
# print(t1.get_unit_level())
print(t1.unit_offerings())



