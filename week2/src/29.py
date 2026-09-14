from operator import methodcaller
s = 'The time has come'
upcase = methodcaller('upper')

print(upcase(s))

print(s.upper())

hiphenate = methodcaller('replace', ' ', '-')
print(hiphenate(s))