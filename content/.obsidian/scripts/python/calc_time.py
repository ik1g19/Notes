import json
import re
import sys
import os
from datetime import datetime

def parse_time_range(start_time, end_time):
    fmt = '%Y-%m-%dT%H:%M:%S.%fZ'
    start = datetime.strptime(start_time, fmt)
    end = datetime.strptime(end_time, fmt)
    duration = (end - start).seconds // 60  # convert to minutes
    return duration

def extract_tasks_and_durations(json_content):
    data = json.loads(json_content)
    entries = data.get("entries", [])
    task_durations = {}
    productivity_total = 0

    for entry in entries:
        task_name = entry.get("name", "Unknown")
        start_time = entry.get("startTime")
        end_time = entry.get("endTime")
        if start_time and end_time:
            duration = parse_time_range(start_time, end_time)
            if task_name in task_durations:
                task_durations[task_name] += duration
            else:
                task_durations[task_name] = duration

    return task_durations

def format_frontmatter(task_durations):
    frontmatter_lines = ['---']
    for task, duration in task_durations.items():
        frontmatter_lines.append(f'{task}: "{duration}"')
    frontmatter_lines.append('---\n')
    return '\n'.join(frontmatter_lines)

def insert_frontmatter(md_content, frontmatter):
    # Find where the current frontmatter ends if it exists
    if md_content.startswith('---\n'):
        end_idx = md_content.find('---\n', 4) + 4
        return frontmatter + md_content[end_idx:]
    else:
        return frontmatter + md_content

def process_markdown_file(file_path):
    with open(file_path, 'r') as file:
        md_content = file.read()
    
    # Extract the JSON content within the simple-time-tracker block
    json_pattern = r'```simple-time-tracker\n(.*?)\n```'
    match = re.search(json_pattern, md_content, re.DOTALL)
    if not match:
        raise ValueError("No simple-time-tracker JSON block found in the markdown file.")
    
    json_content = match.group(1)
    task_durations = extract_tasks_and_durations(json_content)
    frontmatter = format_frontmatter(task_durations)
    updated_md_content = insert_frontmatter(md_content, frontmatter)
    
    with open(file_path, 'w') as file:
        file.write(updated_md_content)

# Arguments passed to the script
python_script = sys.argv[0]
file_path = sys.argv[2]
vault_path = sys.argv[1]

abs_file_path = os.path.abspath(os.path.join(vault_path, file_path))

process_markdown_file(abs_file_path)
