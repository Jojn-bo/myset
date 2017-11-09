import copy

person = ['name',['saving',100]]
'''
p1 = copy.copy(person)
p2 = person[:]
p3 = list(person)
'''

p1 = person[:]
p2 = person[:]

p1[0]='man'
p2[0]='woman'

p1[1][1]=50

print(p1)
print(p2)

