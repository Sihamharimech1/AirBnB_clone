#!/usr/bin/python3

"""Console Cmd """

from models import storage
import cmd
from models.base_model import BaseModel
from models.state import State
from models.review import Review
from models.user import User
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.engine.file_storage import FileStorage


class HBNBCommand(cmd.Cmd):

    """The AIRBNB command interpreter."""

    prompt = '(hbnb) '
    classes = {"BaseModel": BaseModel,
               "FileStorage": FileStorage,
               "Amenity": Amenity,
               "City": City,
               "Place": Place,
               "Review": Review,
               "State": State,
               "User": User}

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

    def do_create(self, line):
        """Create instance of a class"""
        if line == "":
            print("** class name missing **")
        else:
            if line in self.classes:
                ins = self.classes[line]()
                ins.save()
                print(ins.id)
            else:
                print("** class doesn't exist **")

    def do_show(self, line):
        """Show all instances"""
        param = line.split()
        taille = len(param)
        if taille == 0:
            print("** class name missing **")
        else:
            if param[0] not in self.classes:
                print("** class doesn't exist **")
            else:
                if taille < 2:
                    print("** instance id missing **")
                else:
                    un_key = param[0] + '.' + param[1]
                    objs = storage.all()
                    if objs.get(un_key) is not None:
                        print(objs[un_key])
                    else:
                        print("** no instance found **")

    def do_destroy(self, line):
        """Delete Instance"""
        param = line.split()
        taille = len(param)
        if taille == 0:
            print("** class name missing **")
        else:
            if param[0] not in self.classes:
                print("** class doesn't exist **")
            else:
                if taille < 2:
                    print("** instance id missing **")
                else:
                    un_key = param[0] + '.' + param[1]
                    objs = storage.all()
                    if objs.get(un_key) is not None:
                        del objs[un_key]
                        storage.save()
                    else:
                        print("** no instance found **")

    def do_all(self, line):
        """Show all instances"""
        param = line.split()
        taille = len(param)
        if taille == 0:
            print("** class name missing **")
        else:
            if param[0] not in self.classes:
                print("** class doesn't exist **")
            else:
                first = '["'
                last = '"]'
                objs = storage.all()
                for key in objs:
                    print(str(first) + str(objs[key]) + str(last))


if __name__ == '__main__':
    HBNBCommand().cmdloop()
