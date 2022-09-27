from utils.utils import *
from utils.professors import Professor
from utils.schools import School

# Append hired professors to schools and change their state to hired
def hire(school_id, prof_id, professors, schools):
    schools[school_id].hired.append(prof_id)
    schools[school_id].acquired_skills.append(professors[prof_id].skills)

    professors[prof_id].hired = 1
    professors[prof_id].hired_by = school_id
    
# Rejects professors when there's a better match
def reject(school_id, worst_id, professors, schools):
    prof_id = schools[school_id].hired[worst_id]
    professors[prof_id].hired = 0
    professors[prof_id].hired_by = ""
    professors[prof_id].rejections.append(school_id)

    schools[school_id].hired.pop(worst_id)
    schools[school_id].acquired_skills.pop(worst_id)
    schools[school_id].candidates.remove(prof_id)

# Puts candidates in reserve
def reserve_candidates(professors):
    applicants = []
    for prof in professors.values():
        if prof.hired == 0 and (len(prof.desired_schools) != len(prof.rejections)):
            applicants.append(prof.id)
    return applicants

# Defines the best school match for each professor based on
# their desired schools and the school candidates
def best_school_match(prof_id, professors, schools):
    for school_id in professors[prof_id].desired_schools:
        if prof_id in schools[school_id].candidates:
            return school_id
    return -1

# Main Stable matching function
def stable_matching(professors, schools):
    for prof_id in professors:
        for school_id in professors[prof_id].desired_schools:
            
            if professors[prof_id].skills >= min(schools[school_id].desired_skills):
                schools[school_id].candidates.append(prof_id)
            else:
                professors[prof_id].rejections.append(school_id)

    available_candidates = reserve_candidates(professors)

    while (len(available_candidates) != 0):
        prof_id = available_candidates[0]
        school_id = best_school_match(prof_id, professors, schools)
        
        hire(school_id, prof_id, professors, schools)

        hired_ammount = len(schools[school_id].hired)
        vacant = len(schools[school_id].desired_skills)
        
        if (hired_ammount == vacant):
            min_skills = min(schools[school_id].acquired_skills)
            for candidato in schools[school_id].candidates:
                if professors[candidato].skills < min_skills:
                    schools[school_id].candidates.remove(candidato)
                    professors[candidato].rejections.append(school_id)


        if (hired_ammount > vacant):
            worst_match = schools[school_id].acquired_skills.index(min(schools[school_id].acquired_skills))
            reject(school_id, worst_match, professors, schools)

        available_candidates = reserve_candidates(professors)

def main():
    professors, schools = get_data()
    stable_matching(professors, schools)
    print_stable_matchings(schools)

main()