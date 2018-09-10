import re

f = open("test.txt",'r',encoding = 'utf-8')
commands = []
for line in f:
 commands.append(re.split('\n', line)[0])
 print(line, end = '')

print(commands)
for element in commands:
 print(element)

for cmd in commands:
 if cmd == 'setState <state>':
  print('Hi')