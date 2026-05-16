import requests as r 
import speedtest

VERSION = "0.0.1"
print(f"-- m-shell --")

commands = (
"info>>version -> show shell version",
"info>>help -> show commands"
)


def speed_command():
    speed_test = speedtest.Speedtest()

    print("Finding the best server")
    speed_test.get_best_server()

    download_speed = speed_test.download() / 1000000

    upload_speed = speed_test.upload() / 1000000
    
    print(f"Download speed: {download_speed:.2f} Mbps | Upload speed: {upload_speed:.2f} Mbps")


def rq_command(url: str):
    request = r.get(url=url)
    if request.status_code == 200:
        print(f"{request.status_code} | OK!")
    else:
        print(f"{request.status_code}")

def command_processor():
    command = input("COMMAND -> ")
    if command == "info>>version":
        print(f"--- m-shell | V{VERSION} ---")
    elif command == "info>>help":
        print("commands: ")
        print(commands)
    elif command == "rq>>url":
         url = input("URL(e.g. 'https://url.com'):")
         rq_command(url)
    elif command == "speed>>test":
        speed_command()





command_processor()       