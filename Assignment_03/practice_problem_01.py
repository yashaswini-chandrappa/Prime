'''STUDENT ENROLMENTS
Given a list of tuples with info(name, subject):
    1. List of all unique course
    2. List of students enrolled in English
    3. Create a dictionary(student, set of coureses)
'''

info = [
    ("Alice", "Math"),
    ("Bob", "Science"),
    ("Alice", "Science"),
    ("Charlie","Math"),
    ("Bob", "Math"),
    ("Alice", "English"),
    ("Charlie", "English")
]

unique_coures = set ()
english_students = set()
dict = {}
for tup in info: # can also use (for name, course in info:)
     unique_coures.add(tup[1])
     if(tup[1]=='English'):
          english_students.add(tup[0])   
print(unique_coures)
print(english_students)
for name,course in info:
      if(dict.get(name)==None):
          dict.update({name : set()})
          dict[name].add(course)
      else:
          dict[name].add(course)
print(dict)

