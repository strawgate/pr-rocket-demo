"""Command-line argument parser wrapper."""

import argparse
import sys
from dataclasses import dataclass


@dataclass(frozen=True)
class CLIArgs:
    verbose: bool
    output: str
    input_files: list[str]


def parse_args(argv: list[str] | None = None) -> CLIArgs:
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(description="Process files")
    parser.add_argument("-v", "--verbose", action="store_true")
    parser.add_argument("-o", "--output", default="stdout")
    parser.add_argument("files", nargs="+", help="Input files")
    
    args = parser.parse_args(argv)
    return CLIArgs(verbose=args.verbose, output=args.output, input_files=args.files)


def main():
    args = parse_args()
    if args.verbose:
        print(f"Processing {len(args.input_files)} files...")
    for f in args.input_files:
        print(f"  → {f}")


if __name__ == "__main__":
    main()
