def copy_file(command: str) -> None:
    if (command and "cp" in command):
        commands = command.split()
        if len(commands) == 3 and commands[1] != commands[2]:
            try:
                with (
                    open(commands[1], "r") as file,
                    open(commands[2], "w") as copy_file
                ):
                    copy_file.write(file.read())
            except FileNotFoundError:
                return None
