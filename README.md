
# 7407-DriveCode-22-23

Team 7407 Wired Boars 2022-2023 Robot Code



## Getting Started:

### If you don't have Poetry installed already:

#### Linux and Mac

```

curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -

```

#### Windows Powershell

```

(Invoke-WebRequest -Uri https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py -UseBasicParsing).Content | python -

```

Further information can be found here: https://python-poetry.org/docs/



Make sure to add Poetry to your path.



### With Poetry Installed:

```

poetry shell

poetry install

```



## Best Practices

### Pre-Commit, Formatting

Make sure to run ```pre-commit install``` before your first commit. When you commit, pre-commit will automatically check all files you have staged using Flake8, Black, ISort, and other formatters.

- If the response contains an ERROR:

	- If the error response contains "Files were modified by this hook":
		- ``git add .``
		- ``git commit -m "Message"``
	- Otherwise, manually fix the issues outlined, re-stage your files ( ``git add.``) and recommit.

Do not forget to ``git add .`` before committing.

### Commenting
Comment, comment, comment!
 - Use block quotes to start any function with parameters, and every class's "\_\_init\_\_" function. Block quotes should contain:
	 - Summary
	 - Arguments, with types and descriptions
	 - Return description
	 There are many extensions to help with docstrings. Examples include:
		 - autoDocstring on VsCode
		 - On PyCharm
			 - Place your cursor over a function or class name.
			 - Alt-Enter
			 - Generate documentation string stub
 - Use single line comments for any function without parameters with a description of the function.
 - Use single line comments before any complex function to describe how it works, and to the right of any line or variable that is very complicated.
 - Use TODO comments freely.

### Branching
To branch, first make sure that all your local changes are committed. If you would like to abandon the changes, run ``git reset --hard``. Be very careful with resetting.
To branch: ``git branch {branch name}

Branch names are as follows:
 - Subsystem Initialization branch format: init/{subsystem}
	 - Example: init/shooter
	 - Example: init/drivetrain
 - Feature branch format: feat/{subsystems}/{feature}
	 - Example: feat/shooter/optimized_shooting
	 - Example: feat/intake-index/ejection
 - Fix branch format: fix/{subsystems}/issue
	 - Example: fix/camera_server/wrong_ports
	 - Example: fix/robot/network_loop_time
	 - Example: fix/sensors/clean_up
 - Competition branch format: comp/{competition}/day/{day}
	 - Example: comp/battlecry/day/0 (load_in, initial setup, configurations)
	 - Example: comp/hartford/day/1

### Pull Requests
To integrate a branch with branch **Main**,  create a pull-request with the same title as your branch. Make sure pre-commits pass before pushing to ensure clean code.

### Competition Exceptions
#### Pre-commits
 - To avoid frustration, please use ``git commit -m "{Message}" --no-verify``
### Debugging:
#### Logger
 - USE LOGGER! It makes it easier on everyone to debug.

## Resources
 - [RobotPy Documentation](https://robotpy.readthedocs.io/en/stable/) We love RobotPy!
 - [WPILib Documentation](https://docs.wpilib.org/en/stable/index.html) RobotPy is just a wrapper for the WPILib C++ Code. Most of the structure remains the same.
 - [Chief Delphi](https://www.chiefdelphi.com/) Many a sensor problem have been fixed by looking here.
 - [7407 DriveCode-2021-Python](https://github.com/Choate-Robotics/7407-DriveCode-2021-Python) Worlds level code!