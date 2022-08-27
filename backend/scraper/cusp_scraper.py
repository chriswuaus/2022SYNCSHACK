from lxml import html, etree
import requests
import sys

class CUSPScraper:
    def __init__(self, url):
        self.cusp = dict()
        self.url = url
        self.aelectives = [
            "COMP2022",
            "COMP2017",
            "COMP3027",
            "COMP3888"
        ]
        self.advelectives = [
            "COMP5045",
            "COMP5048",
            "COMP5349"
        ]
        self.html_tree = self.get_html_content()

    def run_all(self):
        self.parse_cusp()

    def get_html_content(self):
        request = requests.get(self.url)
        content = request.content
        return html.fromstring(content)

    def parse_cusp(self):
        all_sems = self.html_tree.xpath("//div[@id='semesters']//table[@class='t_b']")
        years = len(all_sems)//2
        for year in range(years):
            curr_year = "Year" + str(year+1)
            self.cusp[curr_year] = {"Semester1": None, "Semester2": None}

        sem_count = 1
        curr_year = 0
        for sem in all_sems:
            units = list()
            rows = sem.xpath(".//tr[position()>1]")
            for row in rows:
                uos = row.xpath("./td[3]/a/text()")[0]
                unit = uos.split(": ")[0]
                if "a elective" in unit.lower():
                    units.append({unit:self.aelectives})
                elif "adv. elective" in unit.lower():
                    units.append({unit:self.advelectives})
                else:
                    units.append(unit)
            if sem_count % 2 == 0:
                semester = "Semester2"
            else:
                semester = "Semester1"
                curr_year += 1
            key_year = "Year" + str(curr_year)
            self.cusp[key_year][semester] = units
            sem_count += 1

# url = "https://cusp.sydney.edu.au/students/view-degree-page/degree_id/754"
# cusp = CUSPScraper(url)
# cusp.run_all()
# print(cusp.cusp)