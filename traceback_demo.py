import os

from rich.console import Console


def bad_function():
    x = 42
    y = "hello"
    return 1 / 0


def main():
    console = Console()

    console.print("[bold green]--- Traceback WITH borders (default) ---[/]\n")
    try:
        bad_function()
    except:
        console.print_exception(show_locals=True)

    console.print()

    console.print("[bold cyan]--- Traceback WITHOUT borders ---[/]\n")
    try:
        bad_function()
    except:
        console.print_exception(show_locals=True, show_border=False)

    input("\nPress Enter to exit...")


if __name__ == "__main__":
    main()

