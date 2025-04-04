import argparse
import eel
import sys
import os

public = os.path.join(os.path.dirname(__file__), "public")
# Initialize the Eel app
eel.init(public)


def create_parser():
    parser = argparse.ArgumentParser(description="A python app to serve smOllama")
    return parser


def cli():
    "A python app to serve smOllama"
    parser = create_parser()
    args = parser.parse_args()
    mycommand(args)


def mycommand(args):
    eel.start("index.html", size=(800, 600))