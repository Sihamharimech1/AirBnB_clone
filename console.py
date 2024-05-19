#!/usr/bin/python3
"""Console Cmd """

import cmd


class HBNBCommand(cmd.Cmd):

    """The AIRBNB command interpreter."""

    prompt = '(hbnb) '

    def do_EOF(self, line):
        """Exits"""
        return True

    def do_quit(self, line):
        """Quit command to exit the program
        """
        return True

    def emptyline(self):
        """Doesn't execute anything"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
