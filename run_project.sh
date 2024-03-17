#!/bin/bash

# Change directory to the location of this script
cd "$(dirname "$0")"

# Check if the virtual environment directory exists
if [ -d "myenv" ]; then
    # Activate the virtual environment
    echo "Activating virtual environment..."
    source myenv/bin/activate

    # Run _08_main.py
    echo "Running _08_main.py..."
    python3 _08_main.py

    # Deactivate the virtual environment
    echo "Deactivating virtual environment..."
    deactivate
else
    # Create virtual environment
    echo "Creating virtual environment..."
    python3 -m venv myenv

    # Activate the virtual environment
    echo "Activating virtual environment..."
    source myenv/bin/activate

    # Install dependencies from requirements.txt
    echo "Installing dependencies..."
    pip install -r requirements.txt

    # Run _08_main.py
    echo "Running _08_main.py..."
    python3 _08_main.py

    # Deactivate the virtual environment
    echo "Deactivating virtual environment..."
    deactivate
fi