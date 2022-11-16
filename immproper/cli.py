import sys
import argparse

parser = argparse.ArgumentParser("immproper")
parser.add_argument("--seq")

def run(args=None):
    if args is None:
        args = sys.argv

    print(args)
    obj = parser.parse_args(args)
    print(obj)

