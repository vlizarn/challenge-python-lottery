# Lottery Game
[![stars](https://img.shields.io/github/stars/vlizarn/challenge-python-lottery)](https://github.com/vlizarn/challenge-python-lottery/stargazers)
[![license](https://img.shields.io/github/license/vlizarn/challenge-python-lottery)](https://github.com/vlizarn/challenge-python-lottery/blob/master/LICENSE)
[![version-pre-release](https://img.shields.io/github/v/release/vlizarn/challenge-python-lottery?include_prereleases)](https://github.com/vlizarn/challenge-python-lottery/releases)
[![issues](https://img.shields.io/github/issues/vlizarn/challenge-python-lottery)](https://github.com/vlizarn/challenge-python-lottery/issues)
[![issues-pr](https://img.shields.io/github/issues-pr/vlizarn/challenge-python-lottery)](https://github.com/vlizarn/challenge-python-lottery/pulls)
[![milestones](https://img.shields.io/github/milestones/open/vlizarn/challenge-python-lottery)](https://github.com/vlizarn/challenge-python-lottery/milestones)

The lottery game project consists of creating the lottery game using the object-oriented python programming language that permits users to choose the bet mode, input game mode, and the number of times for every bet. Also, it's possible creating a new bet mode and modify the current ones.

**Several Options**

Bet Modes: `Simple` or `Multiple`.

Input Game Modes: `Auto` or `Manual`.

Amount of Bet: Equal or up to the `1`.

## General Information

### Table of Content

All essential information about the project, you can be found here.

| Project    | Community |
|    :----   |    :----   |
| [Getting Started](#getting-started) | [Code of Conduct](https://github.com/vlizarn/challenge-python-lottery/blob/master/CODE_OF_CONDUCT.md) |
| [Screenshots](#screenshots) | [Contributing](https://github.com/vlizarn/challenge-python-lottery/blob/master/CONTRIBUTING.md)|
| [Technologies](#technologies) | [License](https://github.com/vlizarn/challenge-python-lottery/blob/master/LICENSE) |
| [Features](#features) |[Security Policy](https://github.com/vlizarn/challenge-python-lottery/blob/master/SECURITY.md) |
| [Contributors](#contributor) |[Discussions](https://github.com/vlizarn/challenge-python-lottery/discussions) |

## Getting Started

### Installation

Install it locally on your machine.

#### For Windows, Linux, and macOS

Open the command line or terminal and follow all instructions.

##### 1. Create a project directory.

```
mkdir app
```

##### 2. Set the path of the current directory.

```
cd app
```

##### 3. Clone the repository into a project directory.

```
git clone https://github.com/vlizarn/challenge-python-lottery.git
```

##### 4. Go to the current directory.

```
cd challenge-python-lottery\project
```

##### 5. To run the project using the command line, terminal, or use [IDE](https://www.freecodecamp.org/news/what-is-an-ide-in-programming-an-ide-definition-for-developers).

```
py main.py
```

### Code Sample

This section contains examples of the descriptions of functionalities and constitutions of the application code.

#### Example 1 - Main Description

The current code has three variables, and every variable contains an input method with a message inside it. The first variable is the `title` and permits inserting a `title` name for your new bet mode. The `mode` variable only accepts an insert game input mode that should only include an `Auto` or `Manual` mode. The last variable is `amount` and corresponds to writing the number of bets equal or higher than one and not equal or less than zero to execute the code correctly.

**main.py file**

```python
title = input(self.message.reportDict['request'][1])
mode = input(self.message.reportDict['request'][0])
amount = input(self.message.reportDict['request'][2])

if title == "Simple":
    Program(
        mode, title,
        amount, 5, 2
    ).bet()
elif title == "Multiple":
    Program(
        mode, title,
        amount, 11, 5,
        lRandConjunt=True,
        lRandStar=True
    ).bet()
else:
     self.print('msg', 'lottery', 2)
```

The `title` variable matches the `"Simple"` string. If the `if` statement match is equal, the `Program` constructor with the bet method will be executed inside the `if` statement. The `Program` constructor inside the `if` has five arguments, and the `elif` statement contains seven arguments on the constructor. Every parameter is changeable and permits the reuse of the `Program` constructor to create a new bet mode for the lottery game. For the least, if all top statements don't match the code, the program will return a message with an error explanation.

#### Example 2 - Game Constructor

The `Game` constructor needs arguments for all parameters to perform correctly. In this case, the `Game` constructor is responsible for the data request provided for the `Lottery` constructor. These two constructors have default parameters that mustn't require arguments requested by the user to perform.

**main.py file**

```python

app = Extend

app.Game(
    lmode = "Auto", 
    lTitle = "New Lottery",
    lTimes = 10,
    lTimesConjunt = 7,
    lTimesStar = 4,
    lMaxConjunt = 50,
    lMaxStar = 9,
    lRandConjunt = False,
    lRandStar = False
).bet()

```

The `lTimes` is responsible for the number of bets, `lTimesConjunt` and `lTimesStar` set for the length of every conjunct of elements. The `lMaxConjunt` and `lMaxStar` are the values that start at one to the maximum values for every conjunct. Finally, `lRandConjunt` and `lRandStar` parameters are two boolean data types that match the process of random to `lTimesConjunt` and `lTimesStar` parameters.

#### Example 3 - Code Abridgment

The current code example uses `lmode` and `lTimes` parameters to set arguments such as `Auto` includes the bet mode choices and the value `10` that match the number of bets. Remember to define inside of the while loop the code. When running, the compiler will get the result ten times the bet using the `Auto` game input mode with the default arguments of the constructor.

**main.py file**

```python

app = Extend

app.Game(
    "Auto",
    lTimes = 10
).bet()

```

The current code executed in the compiler will get the length of the random values for the `lTimesConjunt` and not for the `lTimesStar`.

**main.py file**

```python

app = Extend

app.Game(
    lRandConjunt = True,
    lRandStar = False
).bet()

```
Remember, it's essential to remove or reuse the current code of the application.

## Screenshots
| Phase 1    |
|    :----:   |
| [![picture-1](https://github.com/vlizarn/storage-demo/blob/master/projects/challenge-python-lottery/images/python-1.png "picture-1")](#screenshots) | 

## Technologies
* Programming Languages: `Python`.
* Libraries: `os`, `sys` and `random`.

## Features 
* Creation of the `Simple` and `Multiple` bet modes.
* Ability to choose between `Auto` or `Manual` input game mode lottery.
* Player can insert the number of times for every bet.
* The code can be reused to create new bet modes and modify the current ones.

## Contributors
* [ **Ryan Pontes** ](https://github.com/vlizarn)
