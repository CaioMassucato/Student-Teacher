from utils.schools import School
from utils.professors import Professor

def get_data():
    '''Get data from files and inserts the data into dictionaries
    and initializes instances of Professor and School classes'''
    
    professors = {}
    schools = {}
    
    # Opens professor skills file and read lines
    professors_file = open("../professors.txt", "r")
    professors_lines = professors_file.readlines()
    
    # Opens  file and read lines
    schools_file = open("../schools.txt", "r")
    schools_lines = schools_file.readlines()
    
    # Makes a dict with keys = Professors and values = skills
    # and a list for desired schools
    professors_skills = {}
    schools_list = []
    for line in professors_lines:
        schools_list.clear()
        (k, v) = line.strip().replace("(", "").replace(")", "") .split(": ")
        (professor_id, professor_skills) = k.split(",")
        professors_skills[professor_id] = professor_skills
        professors[professor_id] = Professor(professor_id, professor_skills, v.strip().replace(" ", "").split(","))
    professors_file.close()
    
    skills_list = []
    for line in schools_lines:
        skills_list.clear()
        (k, v) = line.strip().replace("(", "").replace(")", "").replace(" ", "").split(":", 1)
        if ":" in v:
            (v1, v2) = v.split(":")
            skills_list.append(int(v1))
            skills_list.append(int(v2))
        else:
            skills_list.append(v)
        schools[k] = School(k, skills_list)
    schools_file.close()
    
    
    return professors, schools

def print_stable_matchings(schools):
    count = 0
    for school in schools.values():
        count += 1
        print(school.id, school.hired)
    print("----------------------------")
    print("Number of Stable Matchings: ", count)
