from uos_scraper import UoSScraper
from cusp_scraper import CUSPScraper
from blahaj_wrapper import BlahajWrapper

def post_data(uos, blahaj, elective, group, endpoint, groups_created):
    uos.set_cur_url(endpoint)
    aknowledge = uos.get_assumed_knowledge()
    academic_unit = uos.get_unit_academic_unit()
    code = uos.get_unit_code()
    coreq = uos.get_unit_coreq()
    cp =uos.get_unit_cp_val()
    desc = uos.get_unit_desc()
    level = uos.get_unit_level()
    name = uos.get_unit_name()
    prereq = uos.get_unit_prereq()
    prohib = uos.get_unit_prohib()
    semesters = uos.unit_offerings()

    blahaj.create_unit(name, code, level, semesters, academic_unit, cp, desc)
    blahaj.create_prerequisite(code, prereq)
    blahaj.create_prohibution(code, prohib)
    blahaj.create_corequisite(code, coreq)
    blahaj.create_aknowledge(code, aknowledge)


    if elective:
        if group not in groups_created:
            blahaj.create_group(group)
        blahaj.create_unit_groups(group, code)


cusp_cs = CUSPScraper("https://cusp.sydney.edu.au/students/view-degree-page/degree_id/751")
cusp_cs.run_all()
cusp_ds = CUSPScraper("https://cusp.sydney.edu.au/students/view-degree-page/degree_id/754")
cusp_ds.run_all()

uos_base = "https://www.sydney.edu.au/units/"
uos = UoSScraper()

blahaj = BlahajWrapper("localhost:3000")

units_posted = list()
groups_created = list()
endpoint = ""

for year in cusp_cs.cusp:
    for semester in year:
        for unit in semester:
            if "Electives" in unit:
                for elective_unit in unit:
                    if elective_unit in units_posted:
                        continue
                    endpoint = uos_base + elective_unit
                    post_data(uos, blahaj, True, unit, endpoint, groups_created)
                    units_posted.append(elective_unit)
            else:
                if unit in units_posted:
                    continue
                endpoint = uos_base + unit
                post_data(uos, blahaj, False, "", endpoint, groups_created)
                units_posted.append(unit)




