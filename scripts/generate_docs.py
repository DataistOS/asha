import json
import os


def flatten_dict(data, prefix=""):
    """تبدیلِ دیکشنریِ تو در تو به یک لیستِ تخت برای مستندات"""
    items = {}
    for key, value in data.items():
        new_key = f"{prefix}.{key}" if prefix else key
        if isinstance(value, dict):
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

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write("# مستندات توکن‌های طراحی (Automated)\n\n")
        f.write("| نام توکن (مسیر) | مقدار | پیش‌نمایش |\n")
        f.write("| :--- | :--- | :--- |\n")

        for key, value in sorted(flat_data.items()):

            swatch_html = ""
            if isinstance(value, str) and (value.startswith("#") or "rgb" in value):
                swatch_html = f'<div class="token-swatch" style="background-color:{value};"></div>'

            f.write(
                f'| `{key}` | `{value}` | <div class="swatch-container">{swatch_html}</div> |\n')

    print(f"مستندات با پیش‌نمایش گرافیکی در {output_file} تولید شد.")


if __name__ == "__main__":
    generate_docs('build/json/tokens.json', 'docs/source/tokens/colors_auto.md')
