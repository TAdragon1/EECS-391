import re
# variables
goal_state = list("b12345678")  # goal state
state = list("b12345678")  # start at the goal state before randomizing the state
max_nodes = 0

# methods
def setState(str):
 "This sets the state using the given input format: 'b12345678'"
 global state
 state = str
 return

def randomizeState(n):
 "This randomizes the state a certain number n of moves away from the goal state"
 global state

 return

def printState():
 "This prints the state"
 print("".join(state))
 return

def findB():
 "This returns the index of B in the state string"
 i = 0
 for tile in state:
  if tile == "b":
   return i
  i += 1


def move(dir):
 "This moves the blank tile either 'up', 'down', 'left', or 'right'"
 global state
 b = findB()  #b is the location of the blank tile indexed from 0 to 8 along the state string

 return

def maxNodes(n):
 "This sets the number of maximum nodes during a search"
 max_nodes=n
 return

# program
f = open("test.txt",'r',encoding = 'utf-8')
commands = []
for line in f:
 commands.append(re.split('\n', line)[0])

for cmd in commands:
 cmd_list = cmd.split()
 print(cmd_list)
 if cmd_list[0] == 'setState':
  setState(list(cmd_list[1]))
 elif cmd_list[0] == "randomizeState":
  randomizeState(cmd_list[1])
 elif cmd_list[0] == "printState":
  printState()
 elif cmd_list[0] == "move":
  move(cmd_list[1])
 elif cmd_list[0] == "maxNodes":
  maxNodes(cmd_list[1])


print(state)