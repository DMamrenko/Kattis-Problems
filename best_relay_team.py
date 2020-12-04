#Kattis: Best Relay Team

class Runner:
    def __init__(self, name, first_leg, other_leg):
        self.name = name
        self.first_leg = first_leg
        self.other_leg = other_leg
    def show(self):
        print('{} {} {}'.format(self.name, self.first_leg, self.other_leg))
    def show_name(self):
        print(self.name)

    

runners = int(input())
rlist = []

for i in range(runners):
    name, first_leg, other_leg = input().split()
    rlist.append(Runner(name, float(first_leg), float(other_leg)))


slist = sorted(rlist, key=lambda runner: runner.other_leg)

last_three = slist[:3]

sslist = sorted(slist[3:], key=lambda runner: runner.first_leg)

lineup = sslist[:1] + last_three

print()
for f in lineup:
    f.show_name()
# print('runners')
# for r in rlist:
#     r.show()

# print()

# print('BY OTHER LEG')
# for s in slist:
#     s.show()

# print()

# print('BY FIRST LEG')
# for ss in sslist:
#     ss.show()

