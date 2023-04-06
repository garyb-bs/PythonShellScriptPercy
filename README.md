<p float="left">
  <img src="https://branditechture.agency/brand-logos/wp-content/uploads/wpdm-cache/Percy-900x0.png" width="200" height="100" title="Percy.IO">
  <img src="https://raw.githubusercontent.com/computefoundation/gnu-linux-shell-scripting/images/logo.png" width="200" height="100" title="Percy.IO2">
  <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/1869px-Python-logo-notext.svg.png" width="100" height="100" title="Percy.IO2">
</p>
  
# Running a Shell Script via Python to execute Percy commands

This function and set of shell scripts is designed to show an example of how to execute a shell script in Python with the intention of executing Percy against your test scripts.

## Usage

In a terminal, type the following:

```sh
python run_percy_command.py
```

There is logic in the code to determine the OS you are running the script from and this will determine which shell script gets picked up. If no matching OS is found (this is highly unlikely!) an Exception is raised.

Using this script you can pass your Percy token and the relevant test command to the shell script.

You can easily take the function and place it in an existing utility class and use it with your existing project. You can also easily change what is passed to the shell script with some simple changes. This is just a simple example but highly malleable.
