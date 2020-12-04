#Roll Call

class Person():
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
    

ppl = ['Will Smith', 'Agent Smith', 'Peter Pan', 'Micky Mouse', 'Minnie Mouse', 'Peter Gunn']
people = []

for i in ppl:
    fname, lname = i.split()
    people.append(Person(fname, lname))
##while True:
##    try:
##        fname, lname = input().split()
##        person = Person(fname, lname)
##        people.append(person)
##    except EOFError:
##        break
    


people.sort(key=lambda x: x.lname, reverse=False)
for i in people:
    print(i.fname, i.lname)
    
