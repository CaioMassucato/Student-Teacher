class Professor():
    '''Professor class to define a Professor with his skills, desired schools, 
    if he is hired or not, the school that hired him and his rejections'''
    def __init__(self, id, skills, desired_schools):
        self.id = id
        self.skills = int(skills)
        self.desired_schools = desired_schools
        self.hired = 0
        self.hired_by = ""
        self.rejections = []