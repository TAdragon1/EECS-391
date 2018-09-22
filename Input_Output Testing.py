import re
import random
from queue import PriorityQueue

# variables
goal_state = list("b12345678")  # goal state
state = list("")  # set to empty
max_nodes = 0

# methods
def setState(str):
 "This sets the state using the given input format: 'b12345678'"
 global state
 state = str
 return

def randomizeState(n):
 "This randomizes the state a certain number n of moves away from the goal state"
 if n == 0:  #  base case
  return
 global state
 nextMove = random.randint(1, 4)
 if nextMove == 1:
  m = move("up")
 elif nextMove == 2:
  m = move("down")
 elif nextMove == 3:
  m = move("left")
 else:  # nextMove == 4
  m = move("right")
 if m == -1:
  randomizeState(n)  # not a valid move, don't count it
  print("Move not counted")
 else:
  randomizeState(int(n)-1)
 '''
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
 return'''

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
   return -1
 elif dir == "down":
  if b < 6:  # b can be moved down
   temp = state[b + 3]
   state[b + 3] = state[b]
   state[b] = temp
  else:  # b cannot be moved down
   print("Cannot move down")
   return -1
 elif dir == "left":
  if b != 0 and b != 3 and b != 6:  # b can be moved to the left
   temp = state[b - 1]
   state[b - 1] = state[b]
   state[b] = temp
  else:  # b cannot be moved to the left
   print("Cannot move left")
   return -1
 elif dir == "right":
  if b != 2 and b != 5 and b != 8:  # b can be moved to the right
   temp = state[b + 1]
   state[b + 1] = state[b]
   state[b] = temp
  else:  # b cannot be moved to the right
   print("Cannot move right")
   return -1
 return

def solve_A_star(h):

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

q = PriorityQueue()

q.put((2, 'code'))
q.put((1, 'eat'))
q.put((3, 'sleep'))

while not q.empty():
 next_item = q.get()
 print(next_item)