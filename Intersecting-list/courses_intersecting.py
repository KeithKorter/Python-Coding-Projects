COURSES = {
    "Python Basics": {"Python", "functions", "variables",
                      "booleans", "integers", "floats",
                      "arrays", "strings", "exceptions",
                      "conditions", "input", "loops"},
    "Java Basics": {"Java", "strings", "variables",
                    "input", "exceptions", "integers",
                    "booleans", "loops"},
    "PHP Basics": {"PHP", "variables", "conditions",
                   "integers", "floats", "strings",
                   "booleans", "HTML"},
    "Ruby Basics": {"Ruby", "strings", "floats",
                    "integers", "conditions",
                    "functions", "input"}
}


#intersecting

def covers(topics):
    list = []
    for course in COURSES:
        if topics & COURSES[course]:
            list.append(course)
    return list

#Multi
def covers_all(topics):
    list = []
    for course, values in COURSES.items():
        if(values & topics) == topics:
            list.append(course)
            
    return list