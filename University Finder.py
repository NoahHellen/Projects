class University:
    def __init__(self, name, student_population, social_class, entry_standards, social_scene):
        self.name = name
        self.student_population = student_population
        self.social_class = social_class
        self.entry_standards = entry_standards
        self.social_scene = social_scene
    
    def __repr__(self):
        return "{name} is a university with a student population of {population}. The social class is {socialclass} class, and the social scene is {social}. Finally, the entry standards are {standards}.".format(name = self.name, population = self.student_population, socialclass = self.social_class, social = self.social_class, standards = self.entry_standards)

class Subject:
    def __init__(self, low_entry_requirement, high_entry_requirement):
        self.low_entry_requirement = low_entry_requirement
        self.high_entry_requirement = high_entry_requirement

class Student:
    def __init__(self, age, name, a_level_results, subject):
        self.age = age
        self.name = name
        self.a_level_results = a_level_results
        self.subject = subject
    
    def __repr__(self):
        return "This student is called {name}, is {age} years old, got {results} A level results, and is hoping to study {subject} at university.".format(name = self.name, age = self.age, results=self.a_level_results, subject = self.subject)
    
Cambridge = University("Cambridge", 20000, "Upper", "High", "Low")
Durham = University("Durham", 22000, "Upper", "High", "Medium")
Loughborough = University("Loughborough", 20000, "Middle", "High", "Medium")
Leeds = University("Leeds", 37000, "Lower", "Low", "High")

Maths = Subject("AAA", "A*A*A")
Chemisty = Subject('AAB', 'A*AA')
Psychology = Subject('ABB', 'AAA')
Business = Subject('BBB', 'AAB')

university_list = [Cambridge, Durham, Loughborough, Leeds]

low_social_scene_list = []
medium_social_scene_list = []
high_social_scene_list = []

low_entry_standards_list = []
high_entry_standards_list = []

upper_class_list = []
middle_class_list = []
lower_class_list = []

for i in university_list:
    if i.social_class == "Upper":
        upper_class_list.append(i.name)
    if i.social_class == "Middle":
        middle_class_list.append(i.name)
    if i.social_class == "Lower":
        lower_class_list.append(i.name)

for i in university_list:
    if i.entry_standards == "High":
        high_entry_standards_list.append(i.name)
    if i.entry_standards == "Low":
        low_entry_standards_list.append(i.name)

for i in university_list:
    if i.social_scene == 'High':
        high_social_scene_list.append(i.name)
    if i.social_scene == 'Medium':
        medium_social_scene_list.append(i.name)
    if i.social_scene == 'Low':
        low_social_scene_list.append(i.name)
        

student_name = input("This program is designed to help you find the perfect university and subject for you! Firstly, please type in your first name: ")
student_a_level_results = input("Next, what were you A level results? Type them in descending order: ")
student_age = input("Next, what is your age? ")
student_subject = input("Finally, what is your subject of choice? ")

first_student = Student(student_age, student_name, student_a_level_results, student_subject)

print(first_student)

deciding_factor = input("Hi " + str(student_name) + ", what would you say is the deciding factor for choosing your university? Type either: 'social class', 'entry standards' or 'social scene': ")

while deciding_factor != 'social class' and deciding_factor != 'entry standards' and deciding_factor != 'social scene':
  deciding_factor = input("Whoops, it looks like you didn't choose 'social class', 'entry standards' or 'social scene'. Try selecting one again! ")

if deciding_factor == 'social scene':
    social_scene_factor = input("Ok, sounds good. Type either 'low', 'medium' or 'high' for the type of social scene you want ")
    if social_scene_factor == 'high':
        print("Ok, you have the options of {universities}".format(universities = str(high_social_scene_list)))
    elif social_scene_factor == 'medium':
        print("Ok, you have the options of {universities}".format(universities = str(medium_social_scene_list)))
    elif social_scene_factor == 'low':
        print("Ok, you have the option of {universities}".format(universities = str(low_social_scene_list)))

if deciding_factor == 'entry standards':
    entry_standards_factor = input("Ok, sounds good. Type either 'low' or 'high' for the entry standards you are looking at: ")
    if entry_standards_factor == 'high':
        print("Ok, you have the options of {universities}".format(universities = str(high_entry_standards_list)))
    if entry_standards_factor == 'low':
        print("Ok, you have the options of {universities}".format(universities = str(low_entry_standards_list)))

if deciding_factor == 'social class':
    entry_standards_factor = input("Ok, sounds good. Type either 'upper', 'middle' or 'lower' for the social class you are looking for ")
    if entry_standards_factor == 'upper':
        print("Ok, you have the options of {universities}".format(universities = str(upper_class_list)))
    if entry_standards_factor == 'middle':
        print("Ok, you have the options of {universities}".format(universities = str(middle_class_list)))
    if entry_standards_factor == 'lower':
        print("Ok, you have the options of {universities}".format(universities = str(lower_class_list)))

preferred_university = input("Ok, so out of the options, which one would like to explore some more: ")

if preferred_university == "Durham":
    print(Durham)
if preferred_university == "Cambridge":
    print(Cambridge)
if preferred_university == "Loughborough":
    print(Loughborough)
if preferred_university == "Leeds":
    print(Leeds)
