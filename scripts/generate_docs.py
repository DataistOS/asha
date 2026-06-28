#!/usr/bin/env python3

# Usage: python3 scripts/generate_docs.py
# Generates automated Markdown documentation for design tokens.

import json
import os


def flatten_dict(data, prefix=""):
    items = {}
    for key, value in data.items():
        new_key = f"{prefix}.{key}" if prefix else key
        if isinstance(value, dict) and 'value' not in value:
            items.update(flatten_dict(value, new_key))
        else:
            items[new_key] = value
    return items


def generate_docs(json_file, output_file, category_filter=None):
    if not os.path.exists(json_file):
        print(f"Error: {json_file} not found!")
        return

    with open(json_file, 'r') as f:
        data = json.load(f)

    flat_data = flatten_dict(data)

    # Filter and sort keys
    filtered_keys = [k for k in flat_data.keys() if
                     category_filter is None or k.startswith(category_filter)]
    sorted_keys = sorted(filtered_keys, key=lambda k: (k.split('.')[0], k))

    os.makedirs(os.path.dirname(output_file), exist_ok=True)

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(f"### Tokens: {category_filter.capitalize() if category_filter else 'All'}\n\n")
        f.write("| Token Name | Value | Preview |\n")
        f.write("| :--- | :--- | :--- |\n")

        for key in sorted_keys:
            value = flat_data[key]
            swatch_html = ""

            if isinstance(value, str):
                if value.startswith("#") or "rgb" in value:
                    swatch_html = f'<div class="token-swatch" style="background-color:{value}; width:20px; height:20px; border-radius:4px; border: 1px solid #ccc;"></div>'
                elif "size" in key and "px" in value:
                    swatch_html = f'<span style="font-size:{value}; font-weight:bold; line-height:1;">Aa</span>'

            f.write(
                f'| `{key}` | `{value}` | <div class="swatch-container">{swatch_html}</div> |\n')

    print(f"Documentation generated for '{category_filter}' at {output_file}")


if __name__ == "__main__":
    input_json = 'build/json/tokens.json'
    generate_docs(input_json, 'docs/source/tokens/colors_auto.md', category_filter='color')
    generate_docs(input_json, 'docs/source/tokens/typography_auto.md', category_filter='typography')
