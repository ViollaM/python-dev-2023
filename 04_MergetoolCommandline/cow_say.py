import cmd
import shlex
from cowsay import cowsay, list_cows, THOUGHT_OPTIONS, make_bubble, cowthink
import readline
import sys

def cow_parameters(arg):
    options = shlex.split(arg)
    message = options[0]
    cow = 'default'
    eyes = 'oo'
    tongue = '  '
    for i in range(1, len(options)):
        if options[i] == "--cow":
            cow = options[i + 1]
        elif options[i] == "--eyes":
            eyes = options[i + 1]
        elif options[i] == "--tongue":
            tongue = options[i + 1]
    return [message, eyes, tongue, cow]

def complete_cow_parameters(text, line, begidx, endidx):
    print(text, line, begidx, endidx)
    current_args = shlex.split(line)
    args_len = len(current_args)
    default_eyes = ["OO", "XX", "==", "^^"]
    default_tongue = ["UU", "U ", " U", "\/"]
    if text == current_args[-1]:
        if args_len == 3:
            return [c for c in list_cows() if c.startswith(text)]
        if args_len == 4:
            return [c for c in default_eyes if c.startswith(text)]
        if args_len == 5:
            return [c for c in default_tongue if c.startswith(text)]
    else:
        if args_len == 2:
            return [c for c in list_cows() if c.startswith(text)]
        if args_len == 3:
            return [c for c in default_eyes if c.startswith(text)]
        if args_len == 4:
            return [c for c in default_tongue if c.startswith(text)]

class CowSayCmd(cmd.Cmd):
    intro = "Welcome to the CowSay cmd."
    prompt = "Let's start >>>> "
    
    def do_list_cows(self, arg):
        """
        list_cows [dir]
        Lists all cow file names in the given directory or default cow list
        """
        print(shlex.split(arg))
        if len(arg) == 0:
            print(list_cows())
        else:
            print(list_cows(shlex.split(arg)[0]))
    
    def do_make_bubble(self, arg):
        """
        make_buble [wrap_text width brackets]
        This is the text that appears above the cows
        """
        options = shlex.split(arg)
        message = options[0]
        brackets = THOUGHT_OPTIONS['cowsay']
        width = 40
        wrap_text = True
        for i in range(1, len(options)):
            if options[i] == "--wrap_text":
                wrap_text = bool(options[i + 1] == "true")
            elif options[i] == "--width":
                width = int(options[i + 1])
            elif options[i] == "--brackets":
                brackets = THOUGHT_OPTIONS[options[i + 1]]
        print(make_bubble(message, brackets=brackets, width=width, wrap_text=wrap_text))
    
    def do_cowsay(self, arg):
        """
        cowsay message [cow eyes tongue]
        Display a message as cow phrases
        """
        message, eyes, tongue, cow = cow_parameters(arg)
        print(cowsay(message, eyes=eyes, tongue=tongue, cow=cow))

    def complete_cowsay(self, text, line, begidx, endidx):
        return complete_cow_parameters(text, line, begidx, endidx)
    
    def do_cowthink(self, arg):
        """
        cowthink message [cow eyes tongue]
        Display a message as cow thought
        """
        message, eyes, tongue, cow = cow_parameters(arg)
        print(cowthink(message, eyes=eyes, tongue=tongue, cow=cow))
    
    def complete_cowthink(self, text, line, begidx, endidx):
        return complete_cow_parameters(text, line, begidx, endidx)
    
    def do_exit(self, arg):
        """
        End of CowSay cmd.
        """
        return True

if __name__ == '__main__':
    CowSayCmd().cmdloop()
