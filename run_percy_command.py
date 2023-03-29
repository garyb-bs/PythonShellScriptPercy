import subprocess
import shlex
import platform

percy_token = "e5a334ccb9d10c2af3d6ea646adaf648c68c13b71c7a6ee344d62774057fd7a3"


def run_percy_command():
    print(platform.platform())
    if "windows" in platform.platform():
        subprocess.call(
            shlex.split("./windows.sh " + percy_token + " python3 test.py uniqueID"))
    elif "mac" in platform.platform():
        subprocess.call(
            shlex.split("./linux.sh " + percy_token + " python3 test.py uniqueID"))
    elif "linux" in platform.platform():
        subprocess.call(
            shlex.split("./linux.sh " + percy_token + " python3 test.py uniqueID"))
    else:
        raise Exception("No matching OS found, please run file manually")


run_percy_command()

