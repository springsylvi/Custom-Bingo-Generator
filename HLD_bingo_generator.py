# randomises goals from an input file (default: ./HLD_bingo_goals) and creates a Bingosync Custom Game file
# (default: ./HLD_bingo_board)
import random

goals = open("./HLD_bingo_goals", "r")
board = open("./HLD_bingo_board", "w")
goal_list = []

# goal file format is 1 goal per line, lines starting with a hash are ignored
for goal in goals:
    if (goal[0] != '#'):
        goal_list.append(goal.strip())

if (len(goal_list) < 25):
    print("Error: not enough goals (need at least 25)")
    sys.exit()

# randomise goals to use for this game
random_goal_list = random.sample(goal_list, 25)
random.shuffle(random_goal_list)

# write the randomised goals in JSON list format
goal_num = 1 # number of the goal currently being written
board.write("[\n")
for goal in random_goal_list:
    board.write('{"name": "' + goal + '"}')
    if (goal_num < len(random_goal_list)):
        board.write(",\n")
    goal_num += 1
board.write("\n]")
