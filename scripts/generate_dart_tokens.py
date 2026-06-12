import json
import os


def hex_to_flutter_color(hex_str):
    return hex_str.replace("#", "0xFF")


def process_file(file_path):
    with open(file_path, 'r') as f:
        data = json.load(f)

    filename = os.path.basename(file_path).replace('.json', '')
    class_name = filename.capitalize() + "Tokens"

    dart_code = f"class {class_name} {{\n  const {class_name}();\n"

    if 'color' in data:
        for key, info in data['color']['fig'].items():
            dart_field = key.replace("-", "")
            dart_code += f"  final {dart_field} = const Color({hex_to_flutter_color(info['value'])});\n"

    dart_code += "}\n"
    return class_name, dart_code


def generate():
    output_dir = 'packages/flutter/asha_flutter_tokens/lib/src'
    os.makedirs(output_dir, exist_ok=True)

    token_files = [f for f in os.listdir('tokens/global') if f.endswith('.json')]

    final_dart = "import 'dart:ui';\n\n"
    classes = {}

    for f in token_files:
        class_name, code = process_file(os.path.join('tokens/global', f))
        final_dart += code + "\n"
        classes[f.replace('.json', '')] = class_name

    final_dart += "class Asha {\n"
    for name, class_name in classes.items():
        final_dart += f"  static const {name} = {class_name}();\n"
    final_dart += "}"

    with open(os.path.join(output_dir, 'tokens.dart'), 'w') as f:
        f.write(final_dart)

    print("Successfully generated tokens.dart with Asha shortcut.")


if __name__ == "__main__":
    generate()
