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

                        check_value(data, path, errors)
                    except json.JSONDecodeError:
                        errors.append(f"خطای سینتکس در فایل: {path}")
    return errors


def check_value(obj, path, errors):
    if isinstance(obj, dict):
        if "value" in obj:
            return
        for key, value in obj.items():
            check_value(value, path, errors)
    elif isinstance(obj, list):
        for item in obj:
            check_value(item, path, errors)
    else:

        if not any(k in ["value"] for k in obj.keys() if isinstance(obj, dict)):
            return
        errors.append(f"توکن بدون value در مسیر {path} پیدا شد!")


if __name__ == "__main__":
    errors = validate_tokens("tokens")
    if errors:
        for err in errors:
            print(f"❌ {err}")
        sys.exit(1)
    print("✅ تمامی توکن‌ها معتبر هستند.")
