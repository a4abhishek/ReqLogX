# Variables
VENV_DIR = .venv
PYTHON = $(VENV_DIR)/bin/python
PIP = $(VENV_DIR)/bin/pip

# Targets
.PHONY: all venv install run clean normalize-eol

all: venv install

venv:
	@echo "Creating virtual environment..."
	python -m venv $(VENV_DIR)
	@echo "Virtual environment created."

install: venv
	@echo "Installing dependencies..."
	$(PIP) install -r requirements.txt
	@echo "Dependencies installed."

run: install
	@echo "Running the server..."
	$(PYTHON) server.py

clean:
	@echo "Cleaning up..."
	rm -rf $(VENV_DIR)
	find . -type f -name '*.pyc' -delete
	find . -type d -name '__pycache__' -delete
	@echo "Cleanup complete."

normalize-eol:
	@echo "Normalizing end-of-line characters..."
	@find . -type f ! -path "./.git/*" ! -path "./.vscode/*" ! -path "./.idea/*" ! -path "./.venv/*" ! -path "./__pycache__/*" ! -path "./env/*" \
	-exec sed -i'' 's/\r$$//' {} \;
	@echo "Normalization complete for end-of-line."
