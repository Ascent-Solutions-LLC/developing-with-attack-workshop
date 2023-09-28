# Developing with MITRE ATT&CK


## Setup
The examples in this repo are built for a Python3 environment.

### Create a Virtual Environments

**Using `virtualenv`**
```bash
virtualenv -p python3.9 env
```

or using **`venv`**

```bash
python3 -m venv workshop-env
```

Activate the virtual environment:

```bash
source env/bin/activate
```

or on Windows:

```cmd
env\Scripts\activate.bat
```

### Install the requirements

See `requirements.txt` for the packages which will be installed

```bash
python -m pip install -r requirements.txt
```

## Check

Make sure everything works!

```bash
python workshop_check.py
```
