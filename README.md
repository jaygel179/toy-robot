# toy-robot
Toy Robot Code Challenge



Setup
-----

### Installation

You are free to set up locally in your own way (`virtualenv`, `venv`, `pyenv`, `docker`, etc.)

#### Install dependencies

    $ pip install -r requirements.txt

#### Install dev dependencies (test, black, etc.)

    $ pip install -r dev-requirements.txt

#### Running test

    $ pytest

#### Running sample

    $ python main.py



Project Information
-------------------

The application is a simulation of a toy robot moving on a square table top, of dimensions 5 units x 5 units. There are no
other obstructions on the table surface. The robot is free to roam around the surface of the table, but must be prevented
from falling to destruction. Any movement that would result in the robot falling from the table must be prevented,
however further valid movement commands must still be allowed.

### Game commands

#### PLACE

Placing robot to the table specifying the initial coordinates.

    PLACE X,Y,F

example:

    PLACE 0,0,NORTH

Where:

    X - horizontal position of the robot
    Y - vertical position of the robot
    F - facing position of the robot

#### MOVE

Move the robot one unit forward in the direction it is currently facing.

    MOVE

#### LEFT

Rotate the robot -90 degrees without changing the position of the robot.

    LEFT

#### RIGHT

Rotate the robot 90 degrees without changing the position of the robot.

    RIGHT

#### REPORT

Announce the X, Y and F of the robot.

    REPORT



Running Game
------------

The game can run in three different ways.

#### File runner

You need to specify the file location.
The file format should look like.

```
PLACE 0,0,NORTH
MOVE
REPORT
```

```
from main import GameRunner

game_runner = GameRunner()
game_runner.run_file("sample_input.txt")
```

#### String command runner

```
from main import GameRunner

game_runner = GameRunner()
game_runner.run_string_commands([
    "PLACE 0,0,NORTH",
    "MOVE",
    "RIGHT",
    "MOVE",
    "REPORT",
])
```

#### Command runner

```
from main import GameRunner
from commands import (
    MoveCommand,
    PlaceCommand,
    ReportCommand,
    RightCommand,
)

game_runner = GameRunner()
game_runner.run_commands([
    PlaceCommand(1, 1, Faces.SOUTH),
    MoveCommand(),
    RightCommand(),
    MoveCommand(),
    ReportCommand(),
])
```