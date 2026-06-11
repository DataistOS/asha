#!/bin/bash

# Define the target color
TARGET_COLOR="#532E3B"
CSS_FILE="build/css/tokens.css"

echo "Running token integration test..."

# Check if the file exists first
if [ ! -f "$CSS_FILE" ]; then
    echo "Error: $CSS_FILE not found. Run the build script first."
    exit 1
fi

# Check for the color
if grep -q "$TARGET_COLOR" "$CSS_FILE"; then
    echo "Test Passed: $TARGET_COLOR found in $CSS_FILE."
    exit 0
else
    echo "Test Failed: $TARGET_COLOR not found in $CSS_FILE."
    exit 1
fi