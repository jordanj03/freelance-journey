import argparse

parser = argparse.ArgumentParser()
# parser.add_argument("square", help="Display a square of a given number.", type=int)
parser.add_argument("--name", '-n', help="Outputs the argument to the CLI")
parser.add_argument("--uppercase", '-uc', help="Converts the name argument to uppercase", action="store_true")
args = parser.parse_args()
# print(args.square**2)
if args.name:
	output = args.name.upper() if args.uppercase else args.name
	print(output)
else:
	parser.print_help()
		