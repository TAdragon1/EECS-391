import re
import random
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
 for i in range(1, int(n)):
  nextMove = random.randint(1, 4)
  if nextMove == 1:
   move("up")
  elif nextMove == 2:
   move("down")
  elif nextMove == 3:
   move("left")
  else:  # nextMove == 4
   move("right")
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
 b = findB()  # b is the location of the blank tile indexed from 0 to 8 along the state string
 if dir == "up":
  if b > 2:  # b can be moved up
   temp = state[b - 3]
   state[b - 3] = state[b]
   state[b] = temp
  else:  # b cannot be moved up
   print("Cannot move up")
 elif dir == "down":
  if b < 6:  # b can be moved down
   temp = state[b + 3]
   state[b + 3] = state[b]
   state[b] = temp
  else:  # b cannot be moved down
   print("Cannot move down")
 elif dir == "left":
  if b != 0 and b != 3 and b != 6:  # b can be moved to the left
   temp = state[b - 1]
   state[b - 1] = state[b]
   state[b] = temp
  else:  # b cannot be moved to the left
   print("Cannot move left")
 elif dir == "right":
  if b != 2 and b != 5 and b != 8:  # b can be moved to the right
   temp = state[b + 1]
   state[b + 1] = state[b]
   state[b] = temp
  else:  # b cannot be moved to the right
   print("Cannot move right")
 return

def maxNodes(n):
 "This sets the number of maximum nodes during a search"
 global max_nodes
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