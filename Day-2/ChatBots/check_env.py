# python -m venv myenv

# import os module
import os

# check if virtual environment is running
def is_virtualenv():
    return 'VIRTUAL_ENV' in os.environ

if is_virtualenv():
    print("Running inside a virtual environment.")
else:
    print("Not running inside a virtual environment.")