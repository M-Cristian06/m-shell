import requests as r 

VERSION = "0.0.1"
print(f"-- m-shell --")

commands = (
"info>>version -> show shell version",
"info>>help -> show commands"
)


def rq_command(url: str):
    request = r.get(url=url)
    print(request.status_code)


def command_processor():
    command = input("COMMAND -> ")
    if command == "info>>version":
        print(f"--- m-shell | V{VERSION} ---")
    elif command == "info>>help":
        print("commands: ")
        print(commands)
    elif command == f"rq>>":
         pass 



command_processor()       