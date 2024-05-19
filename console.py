#!/usr/bin/python3
import cmd


class HBNBCommand(cmd.Cmd):

    prompt = '(hbnb) '

    # ----- commands -----
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
