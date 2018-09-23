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
 state = list(str)
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
  # print("Move not counted")
 else:
  randomizeState(int(n)-1)


def printState():
 "This prints the state"
 print("".join(state))
 return


def move(dir):
 "This moves the blank tile either 'up', 'down', 'left', or 'right'"
 global state
 b = state.index("b")  # b is the location of the blank tile indexed from 0 to 8 along the state string
 if dir == "up":
  if b > 2:  # b can be moved up
   temp = state[b - 3]
   state[b - 3] = state[b]
   state[b] = temp
  else:  # b cannot be moved up
   # print("Cannot move up")
   return -1
 elif dir == "down":
  if b < 6:  # b can be moved down
   temp = state[b + 3]
   state[b + 3] = state[b]
   state[b] = temp
  else:  # b cannot be moved down
   # print("Cannot move down")
   return -1
 elif dir == "left":
  if b != 0 and b != 3 and b != 6:  # b can be moved to the left
   temp = state[b - 1]
   state[b - 1] = state[b]
   state[b] = temp
  else:  # b cannot be moved to the left
   # print("Cannot move left")
   return -1
 elif dir == "right":
  if b != 2 and b != 5 and b != 8:  # b can be moved to the right
   temp = state[b + 1]
   state[b + 1] = state[b]
   state[b] = temp
  else:  # b cannot be moved to the right
   # print("Cannot move right")
   return -1
 return

def solve_A_star(h):
 g = 0

 return

def h1(s):  # s is the state h1 returns the number of misplaced tiles
 count = 0
 for i in s:
  if i != "b":
   if int(i) != s.index(i):
    count += 1
 return count

# check value of the string compared to the index, int("5") == 5
def h2(s):  # s is the state, h2 returns the sum of distances of misplaced tiles
 count = 0
 for i in s:
  if i != "b":
   value = int(i)
   index = s.index(i)
   if (value < 3 and index < 3) or (value > 5 and index > 5) or (value > 2 and value < 6 and index > 2 and index < 6):
    count += abs(((value % 3) - (index % 3)))  # same row but a certain num of columns away
   elif (value < 3 and index > 5) or (value > 5 and index < 3):  # 2 + columns away
    count += 2 + abs(((value % 3) - (index % 3)))
   else:  # 1 + columns away
    count += 1 + abs(((value % 3) - (index % 3)))
 return count

def solve_beam(k):



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
  printState()
 elif cmd_list[0] == "move":
  move(cmd_list[1])
 elif cmd_list[0] == "solve":
  if cmd_list[1] == "A-star":
   solve_A_star(cmd_list[2])
  else:  # beam search
   solve_beam(cmd_list[2])
 elif cmd_list[0] == "maxNodes":
  maxNodes(cmd_list[1])

print('goal state = ' + "".join(goal_state))
print('current state = ' + "".join(state))
print(h1(state))
print(h2(state))


q = PriorityQueue()

q.put((2, 'code'))
q.put((1, 'eat'))
q.put((3, 'sleep'))

while not q.empty():
 next_item = q.get()
 print(next_item)