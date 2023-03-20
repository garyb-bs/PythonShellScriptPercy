import subprocess
import shlex
import platform


def run_percy_command():
    print(platform.platform())
    if "windows" in platform.platform():
        subprocess.call(shlex.split("./windows.sh token_value test_command"))
    elif "mac" in platform.platform():
        subprocess.call(shlex.split("./linux.sh token_value test_command"))
    elif "linux" in platform.platform():
        subprocess.call(shlex.split("./linux.sh token_value test_command"))
    else:
        raise Exception("No matching OS found, please run file manually")


run_percy_command()
