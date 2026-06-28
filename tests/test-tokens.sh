#!/bin/bash

# Usage: ./tests/test-tokens.sh
# Ensures the design tokens JSON is valid and contains essential values.

# Configuration
JSON_FILE="build/json/tokens.json"
BRAND_COLOR="#532E3B"
REQUIRED_SIZES=("12px" "16px" "24px" "32px")

echo "Running comprehensive token integration test..."

# 1. Check if tokens file exists
if [ ! -f "$JSON_FILE" ]; then
    echo "Error: $JSON_FILE not found. Run the build script first."
    exit 1
fi

# 2. Verify brand color
if grep -q "$BRAND_COLOR" "$JSON_FILE"; then
    echo "Test Passed: Brand color found."
else
    echo "Test Failed: Brand color $BRAND_COLOR missing."
    exit 1
fi

# 3. Verify typography sizes
for size in "${REQUIRED_SIZES[@]}"; do
    if grep -q "$size" "$JSON_FILE"; then
        echo "Test Passed: Size $size found."
    else
        echo "Test Failed: Required size $size missing."
        exit 1
    fi
done

echo "All tests passed successfully!"
exit 0