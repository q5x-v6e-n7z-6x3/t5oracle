# src/t5oracle/cli.py

import argparse

from .code import generate_code


def main():
    parser = argparse.ArgumentParser(
        prog="t5oracle",
        description="T5 Oracle",
    )

    subparsers = parser.add_subparsers(
        dest="command",
        required=True,
    )

    subparsers.add_parser(
        "code",
        help="Generate a T5 Oracle code",
    )

    args = parser.parse_args()

    if args.command == "code":
        print(generate_code())


if __name__ == "__main__":
    main()