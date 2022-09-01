def get_data():
    '''Get data from file <filename> and appends it to a list'''
    
    # Opens professor skills file and read lines
    professors_file = open("../professors.txt", "r")
    professors_lines = professors_file.readlines()
    
    # Opens  file and read lines
    schools_file = open("../schools.txt", "r")
    schools_lines = schools_file.readlines()
    
    # Makes a dict with keys = Professors and values = skills
    # and another with keys = Professors and values = desired schools
    professors_skills = {}
    professors_schools = {}
    schools = []
    for line in professors_lines:
        schools.clear()
        (k, v) = line.strip().replace("(", "").replace(")", "").split(": ")
        (professor_id, professor_skills) = k.split(",")
        
        # Makes a list of schools
        for school in v.split(","):
            schools.append(school)
        professors_schools[professor_id] = schools
        professors_skills[professor_id] = int(professor_skills)
    print("------------Professors' Skills------------")
    print(professors_skills)
    print()
    print("------------Professors' Desired Schools------------")
    print(professors_schools)
    print()
    professors_file.close()
    
    # Makes a dict with keys = schools and values = desired skills
    schools_skills = {}
    skills_list = []
    for line in schools_lines:
        skills_list.clear()
        (k, v) = line.strip().replace("(", "").replace(")", "").split(":", 1)
        if ":" in v:
            (v1, v2) = v.split(":")
            skills_list.append(int(v1))
            skills_list.append(int(v2))
        else:
            skills_list.append(v)
            
        schools_skills[k] = skills_list
    print("------------Schools' Desired Skills------------")
    print(schools_skills)
    print()
    schools_file.close()
    
    
    return
