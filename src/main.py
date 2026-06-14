from modules.auxilliary import titulo
from modules.options import options
from modules.todo import todo
from modules.routine import routine

# Main
def main() -> None:
    main_titulo: int = titulo("An CLI App", "What u wanna do?\nCredits to bcsarah@github.com", ["To-Do", "Routine", "Options", "Exit"])
    match main_titulo:
        case 1:
            todo()
        case 2:
            routine()
        case 3:
            options()
        case 4:
            pass

main()