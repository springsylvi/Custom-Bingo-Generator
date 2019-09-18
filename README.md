# Custom-Bingo-Generator

Basic bingo card generator for the Custom (Advanced) option on bingosync.com. Takes a list of goals and generates a list of 25 of them at random.

Synopsis:
    python3 bingo_generator.py [-p] [-i filename] [-o filename]

Options:
    -p
        Read goals from pastebin (default: ???) rather than a local file.

    -i filename
        If -p option is not used, read goals from filename instead of the default 
        "./bingo_goals"

    -o filename
        Write board to filename instead of the default "./bingo_board"
