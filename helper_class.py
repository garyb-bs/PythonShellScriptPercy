import subprocess
import shlex


class Utilities:

    @staticmethod
    def run_through_percy(percy_token, filename, functionname, uniqueid):
        subprocess.call(shlex.split("scripts/linux.sh " + percy_token + " python3 " + filename + " "
                                    + functionname + " " + uniqueid))
