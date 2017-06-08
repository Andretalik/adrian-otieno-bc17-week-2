# Dojo Allocation Application
---
[![Build Status](https://travis-ci.org/Andretalik/adrian-otieno-bc17-week-2.svg?branch=development)](https://travis-ci.org/Andretalik/adrian-otieno-bc17-week-2.svg?branch=development)
[![Coverage Status](https://coveralls.io/repos/github/Andretalik/adrian-otieno-bc17-week-2/badge.svg?branch=development)](https://coveralls.io/github/Andretalik/adrian-otieno-bc17-week-2?branch=development)
[![Code Issues](https://www.quantifiedcode.com/api/v1/project/7bb525c95d53495189c12c300eb2219c/badge.svg)](https://www.quantifiedcode.com/app/project/7bb525c95d53495189c12c300eb2219c)
---
The Dojo Allocation Application is an app designed to ease the maintenance of the system of fellows, staff and the rooms.

## Installation
To run the app, you first need to do some setup.
First off, you need to clone the repository: $ git clone https://github.com/Andretalik/adrian-otieno-bc17-week-2.git

After the clone is complete, create a virtual environment first:

`mkdir "virtual environment name of your choice"`

Install the requirements.txt

`pip install -r requirements.txt`

Now you are ready to use the app. To run it simply run this command in your command-line interface:

`python docopt_main.py -i`

## Using the Application
For some insight as to how to use the program, here are the commands:

```Usage:
    dojo create_room <room_type> <room_name>...
    dojo add_person <person_first_name> <person_second_name> <person_type> [<wants_accommodation='N'>]
    dojo print_room <room_name>
    dojo print_allocations [<txt_file_name>]
    dojo print_unallocated [<txt_file_name>]
    dojo reallocate_person <ID> <room_name>
    dojo mass_add_people <txt_file_name>
    dojo save_to_db [<database_name>]
    dojo load_from_db [<database_name>]
    dojo (-i | --interactive)
    dojo (-h | --help)
Options:
    -a, --wants_accommodation  whether the person wants accommodation
    -o, --output  Save to a txt file
    -i, --interactive  Interactive Mode
    -h, --help  Show this screen and exit.
```

Go wild and use it as you please. Any feedback as to how I can improve my project is welcomed.

A link to a demonstration of the application use is [Dojo App Demo](https://www.youtube.com/watch?v=xNxjXSMgPI4)
