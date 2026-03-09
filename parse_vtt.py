import re
import sys

def parse_vtt(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    content = re.sub(r'WEBVTT.*?\n\n', '', content, flags=re.DOTALL)
    content = re.sub(r'\d{2}:\d{2}:\d{2}\.\d{3} --> \d{2}:\d{2}:\d{2}\.\d{3}.*?\n', '', content)
    content = re.sub(r'<[^>]+>', '', content)
    content = re.sub(r'align:start position:0%.*?\n', '', content)

    lines = content.split('\n')
    cleaned_lines = []
    prev_line = None
    for line in lines:
        line = line.strip()
        if line and line != prev_line:
            cleaned_lines.append(line)
            prev_line = line

    return ' '.join(cleaned_lines)

if __name__ == '__main__':
    text = parse_vtt(sys.argv[1])
    with open('clean_transcript.txt', 'w', encoding='utf-8') as f:
        f.write(text)
