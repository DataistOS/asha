import json
import os


def flatten_dict(data, prefix=""):
    items = {}
    for key, value in data.items():
        new_key = f"{prefix}.{key}" if prefix else key
        if isinstance(value, dict) and 'value' not in value:  # تو در تو بودن
            items.update(flatten_dict(value, new_key))
        else:
            items[new_key] = value
    return items


def generate_docs(json_file, output_file):
    if not os.path.exists(json_file):
        print(f"File {json_file} not found!")
        return

    with open(json_file, 'r') as f:
        data = json.load(f)

    flat_data = flatten_dict(data)

    # مرتب‌سازی بر اساس دسته‌بندی (Color, Typography, Spacing)
    sorted_keys = sorted(flat_data.keys(), key=lambda k: (k.split('.')[0], k))

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write("# مستندات توکن‌ها (Automated)\n\n")
        f.write("| نام توکن (مسیر) | مقدار | پیش‌نمایش |\n")
        f.write("| :--- | :--- | :--- |\n")

        current_category = ""
        for key in sorted_keys:
            value = flat_data[key]
            category = key.split('.')[0]

            # افزودنِ جداکننده بصری بین دسته‌ها
            if category != current_category:
                f.write(f"| **{category.upper()}** | | |\n")
                current_category = category

            swatch_html = ""
            if isinstance(value, str) and (value.startswith("#") or "rgb" in value):
                swatch_html = f'<div class="token-swatch" style="background-color:{value};"></div>'

            f.write(
                f'| `{key}` | `{value}` | <div class="swatch-container">{swatch_html}</div> |\n')

    print(f"مستندات مرتب‌سازی شده در {output_file} تولید شد.")


if __name__ == "__main__":
    generate_docs('build/json/tokens.json', 'docs/source/tokens/colors_auto.md')
