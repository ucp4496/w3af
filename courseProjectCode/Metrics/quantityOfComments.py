import os

def count_python_comments(directory):
    comment_lines = 0
    in_multiline_comment = False

    for root, dirs, files in os.walk(directory):
        if 'courseProjectCode' in dirs:
            dirs.remove('courseProjectCode')
        if 'courseProjectDocs' in dirs:
            dirs.remove('courseProjectDocs')

        for file in files:
            if file.endswith('.py'):
                filepath = os.path.join(root, file)
                with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
                    for line in f:
                        stripped = line.strip()
                        if stripped.startswith('"""') or stripped.startswith("'''"):
                            if in_multiline_comment:
                                in_multiline_comment = False
                                comment_lines += 1
                            else:
                                in_multiline_comment = True
                                comment_lines += 1
                        elif in_multiline_comment:
                            comment_lines += 1
                        elif stripped.startswith('#'):
                            comment_lines += 1
    return comment_lines

current_dir = os.path.dirname(os.path.abspath(__file__))
project_path = os.path.abspath(os.path.join(current_dir, '..', '..'))

total_comments = count_python_comments(project_path)
print(f'Total comment lines in Python files: {total_comments}')
