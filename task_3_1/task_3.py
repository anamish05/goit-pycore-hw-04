import sys
from pathlib import Path
from colorama import Fore, Style

def get_directory_tree(path: Path, indent: str = ""):
    try:
        for item in path.iterdir():
            if item.is_dir():
                print(f"{indent}{Fore.YELLOW}{item.name}/")
                get_directory_tree(item, indent+"    ")
            else:
                print(f"{indent}{Fore.BLUE}{item.name}")
    except PermissionError:
        print(f"{indent}{Fore.RED}Access denied: {path}")

def main():
    if len(sys.argv)<2:
        print(f"{Fore.RED}Error in your directory path")
        sys.exit(1)
    directory=Path(sys.argv[1])
    if not directory.exists():
        print(f"{Fore.RED}Error - directory {directory} does not exist")
        sys.exit(1)
    if not directory.is_dir():
        print(f"{Fore.RED}Error - directory is not a directory")
        sys.exit(1)
    print(f"{Fore.CYAN}Directory '{directory}' structure:\n")
    get_directory_tree(directory)
    print(Style.RESET_ALL)

if __name__=="__main__":
    main()
        