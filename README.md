<p float="left">
  <img src="https://branditechture.agency/brand-logos/wp-content/uploads/wpdm-cache/Percy-900x0.png" width="200" height="100" title="Percy.IO">
  <img src="https://raw.githubusercontent.com/computefoundation/gnu-linux-shell-scripting/images/logo.png" width="200" height="100" title="Percy.IO2">
  <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/1869px-Python-logo-notext.svg.png" width="100" height="100" title="Percy.IO2">
</p>
  
# Running a Shell Script via Python to execute Percy commands

This test, helper class and set of shell scripts is designed to show an example of how to execute a shell script in Python with the intention of executing Percy against your test scripts.

## Usage

In a terminal, type the following:

```sh
python my_test.py run_test_via_percy
```

By passing the function name "run_test_via_percy" we are telling Python to only execute this particular function. In order for this to work, the following needs to be added to the end of your Python test script:

```python
if __name__ == '__main__':
    globals()[sys.argv[1]]()
```

The <b>run_test_via_percy()</b> function calls the utility method to execute the shell script. It passes in the correct function name "run_test" which contains all of our test and Percy snapshot logic. 

```python
def run_test_via_percy():
    utils.run_through_percy(percy_token, sys.argv[0], run_test.__name__, str(unique_id))
```

* `sys.argv[0]` is the first argument, which is the name of the file, so we use this to pass the file to the Percy command.
* `run_test.__name__` is the way we call the function we want to run

**NOTE:** If you would prefer not to use the if statement above, then you can simply place your test code in a function, and place the <b>run_test_via_percy()</b> function in the same file and call it at the end. Just make sure it has the correct function name for your specific test.