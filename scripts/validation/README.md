# Virtual Environments
In node scripts, we use lock files to store all dependencies for a script so that users can run `npm i` to install all dependencies. In Python, we need to create a virtual environment to hold dependencies that the script uses.

## Running this script
After navigating to the location of the script, run the following (Mac) to create the virtual environment:
```bash
python3 -m venv <name of venv>
```

Then, activate it:
```bash
source <name of venv>/bin/activate
```

Since the requirements are already packaged, run the following:
```bash
pip install -r requirements.txt
```

To deactivate a virtual environment, simply run:
```bash
deactivate
```

### Other Reference:
Creating a requirements file after installs and while using venv:
```bash
pip freeze > requirements.txt
```

Ensure you don't commit your virtual environments. In this repo, it is in the gitignore.
