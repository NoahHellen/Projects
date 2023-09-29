class University:
    def __init__(self, settlement_name, student_population, social_class, entry_standards, social_scene):
        self.settlement_name = settlement_name
        self.student_population = student_population
        self.social_class = social_class
        self.entry_standards = entry_standards
        self.social_scene = social_scene

class Subject:
    def __init__(self, lower_entry_requirement, higher_entry_requirement):
        self.low_entry_requirement = lower_entry_requirement
        self.high_entry_requirement = higher_entry_requirement

class Student:
    def __init__(self, age, name, a_level_results, subject):
        self.age = age
        self.name = name
        self.a_level_results = a_level_results
        self.subject = subject
    
Cambridge = University("Cambridge", 20000, "Upper", "High", "Low")
Durham = University("Durham", 22000, "Upper", "High", "Medium")
Loughborough = University("Loughborough", 20000, "Lower", "High", "Medium")
Leeds = University("Leeds", 37000, "Lower", "Low", "High")

Maths = Subject("AAA", "A*A*A")
Chemisty = Subject('AAB', 'A*AA')
Psychology = Subject('ABB', 'AAA')
Business = Subject('BBB', 'AAB')

student_name = input("This program is designed to help you find the perfect university and subject for you! Firstly, please type in your name: ")
deciding_factor = input("Hi " + str(student_name) + ", what would you say is the deciding factor for choosing your university? Type either: 'social class', 'entry standards' or 'social scene' ")

while deciding_factor != 'social class' and deciding_factor != 'entry standards' and deciding_factor != 'social scene':
  deciding_factor = input("Whoops, it looks like you didn't choose 'social class' or ''. Try selecting one again! ")

if choice == 'social scene':
    