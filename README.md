# BlackBox Puzzle 31


## The puzzle
[James Lyndsay](https://twitter.com/workroomprds) has created a number of
[BlackBox Puzzles](http://blackboxpuzzles.workroomprds.com/). Puzzle 31 is one of the puzzles with both a [GUI]((http://blackboxpuzzles.workroomprds.com/puzzle31/)) and an
[API](http://blackboxpuzzles.workroomprds.com:8002/puzzle31).


## The plan
When exploring a BlackBox Puzzle through the GUI, you start from the input, observe the output, and try to find a
pattern. Based on that pattern you form one or more hypotheses, which feedback into your exploration.

Using the API, however, allows you to get the output for all possible combinations of inputs (there are 512 for puzzle
31). Or rather, it allows you to do so more easily than through the GUI. Once you have that dataset, you can explore
it starting from the output, from a range of inputs, etc.

**Disclaimer**: I knew the simple principle this puzzle adheres to before looking into this API/data analysis approach.


## This repo

### Contents
- `get_it_all.py`: get the output for all possible input combinations and write it to the csv file `puzzle31.csv`
- `puzzle31.csv`: all input combinations and their output

### Setup
- Install Python 3
- Create a virtual environment: `python -m venv venv` or `python3 -m venv venv`
- Activate the virtual environment: (linux/mac) `source ./venv/bin/activate` or (win) `venv\Scripts\activate`
- Install dependencies: `pip install -r requirements.txt`
