class School():
    '''School class to define a School with it's hired professors, candidates, 
    desired and acquired skills'''
    def __init__(self, id, skills):
        self.id = id
        self.hired = []
        self.candidates = []
        self.acquired_skills = []
        self.desired_skills = [int(x) for x in skills]