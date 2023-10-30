import argparse as argp
import sys
import os


def inputParseFunc():
    parser = argp.ArgumentParser()
    parser.add_argument('name', type=str)
    args = parser.parse_args()
    return args.name

def printVers():
    print(sys.version)

def makeNewDir(name):
    os.makedirs(name)
    print(f"Made a dir called: {name}")

def getList():
    dirr = os.getcwd()
    parent = os.path.dirname(dirr)
    print(os.listdir(parent))