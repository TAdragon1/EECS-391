import re
import random
from queue import PriorityQueue
from dataclasses import dataclass, field
from typing import Any

class State(object):
 def __init__(self, state):
  self.state = state
  self.prev = ""
  self.prev_move = ""
  return

 def set_prev(self, prev):
  self.prev = prev
  return

 def set_move(self, m):
  self.prev_move = m
  return

 def __repr__(self):
  return "".join(self.state)


@dataclass(order = True)
class PrioritizedItem:
 priority: int
 item: State = field(compare = False)

 def __init__(self, v, s):
  self.priority = v
  self.item = s
  return


# variables
goal_state = list("b12345678")  # goal state
init_state = State(list(""))  # set to empty
max_nodes = 0

# methods
def setState(str):
 "This sets the state using the given input format: 'b12345678'"
 global init_state
 init_state.state = list(str)
 return

def randomizeState(n):
 "This randomizes the state a certain number n of moves away from the goal state"
 if n == 0:  #  base case
  return

 global init_state
 nextMove = random.randint(1, 4)
 if nextMove == 1:
  m = move("up", init_state)
 elif nextMove == 2:
  m = move("down", init_state)
 elif nextMove == 3:
  m = move("left", init_state)
 else:  # nextMove == 4
  m = move("right", init_state)
 if m == "-1":
  randomizeState(n)  # not a valid move, don't count it
  # print("Move not counted")
 else:
  init_state = m  # valid move so change the state
  randomizeState(int(n)-1)


def printState(state):
 "This prints the state"
 print("".join(state.state))
 return


def move(dir, cur_state):  # returns the new state after move
 "This moves the blank tile either 'up', 'down', 'left', or 'right'"
 nextState = State(cur_state.state)
 b = nextState.state.index("b")  # b is the location of the blank tile indexed from 0 to 8 along the state string
 if dir == "up":
  nextState.prev_move = "up"
  if b > 2:  # b can be moved up
   temp = nextState.state[b - 3]
   nextState.state[b - 3] = nextState.state[b]
   nextState.state[b] = temp
  else:  # b cannot be moved up
   return "-1"
 elif dir == "down":
  nextState.prev_move = "down"
  if b < 6:  # b can be moved down
   temp = nextState.state[b + 3]
   nextState.state[b + 3] = nextState.state[b]
   nextState.state[b] = temp
  else:  # b cannot be moved down
   return "-1"
 elif dir == "left":
  nextState.prev_move = "left"
  if b != 0 and b != 3 and b != 6:  # b can be moved to the left
   temp = nextState.state[b - 1]
   nextState.state[b - 1] = nextState.state[b]
   nextState.state[b] = temp
  else:  # b cannot be moved to the left
   return "-1"
 elif dir == "right":
  nextState.prev_move = "right"
  if b != 2 and b != 5 and b != 8:  # b can be moved to the right
   temp = nextState.state[b + 1]
   nextState.state[b + 1] = nextState.state[b]
   nextState.state[b] = temp
  else:  # b cannot be moved to the right
   return "-1"

 nextState.prev = cur_state
 return nextState

def solve_A_star(h):
 g = 0
 num_moves = 0
 solution = []



 return

def h1(s):  # s is the State h1 returns the number of misplaced tiles
 count = 0
 for i in s.state:
  if i != "b":
   if int(i) != s.state.index(i):
    count += 1
 return count

# check value of the string compared to the index, int("5") == 5
def h2(s):  # s is the state, h2 returns the sum of distances of misplaced tiles
 count = 0
 for i in s.state:
  if i != "b":
   value = int(i)
   index = s.state.index(i)
   if (value < 3 and index < 3) or (value > 5 and index > 5) or (value > 2 and value < 6 and index > 2 and index < 6):
    count += abs(((value % 3) - (index % 3)))  # same row but a certain num of columns away
   elif (value < 3 and index > 5) or (value > 5 and index < 3):  # 2 + columns away
    count += 2 + abs(((value % 3) - (index % 3)))
   else:  # 1 + columns away
    count += 1 + abs(((value % 3) - (index % 3)))
 return count

def solve_beam(k):
 successors = PriorityQueue()
 k_best = []
 k_best.append(init_state)

 done = False
 while(not done):
  for i in k_best:  # create successors

   printState(i)

   for l in range(0, 4):
    if l == 0:
     next = move("up", i)
     printState(next)
     printState(next.prev)
     if next.prev.state != next.state:
      successors.put(PrioritizedItem(eval(next), next))
    elif l == 1:
     next = move("down", i)
     printState(next)
     printState(next.prev)
     if next.prev.state != next.state:
      successors.put(PrioritizedItem(eval(next), next))
    elif l == 2:
     next = move("left", i)
     printState(next)
     printState(next.prev)
     if next.prev.state != next.state:
      successors.put(PrioritizedItem(eval(next), next))
    else:
     next = move("right", i)
     printState(next)
     printState(next.prev)
     if next.prev.state != next.state:
      successors.put(PrioritizedItem(eval(next), next))



   while not successors.empty():
    temp = successors.get()
    print(temp.priority)
    print(temp.item)

   done = True



 return

def eval(s):  # my evaluation funciton for beamsort, h2 is always >= to h1 so this result is always positive
 return h2(s) - h1(s)

def maxNodes(n):
 "This sets the number of maximum nodes during a search"
 global max_nodes
 max_nodes = n
 return

# program
f = open("test.txt", 'r', encoding = 'utf-8')
commands = []
for line in f:
 commands.append(re.split('\n', line)[0])

for cmd in commands:
 cmd_list = cmd.split()
 if cmd_list[0] == 'setState':
  setState(list(cmd_list[1]))
 elif cmd_list[0] == "randomizeState":
  randomizeState(cmd_list[1])
 elif cmd_list[0] == "printState":
  printState(init_state)
 elif cmd_list[0] == "move":
  if move(cmd_list[1], init_state) != "-1":  # if it is a valid move
   next_state = move(cmd_list[1])
 elif cmd_list[0] == "solve":
  if cmd_list[1] == "A-star":
   solve_A_star(cmd_list[2])
  else:  # beam search
   solve_beam(int(cmd_list[2]))
 elif cmd_list[0] == "maxNodes":
  maxNodes(cmd_list[1])

print('goal state = ' + "".join(goal_state))
print('current state = ' + "".join(init_state.state))
print(h1(init_state))
print(h2(init_state))
print(eval(init_state))


q = PriorityQueue()


q.put((2, 'code'))
q.put((1, 'eat'))
q.put((3, 'sleep'))

while not q.empty():
 next_item = q.get()
 print(next_item)