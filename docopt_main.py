__doc__ = """
This project uses docopt with the built in cmd module to be used as an
interactive command application.
Usage:
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
"""
import sys
import cmd
from termcolor import cprint
from pyfiglet import figlet_format
from docopt import docopt, DocoptExit
from dojo_class import Dojo


def docopt_cmd(func):
    """
    This decorator is used to simplify the try/except block and pass the result
    of the docopt parsing to the called action.
    """

    def fn(self, arg):
        try:
            opt = docopt(fn.__doc__, arg)

        except DocoptExit as e:
            # The DocoptExit is thrown when the args do not match.
            # We print a message to the user and the usage block.

            print('Invalid Command!')
            print(e)
            return

        except SystemExit:
            # The SystemExit exception prints the usage for --help
            # We do not need to do the print here.

            return

        return func(self, opt)

    fn.__name__ = func.__name__
    fn.__doc__ = func.__doc__
    fn.__dict__.update(func.__dict__)
    return fn


def intro():
    cprint(figlet_format('Dojo Allocation Application', font='slant'),
           'yellow', attrs=['bold'])
    print("Welcome to the Dojo Allocation Application! Here is a list of commands to get you started." +
          " Type 'help' anytime to access available commands")
    cprint(__doc__, 'green')


def leaving():
    cprint(figlet_format('Later!', font='slant'), 'red', attrs=['bold'])


class MyInteractive(cmd.Cmd):

    intro()
    dojo = Dojo()
    prompt = 'dojo >>>'
    file = None

    @docopt_cmd
    def do_create_room(self, args):
        """Usage: create_room <room_type> <room_name>..."""
        self.dojo.create_room(args['<room_type>'], args['<room_name>'])

    @docopt_cmd
    def do_add_person(self, args):
        """Usage: add_person <person_first_name> <person_second_name> <person_type> [<wants_accommodation>]"""
        self.dojo.add_person(args['<person_first_name>'].title(), args['<person_second_name>'].title(), args['<person_type>'].lower(), args['<wants_accommodation>'])

    @docopt_cmd
    def do_print_room(self, args):
        """Usage: print_room <room_name>"""
        self.dojo.print_room(args['<room_name>'])

    @docopt_cmd
    def do_print_allocations(self, args):
        """Usage: print_allocations [<txt_file_name>]"""
        self.dojo.print_allocations(args['<txt_file_name>'])

    @docopt_cmd
    def do_print_unallocated(self, args):
        """Usage: print_unallocations [<txt_file_name>]"""
        self.dojo.print_unallocated(args['<txt_file_name>'])

    @docopt_cmd
    def do_reallocate_person(self, args):
        """Usage: reallocate_person <ID> <room_name>"""
        self.dojo.reallocate_person(args['<ID>'], args['<room_name>'])

    @docopt_cmd
    def do_mass_add_people(self, args):
        """Usage: mass_add_people <file_name>"""
        self.dojo.mass_add_people(args['<file_name>'])

    @docopt_cmd
    def do_save_to_db(self, args):
        """Usage: save_to_db [<database_name>]"""
        self.dojo.save_to_db(args['<database_name>'])

    @docopt_cmd
    def do_load_from_db(self, args):
        """Usage: load_from_db [<database_name>]"""
        self.dojo.load_from_db(args['<database_name>'])

    def do_quit(self, args):
        leaving()
        exit()


opt = docopt(__doc__, sys.argv[1:])

if opt['--interactive']:
    MyInteractive().cmdloop()

print(opt)
