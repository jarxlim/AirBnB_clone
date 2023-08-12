#!/usr/bin/env python3
import cmd
import re
from shlex import split
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


def parsing(input_str):
    curly_bracket_match = re.search(r"\{(.*?)\}", input_str)
    square_bracket_match = re.search(r"\[(.*?)\]", input_str)

    if curly_bracket_match is None:
        if square_bracket_match is None:
            segments = [segment.strip(",") for segment in input_str.split()]
        else:
            left_segments = input_str[:square_bracket_match.span()[0]].split()
            right_segments = [segment.strip(",") for segment in left_segments]
            right_segments.append(square_bracket_match.group())
            segments = right_segments
    else:
        left_segments = input_str[:curly_bracket_match.span()[0]].split()
        right_segments = [segment.strip(",") for segment in left_segments]
        right_segments.append(curly_bracket_match.group())
        segments = right_segments

    return segments


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "
    __classes = {
        "BaseModel",
        "User",
        "State",
        "City",
        "Place",
        "Amenity",
        "Review"
    }

    def default(self, input_arg):
        """Default behavior for cmd module when input is invalid"""
        command_dict = {
            "all": self.do_all,
            "show": self.do_show,
            "destroy": self.do_destroy,
            "count": self.do_count,
            "update": self.do_update
        }
        dot_match = re.search(r"\.", input_arg)
        if dot_match is not None:
            input_arg_list =
            [
                input_arg[:dot_match.span()[0]],
                input_arg[dot_match.span()[1]:]
            ]
            parentheses_match = re.search(r"\((.*?)\)", input_arg_list[1])
            if parentheses_match is not None:
                command_parts =
                [
                    input_arg_list[1][:parentheses_match.span()[0]],
                    parentheses_match.group()[1:-1]
                ]
                if command_parts[0] in command_dict.keys():
                    part1 = input_arg_list[0]
                    full_call = "{} {}".format(part1, command_parts[1])
                    return command_dict[command_parts[0]](full_call)
        print("*** Unknown syntax: {}".format(input_arg))
        return False

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """Exit the program on EOF (Ctrl-D)"""
        print("")
        return True

    def emptyline(self):
        """Do nothing on empty line"""
        pass

    def do_create(self, arg):
        """Create a new instance of BaseModel, save it, and print the id"""
        args = parsing(arg)
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return
        else:
            print(eval(class_name)().id)
            new_instance.save()

    def do_show(self, arg):
        """Prints the string representation of an instance"""
        args = parsing(arg)
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        instances = storage.all()
        instance_id = args[1]
        key = "{}.{}".format(class_name, instance_id)
        if key in instances:
            print(instances[key])
        else:
            print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        args = parsing(arg)
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        instances = storage.all()
        instance_id = args[1]
        key = "{}.{}".format(class_name, instance_id)
        if key in instances:
            del instances[key]
            storage.save()
        else:
            print("** no instance found **")

    def do_count(self, arg):
        """Usage: count <class> or <class>.count()
        Retrieve the number of instances of a given class."""
        argl = parsing(arg)
        count = 0
        for obj in storage.all().values():
            if argl[0] == obj.__class__.__name__:
                count += 1
        print(count)

    def do_all(self, arg):
        """Prints all string representation of all instances"""
        args = parsing(arg)
        if args and args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return
        else:
            objl = []
            for obj in storage.all().values():
                if len(args) > 0 and args[0] == obj.__class__.__name__:
                    objl.append(obj.__str__())
                elif len(args) == 0:
                    objl.append(obj.__str__())
            print(objl)

    def do_update(self, arg):
        """Updates an instance based on the class name and id"""
        args = parsing(arg)
        if not args:
            print("** class name missing **")
            return False
        class_name = args[0]
        if class_name not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return False
        if len(args) < 2:
            print("** instance id missing **")
            return False
        instances = storage.all()
        instance_id = args[1]
        key = "{}.{}".format(class_name, instance_id)
        if key not in instances:
            print("** no instance found **")
            return False
        if len(args) < 3:
            print("** attribute name missing **")
            return False
        if len(args) < 4:
            try:
                type(eval(args[2])) != dict
            except NameError:
                print("** value missing **")
                return False

        if len(args) == 4:
            obj = instances["{}.{}".format(args[0], args[1])]
            if args[2] in obj.__class__.__dict__.keys():
                valtype = type(obj.__class__.__dict__[args[2]])
                obj.__dict__[args[2]] = valtype(args[3])
            else:
                obj.__dict__[args[2]] = args[3]
        elif type(eval(args[2])) == dict:
            obj = instances["{}.{}".format(args[0], args[1])]
            for k, v in eval(args[2]).items():
                if (k in obj.__class__.__dict__.keys() and
                        type(obj.__class__.__dict__[k]) in {str, int, float}):
                    valtype = type(obj.__class__.__dict__[k])
                    obj.__dict__[k] = valtype(v)
                else:
                    obj.__dict__[k] = v
        storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
