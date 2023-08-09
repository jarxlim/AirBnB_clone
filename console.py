#!/usr/bin/python3
"""cmd class to command line interprete"""
import cmd


class HBNBCommand(cmd.Cmd):
    """cmd class to command line interprete"""
    prompt = '(hbnb) '

    def do_EOF(self):
        """handles end of file"""
        print ("")
        return True
   
    def emptyline(self):
        """don't do anything for emptyline"""
        pass

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()
