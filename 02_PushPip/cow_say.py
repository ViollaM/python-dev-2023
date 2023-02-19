import argparse
import sys
from cowsay import cowsay, list_cows

def draw_cow(args):
    if args.l:
        print("Found cow files: ", list_cows())
    else:
        if len(args.message) == 0:
            message = []
            for line in sys.stdin:
                message.append(line.strip())
            args.message = "\n".join(message)

        mode = None
        if args.modes is not None:
            mode = ''.join(args.modes)

        print(cowsay(message=args.message,
                     cow=args.f,
                     preset=mode,
                     eyes=args.e[:2],
                     tongue=args.T[:2],
                     width=args.W,
                     wrap_text=args.n,
                     cowfile=args.f if "/" in args.f else None))

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
                        prog = 'Cowsay',
                        description = 'Python cowsay')
                        
    parser.add_argument("-e", action="store", type=str, default="oo", metavar="eye_string", help="Select the appearance of the cow's eyes", required=False)
    parser.add_argument("-f", action="store", type=str, default="default", metavar="cowfile", help="Specifies a particular cow picture file to use", required=False)
    parser.add_argument("-n", action="store_true", help="The given message will not be word-wrapped", required=False)
    parser.add_argument("-T", action="store", type=str, default="  ", metavar="tongue_string", help="Select the appearance of the cow's tongue", required=False)
    parser.add_argument("-W", action="store", type=int, default=40, metavar="column", help="Specifies where the message should be wrapped", required=False)

    parser.add_argument("message", action="store", type=str, default="", nargs="?", help="Message for cow to say")

    parser.add_argument("-l", action="store_true", help="List of cowfiles", required=False)

    cow_modes = {"b": "borg",
                 "d": "dead",
                 "g": "greedy",
                 "p": "paranoia",
                 "s": "stoned",
                 "t": "tired",
                 "w": "wired",
                 "y": "youthful"}

    for mode, desc in cow_modes.items():
        parser.add_argument(f"-{mode}", action="append_const", const=mode, dest = "modes", help="mode: " + desc)

    args = parser.parse_args()
    draw_cow(args)
