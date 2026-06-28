#!/usr/bin/env python3

# Usage: python3 scripts/generate_dart_tokens.py
# Generates Dart classes for Flutter tokens from JSON source files.

import json
import os

TYPO_MAPPING = {
    "small": "12.0",
    "medium": "16.0",
    "large": "24.0",
    "xlarge": "32.0"
}


def hex_to_flutter_color(hex_str):
    """Converts hex color string to Flutter Color format."""
    return hex_str.replace("#", "0xFF")


def process_file(file_path):
    """Parses JSON token file and generates Dart class code."""
    with open(file_path, 'r') as f:
        data = json.load(f)

    filename = os.path.basename(file_path).replace('.json', '')
    class_name = filename.capitalize().replace('-', '_') + "Tokens"

    dart_code = ""
    # Add import if typography exists
    if 'typography' in data:
        dart_code += "import 'package:flutter/material.dart';\n"

    dart_code += f"class {class_name} {{\n  const {class_name}();\n"

    # Process Colors
    if 'color' in data:
        for key, info in data['color'].get('fig', {}).items():
            dart_field = key.replace("-", "")
            dart_code += f"  final {dart_field} = const Color({hex_to_flutter_color(info['value'])});\n"

    # Process Typography
    if 'typography' in data:
        for key, info in data['typography'].items():
            dart_field = key.replace("-", "_")
            size_token = info.get('size', {}).get('value', '').split('.')[-1].replace('}', '')
            size = TYPO_MAPPING.get(size_token, "16.0")
            weight = 'FontWeight.bold' if 'bold' in str(
                info.get('weight', {})) else 'FontWeight.normal'
            dart_code += f"  final {dart_field} = const TextStyle(fontSize: {size}, fontWeight: {weight});\n"

    dart_code += "}\n"
    return class_name, dart_code


def generate():
    """Generates the main tokens.dart entry file."""
    output_dir = 'packages/flutter/asha_flutter_tokens/lib/src'
    os.makedirs(output_dir, exist_ok=True)

    token_folders = ['tokens/global', 'tokens/semantic']
    token_files = []

    for folder in token_folders:
        if os.path.exists(folder):
            for f in os.listdir(folder):
                if f.endswith('.json'):
                    token_files.append((folder, f))

    final_dart = "import 'dart:ui';\n\n"
    classes = {}

    for folder, f in token_files:
        class_name, code = process_file(os.path.join(folder, f))
        final_dart += code + "\n"
        classes[f.replace('.json', '')] = class_name

    # Generate entry class
    final_dart += "class Asha {\n"
    for name, class_name in classes.items():
        final_dart += f"  static const {name.replace('-', '_')} = {class_name}();\n"
    final_dart += "}"

    with open(os.path.join(output_dir, 'tokens.dart'), 'w') as f:
        f.write(final_dart)

    print("Successfully generated tokens.dart.")


if __name__ == "__main__":
    generate()
