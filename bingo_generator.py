import sys, getopt, random
from urllib.request import urlopen

shortopts = "p:i:o:"
paste = ""
infile = ""
outfile = "bingo_board"

# parse arguments
try:
    options = getopt.getopt(sys.argv[1:], shortopts)[0]
except getopt.GetoptError as optError:
    print("Error:", optError)
    sys.exit()

for option in options:
    if option[0] == "-p":
        local = False
        paste = option[1]
    elif option[0] == "-i":
        local = True
        infile = option[1]
    elif option[0] == "-o":
        outfile = option[1]
if paste == "" and infile == "":
    print("Error: no goal list provided")
    sys.exit()

# open files
if local:
    try:
        goals = open(infile, "r")
        print("Reading goals from", infile)
    except:
        print("Error: failed to open file", infile)
        sys.exit()
else:
    try:
        goals = urlopen(paste)
        print("Reading goals from", paste)
    except:
        print("Error: failed to open URL", paste)
        sys.exit()
try:
    board = open(outfile, "w")
except:
    print("Error: failed to write file", outfile)

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

print("Board generated as", outfile)

