class Visulaization:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def home(self):
        print(self.name, self.age)


viz = Visulaization("baburao",56)
viz.home()