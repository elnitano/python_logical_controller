# Python Logical Controller (PLC)
First personal project for Boot.dev lessons.

A bit atypical project, as my daily work is in industrial automation, working with _Programmable Logical Controller_ <sup>(PLC)</sup>

The idea is to take the foundation of how a typical Logic Controller is programmed, and turn it into a Python code.

To make this truely expandable, the program should be mostly done with OOP, like you would do in the real life, making instances of programming blocks.

## Showcase
The project was easier than first projected, maybe its not the cleanest code - but it actually does the job relatively good.

[![Watch the showcase](/factory/overview.png)](https://i.gyazo.com/03a1e2a698c713d6c5aaf54e81a74924.mp4)

## Whats required for this project
This won't be something I'd expect a regular user can setup and play around with.

We will be utilizing [FactoryIO](https://factoryio.com) as simulation tool. <sup>*NOTE* This software has license requirement</sup>

And then we will use [pyModbusTCP](https://pypi.org/project/pyModbusTCP/) as communication protocol between the Python code, and the simulation tool.

## So what is the goal of the project?
Goal would be to have a small logistic simulation, sorting 3 types of boxes into categories.

Once the baseline has been established, this can be extended into a larger fully fletched logistics system, implementing various machines in the process.

### Currently working on:
 - [x] Create the scenario in FactoryIO for our sorting line.
 - [x] Make sure the Python program can work with FactoryIO (Establish connection via pyModbusTCP)
 - [x] Create software to Read Inputs and Write Outputs - Should be (Read IO -> Execute Software -> Write IO).
 - [x] Create Groupstart software, to handle Start/Stop of the Plant.
 - [x] Create Conveyor software, this should inherit Groupstart, and handle the controls of Conveyors, with sensors ect.
 - [x] Create Sweeper software, this should inherit Groupstart, and handle the sweeper for boxes, with motor ect.
 - [x] Create Tracking software, this should track our product, assigning the sweeper output needed.
 - [x] Create Scale software, this should stop the conveyor, read the scale once stable, determine box type, add it to tracking software.