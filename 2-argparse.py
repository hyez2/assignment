import argparse
import logging


def create_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Process some integers.")
    parser.add_argument('--start', type=int, required=True, help='Start value')
    parser.add_argument('--end', type=int, required=True, help='End value')
    parser.add_argument('--verbose', action='store_true', help='Enable verbose output')
    return parser


if __name__ == "__main__":
    parser = create_parser()
    args = parser.parse_args()

    start: int = args.start
    end: int = args.end
    verbose: bool = args.verbose

    print(start, end, verbose)

