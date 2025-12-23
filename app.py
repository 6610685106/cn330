import argparse
from dotenv import load_dotenv

load_dotenv()

def show_help():
    print("Weather CLI - Help")
    print()
    print("Example command format:")
    print("  python app.py <command>")
    print()
    print("Available commands:")
    print("  help      Show this help message")
    print("  list      List of available weather data")
    print()

def show_list():
    print("Available weather data:")


def create_parser():
    parser = argparse.ArgumentParser(
        description="Weather CLI using OpenWeatherMap API"
    )

    subparsers = parser.add_subparsers(
        dest="command",
        help="Available commands"
    )

    subparsers.add_parser(
        "list",
        help="List of available weather data"
    )

    subparsers.add_parser(
        "help",
        help="Show help information"
    )

    return parser


def main():
    parser = create_parser()
    args = parser.parse_args()

    if args.command == "list":
        show_list()

    elif args.command == "help":
        show_help()

    else:
        print("You successfully opened the Weather CLI app!\n")
        parser.print_help()
    


if __name__ == "__main__":
    main()
