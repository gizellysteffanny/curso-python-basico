from collections import namedtuple as nt

Employee = nt('Employee', ['name', 'gender', 'salary'])

# Jeito reduzido de criar uma classe, como se fosse uma struct
c1 = Employee(name='Gizelly', gender='F', salary=2000)
c2 = Employee(name='Luis', gender='M', salary=4000)
c3 = Employee(name='Alexandre', gender='M', salary=8000)

print(c1)
print(c2)
print(c3)

print(type(c1))
