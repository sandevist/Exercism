# note to self -->  expected in tests refers to what added() should return, not what roster() returns

class School:
    def __init__(self):
        
        self.CLASSES = {}
        self.result = []

    def add_student(self, name, grade):

        student_not_added = not any(name in stu_list for stu_list in self.CLASSES.values())
        
        if student_not_added:

            if grade in self.CLASSES:
                self.CLASSES[grade].append(name)
                self.CLASSES[grade].sort()
            else:
                self.CLASSES[grade] = [name]
        
        self.result.append(student_not_added)

    def roster(self):
        roll = []
        for grades in sorted(self.CLASSES):
            roll.extend(sorted(self.CLASSES[grades]))
        return roll

    def grade(self, grade_number):
        if grade_number in self.CLASSES:
            return sorted(self.CLASSES[grade_number])
        return []

    def added(self):
        
        return self.result



