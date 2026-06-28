#!/usr/bin/env python3

# Usage: python3 scripts/validate_tokens.py
# Validates all JSON files in the tokens directory to ensure they contain a 'value' field.

import json
import os
import sys


def validate_tokens(directory):
    errors = []
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".json"):
                path = os.path.join(root, file)
                with open(path, 'r') as f:
                    try:
                        data = json.load(f)
                        check_structure(data, path, errors)
                    except json.JSONDecodeError:
                        errors.append(f"Syntax error in file: {path}")
    return errors


def check_structure(obj, path, errors):
    """Recursively checks that objects containing tokens have a 'value' field."""
    if isinstance(obj, dict):
        # If this dict looks like a token, it must have a 'value'
        if "type" in obj or "value" in obj or "category" in obj:
            if "value" not in obj:
                errors.append(f"Missing 'value' field in: {path} -> {obj}")
            return

        # Otherwise, keep digging
        for key, value in obj.items():
            check_structure(value, path, errors)

    elif isinstance(obj, list):
        for item in obj:
            check_structure(item, path, errors)


if __name__ == "__main__":
    validation_errors = validate_tokens("tokens")

    if validation_errors:
        for error in validation_errors:
            print(f"❌ {error}")
        sys.exit(1)

    print("✅ All tokens are valid.")
