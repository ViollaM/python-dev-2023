import argparse
import sys
from cowsay import cowsay, list_cows

def draw_cow(args):
    print(cowsay(message=args.message,
                 cow=args.f,
                 preset=None,
                 eyes=args.e,
                 tongue=args.T,
                 width=args.W,
                 wrap_text=args.n))

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
                        prog = 'Cowsay',
                        description = 'Python cowsay')
                        
    parser.add_argument("-e", action="store", type=str, default="oo", metavar="eye_string", help="Select the appearance of the cow's eyes", required=False)
    parser.add_argument("-f", action="store", type=str, default="default", metavar="cowfile", help="Specifies a particular cow picture file to use", required=False)
    parser.add_argument("-n", action="store_true", help="The given message will not be word-wrapped", required=False)
    parser.add_argument("-T", action="store", type=str, default='  ', metavar="tongue_string", help="Select the appearance of the cow's tongue", required=False)
    parser.add_argument("-W", action="store", type=int, default=40, metavar="column", help="Specifies where the message should be wrapped", required=False)

    parser.add_argument("message", action="store", type=str, default='', help="Message for cow to say")

    args = parser.parse_args()
    draw_cow(args)
