# GLOBALS
PYTHON = python3

# COMMANDS
install-pip-tools:
	$(PYTHON) -m pip install pip-tools 

requirements: install-pip-tools
	$(PYTHON) -m pip install -r requirements.txt 