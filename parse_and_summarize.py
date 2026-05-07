import os

def create_deep_notes():
    """
    Reads session notes from a template file and writes them to the output file.
    """
    template_path = os.path.join('resources', 'session2_notes.md')
    output_path = 'part2_sales.md'

    try:
        with open(template_path, 'r', encoding='utf-8') as f:
            md_content = f.read()

        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(md_content)

    except FileNotFoundError:
        print(f"Error: Template file not found at {template_path}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == '__main__':
    create_deep_notes()
