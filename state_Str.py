import re
import random
from queue import PriorityQueue
import sys
import time


# variables
goal_state = list("b12345678")  # goal state
state = list("")  # set to empty
random.seed(8)
max_nodes = None


# comment this out to use ide's run command

file_name = sys.argv[1]



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
        m = move("up", state)
    elif nextMove == 2:
        m = move("down", state)
    elif nextMove == 3:
        m = move("left", state)
    else:  # nextMove == 4
        m = move("right", state)
    if m == -1:
        return randomizeState(n)  # not a valid move, don't count it
        # print("Move not counted")
    else:
        state = m
        return randomizeState(n-1)


def printState():
    "This prints the state"
    print("".join(state))
    return

def copy(str_list):
    r = []
    for i in str_list:
        r.append(i)
    return r

def move(dir, input):
    "This moves the blank tile either 'up', 'down', 'left', or 'right'"
    s = copy(input)
    test_state = "".join(input)
    b = s.index("b")  # b is the location of the blank tile indexed from 0 to 8 along the state string
    if dir == "up":
        if b > 2:  # b can be moved up
            temp = s[b - 3]
            s[b - 3] = s[b]
            s[b] = temp
        else:  # b cannot be moved up
            # print("Cannot move up")
            return -1
    elif dir == "down":
        if b < 6:  # b can be moved down
            temp = s[b + 3]
            s[b + 3] = s[b]
            s[b] = temp
        else:  # b cannot be moved down
            # print("Cannot move down")
            return -1
    elif dir == "left":
        if b != 0 and b != 3 and b != 6:  # b can be moved to the left
            temp = s[b - 1]
            s[b - 1] = s[b]
            s[b] = temp
        else:  # b cannot be moved to the left
            # print("Cannot move left")
            return -1
    elif dir == "right":
        if b != 2 and b != 5 and b != 8:  # b can be moved to the right
            temp = s[b + 1]
            s[b + 1] = s[b]
            s[b] = temp
        else:  # b cannot be moved to the right
            # print("Cannot move right")
            return -1
    if "".join(s) != test_state:  # extra catch
        '''print()
        print(input)
        print(s)
        print()'''
        return s
    else:
        return -1

def solve_A_star(h):
    '''
    print('goal state = ' + "".join(goal_state))
    print('current state = ' + "".join(state))
    '''
    prev_states = {
        "".join(state): None
    }
    # formatted as state: prev move
    prev_moves = {
        "".join(state): None
    }

    total_moves = {
        "".join(state): 0
    }

    queue = PriorityQueue()
    queue.put((heval(h, state), state))
    prev_states["".join(state)] = None
    prev_moves["".join(state)] = None
    total_moves["".join(state)] = 0

    # print(total_moves)
    done = False
    start_time = time.perf_counter()
    while not done:

        # a node's value in the p_queue is num_moves + heuristic

        item = queue.get()
        curr = item[1]
        for l in range(0, 4):
            if l == 0:
                next_state = move("up", curr)
                if next_state != -1:
                    if prev_states.get("".join(next_state)) is None:
                        value = heval(h, next_state) + total_moves["".join(curr)] + 1
                        queue.put((value, next_state))
                        prev_states["".join(next_state)] = "".join(curr)
                        prev_moves["".join(next_state)] = "up"
                        total_moves["".join(next_state)] = total_moves["".join(curr)] + 1
                    elif total_moves["".join(next_state)] > total_moves["".join(curr)]:
                        # total_moves of prev plus one is base
                        # if the moves at the already existing next_state are less that the base
                        # don't replace the existing values
                        # if the moves at the already existing next_state are larger than the base
                        # replace them
                        value = heval(h, next_state) + total_moves["".join(curr)] + 1
                        queue.put((value, next_state))
                        prev_states["".join(next_state)] = "".join(curr)
                        prev_moves["".join(next_state)] = "up"
                        total_moves["".join(next_state)] = total_moves["".join(curr)] + 1

            elif l == 1:
                next_state = move("down", curr)
                if next_state != -1:
                    if prev_states.get("".join(next_state)) is None or total_moves["".join(next_state)] > total_moves["".join(curr)]:
                        value = heval(h, next_state) + total_moves["".join(curr)] + 1
                        queue.put((value, next_state))
                        prev_states["".join(next_state)] = "".join(curr)
                        prev_moves["".join(next_state)] = "down"
                        total_moves["".join(next_state)] = total_moves["".join(curr)] + 1

            elif l == 2:
                next_state = move("left", curr)
                if next_state != -1:
                    if prev_states.get("".join(next_state)) is None or total_moves["".join(next_state)] > \
                            total_moves["".join(curr)]:
                        value = heval(h, next_state) + total_moves["".join(curr)] + 1
                        queue.put((value, next_state))
                        prev_states["".join(next_state)] = "".join(curr)
                        prev_moves["".join(next_state)] = "left"
                        total_moves["".join(next_state)] = total_moves["".join(curr)] + 1

            else:
                next_state = move("right", curr)
                if next_state != -1:
                    if prev_states.get("".join(next_state)) is None or total_moves["".join(next_state)] > \
                            total_moves["".join(curr)]:
                        value = heval(h, next_state) + total_moves["".join(curr)] + 1
                        queue.put((value, next_state))
                        prev_states["".join(next_state)] = "".join(curr)
                        prev_moves["".join(next_state)] = "right"
                        total_moves["".join(next_state)] = total_moves["".join(curr)] + 1
        '''
        print(total_moves)
        print(prev_states)
        print(prev_moves)
        '''
        c = queue.get()
        # print(c)
        end_time = time.perf_counter()
        if c[1] == goal_state:
            str = "".join(c[1])
            done = True
            print("Total number of moves: ")
            print(total_moves[str])
            moveList = []
            prev_states["".join(state)] = None
            prev_moves["".join(state)] = None
            total_moves["".join(state)] = 0
            while prev_states[str] is not None:
                moveList.append(prev_moves[str])
                str = prev_states[str]
            moveList.reverse()
            out = ", ".join(moveList)
            print("Moves taken to reach the solution: ")
            print(out)
            print("Number of nodes: ")
            print(queue.qsize()+1)
            print((end_time - start_time), "seconds")
        else:
            queue.put((c[0], c[1]))

        if max_nodes <= queue.qsize():
            print("Reached max nodes")
            print((end_time - start_time), "seconds")
            done = True
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

def heval(h, s):
    if h == "h1":
        return h1(s)
    else:
        return h2(s)

def solve_beam(k):
    global state
    '''
    print('goal state = ' + "".join(goal_state))
    print('current state = ' + "".join(state))
    '''
    # dictionary formatted as state: prev state
    prev_states = {
        "".join(state): None
    }
    # formatted as state: prev move
    prev_moves = {
        "".join(state): None
    }

    total_moves = {
        "".join(state): 0
    }

    k_best = [None] * int(k)
    k_best[0] = "".join(state)
    successors = PriorityQueue()
    done = False
    start_time = time.perf_counter()
    while not done:

        for i in k_best:

            if i is not None:
                for l in range(0, 4):
                    if l == 0:
                        next_state = move("up", list(i))
                        if next_state != -1:
                            if prev_states.get("".join(next_state)) is None:  # new state
                                successors.put((eval(next_state), next_state))
                                prev_states["".join(next_state)] = i
                                prev_moves["".join(next_state)] = "up"
                                total_moves["".join(next_state)] = total_moves[i] + 1
                            else:  # if less moves to get to this state, update parent, move, and count
                                if total_moves[i] + 1 < total_moves["".join(next_state)]:
                                    successors.put((eval(next_state), next_state))
                                    prev_states["".join(next_state)] = i
                                    prev_moves["".join(next_state)] = "up"
                                    total_moves["".join(next_state)] = total_moves[i] + 1

                    elif l == 1:
                        next_state = move("down", list(i))
                        if next_state != -1:
                            if prev_states.get("".join(next_state)) is None:  # new state
                                successors.put((eval(next_state), next_state))
                                prev_states["".join(next_state)] = i
                                prev_moves["".join(next_state)] = "down"
                                total_moves["".join(next_state)] = total_moves[i] + 1
                            else:  # if less moves to get to this state, update parent, move, and count
                                if total_moves[i] + 1 < total_moves["".join(next_state)]:
                                    successors.put((eval(next_state), next_state))
                                    prev_states["".join(next_state)] = i
                                    prev_moves["".join(next_state)] = "down"
                                    total_moves["".join(next_state)] = total_moves[i] + 1
                    elif l == 2:
                        next_state = move("left", list(i))
                        if next_state != -1:
                            if prev_states.get("".join(next_state)) is None:  # new state
                                successors.put((eval(next_state), next_state))
                                prev_states["".join(next_state)] = i
                                prev_moves["".join(next_state)] = "left"
                                total_moves["".join(next_state)] = total_moves[i] + 1
                            else:  # if less moves to get to this state, update parent, move, and count
                                if total_moves[i] + 1 < total_moves["".join(next_state)]:
                                    successors.put((eval(next_state), next_state))
                                    prev_states["".join(next_state)] = i
                                    prev_moves["".join(next_state)] = "left"
                                    total_moves["".join(next_state)] = total_moves[i] + 1
                    else:
                        next_state = move("right", list(i))
                        if next_state != -1:
                            if prev_states.get("".join(next_state)) is None:  # new state
                                successors.put((eval(next_state), next_state))
                                prev_states["".join(next_state)] = i
                                prev_moves["".join(next_state)] = "right"
                                total_moves["".join(next_state)] = total_moves[i] + 1
                            else:  # if less moves to get to this state, update parent, move, and count
                                if total_moves[i] + 1 < total_moves["".join(next_state)]:
                                    successors.put((eval(next_state), next_state))
                                    prev_states["".join(next_state)] = i
                                    prev_moves["".join(next_state)] = "right"
                                    total_moves["".join(next_state)] = total_moves[i] + 1

        for m in range(0, len(k_best)):
            if not successors.empty():
                temp = successors.get()
                k_best[m] = "".join(temp[1])

        end_time = time.perf_counter()
        if "".join(goal_state) in k_best:
            done = True
            print("Total moves to reach the solution: ")
            print(total_moves["".join(goal_state)])
            temp = "".join(goal_state)
            moveList = []
            prev_states["".join(state)] = None
            prev_moves["".join(state)] = None
            total_moves["".join(state)] = 0
            while prev_states[temp] is not None:
                moveList.append(prev_moves[temp])
                temp = prev_states[temp]
            moveList.reverse()
            out = ", ".join(moveList)
            print("Moves taken to reach the solution: ")
            print(out)
            print((end_time - start_time), "seconds")

    return

def eval(s):  # my evaluation funciton for beamsort, h2 is always >= to h1 so this result is always positive
    return h2(s) + h1(s)

def maxNodes(n):
    "This sets the number of maximum nodes during a search"
    global max_nodes
    max_nodes = int(n)
    return

# program
# file_name = "testCorrect.txt"  # comment this line out to use command line input
f = open(file_name, 'r', encoding = 'utf-8')
commands = []
for line in f:
    commands.append(re.split('\n', line)[0])

for cmd in commands:
    cmd_list = cmd.split()
    if cmd_list[0] == 'setState':
        setState(list(cmd_list[1]))
    elif cmd_list[0] == "randomizeState":
        randomizeState(int(cmd_list[1]))
    elif cmd_list[0] == "printState":
        printState()
    elif cmd_list[0] == "move":
        state = move(cmd_list[1], state)
    elif cmd_list[0] == "solve":
        if cmd_list[1] == "A-star":
            solve_A_star(cmd_list[2])
        else:  # beam search
            solve_beam(cmd_list[2])
    elif cmd_list[0] == "maxNodes":
        maxNodes(cmd_list[1])