#!/bin/bash

# Change directory to the location of this script
cd "$(dirname "$0")"

# Check if the virtual environment directory exists, if not, create it
if [ ! -d "myenv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv myenv
fi

# Activate the virtual environment
echo "Activating virtual environment..."
source myenv/bin/activate

# Install dependencies from requirements.txt
echo "Installing dependencies..."
pip install -r requirements.txt

# Run main.py
echo "Running main.py..."
python _08_main.py

# Deactivate the virtual environment
echo "Deactivating virtual environment..."
deactivate