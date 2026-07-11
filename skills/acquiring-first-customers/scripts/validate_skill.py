import os
import yaml
import re
import sys

def validate_skill(file_path):
    errors = []

    if not os.path.exists(file_path):
        return [f"File not found: {file_path}"]

    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        content = "".join(lines)

    # 1. Line count limit
    if len(lines) > 500:
        errors.append(f"Skill file exceeds 500 lines (current: {len(lines)}).")

    # 2. No XML tags allowed
    if re.search(r'<[^>]+>', content):
        errors.append("Skill file contains XML/HTML tags, which are strictly forbidden.")

    # 3. YAML frontmatter validation
    if not content.startswith('---'):
        errors.append("Missing YAML frontmatter at the start of the file.")
    else:
        parts = content.split('---')
        if len(parts) < 3:
            errors.append("Malformed YAML frontmatter. Ensure it is closed with '---'.")
        else:
            frontmatter_str = parts[1]
            try:
                frontmatter = yaml.safe_load(frontmatter_str)

                # Check name
                if 'name' not in frontmatter:
                    errors.append("Frontmatter missing 'name' field.")
                else:
                    name = str(frontmatter['name'])
                    if not re.match(r'^[a-z]+(-[a-z]+)*$', name):
                        errors.append(f"Name '{name}' is not lowercase-hyphenated.")
                    if len(name) >= 64:
                        errors.append(f"Name '{name}' must be under 64 characters (current: {len(name)}).")

                # Check description
                if 'description' not in frontmatter:
                    errors.append("Frontmatter missing 'description' field.")
                else:
                    description = str(frontmatter['description'])
                    if len(description) >= 1024:
                        errors.append(f"Description must be under 1024 characters (current: {len(description)}).")

            except yaml.YAMLError as e:
                errors.append(f"Failed to parse YAML frontmatter: {e}")

    return errors

if __name__ == '__main__':
    skill_file = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'SKILL.md')
    errors = validate_skill(skill_file)

    if errors:
        print("Validation failed with the following errors:")
        for error in errors:
            print(f"- {error}")
        sys.exit(1)
    else:
        print("Validation passed successfully.")
        sys.exit(0)
