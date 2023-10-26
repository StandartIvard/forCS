import argparse as argp
import sys
import os


parser = argp.ArgumentParser()
parser.add_argument('name', type=str)
args = parser.parse_args()

print(sys.version)

os.makedirs(args.name)

dirr = os.getcwd()
parent = os.path.dirname(dirr)
print(os.listdir(parent))
