# Dojo Allocation Application
---
[![Build Status](https://travis-ci.org/Andretalik/adrian-otieno-bc17-week-2.svg?branch=test_full_project)](https://travis-ci.org/Andretalik/adrian-otieno-bc17-week-2.svg?branch=test_full_project)
[![Coverage Status](https://coveralls.io/repos/github/Andretalik/adrian-otieno-bc17-week-2/badge.svg?branch=test_full_project)](https://coveralls.io/github/Andretalik/adrian-otieno-bc17-week-2?branch=test_full_project)
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
