# randomises goals from an input file (default: ./HLD_bingo_goals) and creates a Bingosync Custom Game file (default: ./HLD_bingo_board)
import random
import sys
from urllib.request import urlopen

# set constants until remote goal list importing works
default_paste_url = "https://pastebin.com/raw/WHjRDRiR"
default_input_file = "./HLD_bingo_goals"
default_output_file = "./HLD_bingo_board"
local = True

if len(sys.argv) > 1:
    # parse command line args
    if '-p' in sys.argv:
        local = False

if local:
    try:
        goals = open("./HLD_bingo_goals", "r")
        print("Reading goals from", default_input_file)
    except:
        print("Error: failed to open file:", default_input_file)
        sys.exit()
else:
    try:
        goals = urlopen(default_paste_url)
        print("Reading goals from", default_paste_url)
    except:
        print("Error: failed to open URL:", default_paste_url)
        sys.exit()

board = open("./HLD_bingo_board", "w")
goal_list = []

# goal file format is 1 goal per line, lines starting with a hash are ignored
for goal in goals:
    if not local:
        # strip lines pulled from pastebin
        goal = str(goal)[2:].split('\\')[0]
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

print("Board generated as", default_output_file)

