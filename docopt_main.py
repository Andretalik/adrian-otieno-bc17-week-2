import sys
import cmd
from docopt import docopt, DocoptExit
from Dojo_class import *

__doc__ = """
This example uses docopt with the built in cmd module to demonstrate an
interactive command application.
Usage:
    dojo create_room <room_type> <room_name>...
    dojo add_person <person_name> <person_type> [<wants_accommodation='N'>]
    dojo print_room <room_name>
    dojo (-i | --interactive)
    dojo (-h | --help)
Options:
    -a, --wants_accommodation  whether the person wants accommodation
    -o, --output  Save to a txt file
    -i, --interactive  Interactive Mode
    -h, --help  Show this screen and exit.
    <room_type>  Type of room - office or living space
    <room_name>  Name of the room
"""
dojo = Dojo()
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


class MyInteractive(cmd.Cmd):

    prompt = 'Dojo Allocation App >>>'
    file = None

    @docopt_cmd
    def do_create_room(self, args):
        """Usage: create_room <room_type> <room_name>..."""
        print(dojo.create_room(args['<room_type>'], args['<room_name>']))


    @docopt_cmd
    def do_add_person(self, args):
        """Usage: add_person <person_name> <person_type> [<wants_accommodation>]"""
        print((args['<person_type>']))
        print(dojo.add_person(args['<person_name>'], args['<person_type>'], args['<wants_accommodation>']))

    @docopt_cmd
    def do_print_room(self, args):
        """Usage: print_room <room_name>"""
        print(dojo.print_room(args['<room_name>']))


    def do_quit(self, args):
        exit()


opt = docopt(__doc__, sys.argv[1:])

if opt['--interactive']:
    MyInteractive().cmdloop()

print(opt)