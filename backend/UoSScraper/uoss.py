from lxml import html
import requests
import sys

class UoSScraper:
    def __init__(self) -> None:
        self.uosURL = None
        self.modeURL = "https://www.sydney.edu.au"

    
    def set_cur_url(self, new_url: str):
            self.uosURL = new_url
    
    #Sets up the tree object that I xpath (idk how to describe it properly)
    def uos_url_tree_setup(self):
        req = requests.get(self.uosURL)
        tree = html.fromstring(req.content)
        return tree

    #scrapes unit code and name
    def get_unit_name(self):
        tree = self.uos_url_tree_setup()
        req = tree.xpath("//h1[@class='pageTitle b-student-site__section-title']/text()")
        return req[0]

    #scrapes unit code
    def get_unit_code(self):
        tree = self.uos_url_tree_setup()
        req = tree.xpath("//div[@id='academicDetails']//tbody/tr[1]/td/text()")
        return req[0]

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
        return req[0]
    
    #scrapes all co-requisites for the unit (single string)
    def get_unit_coreq(self):
        tree = self.uos_url_tree_setup()
        req = tree.xpath("//div[@id='enrolmentRules']//tbody/tr[2]/td/text()")
        return req[0]

    #scrapes all prerequisites for the unit (single string)
    def get_unit_prohib(self):
        tree = self.uos_url_tree_setup()
        req = tree.xpath("//div[@id='enrolmentRules']//tbody/tr[3]/td/text()")
        return req[0]

    #set modeURL to CC for scraping mode specific information (extension) i.e. semester weekly schedule, assessment schedule
    def set_cc_url(self):
        tree = self.uos_url_tree_setup()
        req = tree.xpath("//div[@class='bodyContentContainer']//div[@id='currentOutlines']/ul/li[1]//@href")
        self.modeURL = self.modeURL + req[0]

        return self.modeURL
    
    #sets up the tree for use in scraping outline content (extension)
    def mode_url_tree_setup(self):
        req = requests.get(self.modeURL)
        tree = html.fromstring(req.content)
        return tree
    

t1 = UoSScraper()
t1.set_cur_url("https://www.sydney.edu.au/units/ISYS2120")
print(t1.get_unit_name())
print(t1.get_unit_code())
print(t1.get_unit_academic_unit())
print(t1.get_unit_cp_val())
print(t1.get_unit_prereq())
print(t1.get_unit_coreq())
print(t1.get_unit_prohib())
print(t1.set_cc_url())



