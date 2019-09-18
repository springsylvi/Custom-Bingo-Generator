# Custom-Bingo-Generator

Basic bingo card generator for the Custom (Advanced) option on bingosync.com. Takes a list of goals and generates a list of 25 of them at random. This is primarily for frequently updated goal lists, otherwise use a generator provided by bingosync.

Synopsis:
    python3 bingo_generator.py [-p paste | -i filename] [-o filename]

Options:

    -p paste
        Read goals from the specified pastebin URL, e.g. https://pastebin.com/raw/WHjRDRiR

    -i filename
        Read goals from filename. Either -p or -i must be specified.

    -o filename
        Write board to filename instead of the default "./bingo_board"
