class Sagarmatha:
    def ___init__(self, no_of_departments = 2, no_of_students = 1000,no_of_faculty = 100):
        self.affilaition = "TU"
        self.no_of_departments = no_of_departments
        self.location = "Sanepa"
        self.no_of_students = no_of_students
        self.no_of_faculty = no_of_faculty
    def canteen_profit(self):
        return self.no_of_students * 0.1 * 10

class ScienceTechnology(Sagarmatha):
        def ___init__(self, no_of_departments = 2, no_of_students = 1000,no_of_faculty = 100):
            super().__init__(no_of_departments, no_of_students,no_of_faculty)
            # self.affilaition = "TU"
            # self.no_of_departments = no_of_departments
            # self.location = "Sanepa"
            # self.no_of_students = no_of_students
            # self.no_of_faculty = no_of_faculty
def canteen_loss(self):
    return self.no_of_students * 0.1 * 10
obj = ScienceTechnology()
print(obj.canteen_profit())