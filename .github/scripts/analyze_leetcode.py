import os
import re
import collections

# Define the path to the leetcode directory
readme_path = 'cyborgisthefuture/README.md'

# Regex patterns to extract metadata
metadata_pattern = re.compile(r'# (.*?): (.*)')

# Data structure to hold the statistics
stats = {
    'problems_solved': set(),
    'time_complexity': [],
    'space_complexity': [],
    'difficulty': collections.Counter()
}

# Traverse the leetcode directory and parse each Python file
for filename in os.listdir(leetcode_dir):
    if filename.endswith('.py'):
        filepath = os.path.join(leetcode_dir, filename)
        with open(filepath, 'r') as file:
            content = file.read()
            metadata = dict(metadata_pattern.findall(content))
            problem_id = filename.split('.')[0]
            stats['problems_solved'].add(problem_id)
            if 'time-complexity' in metadata:
                stats['time_complexity'].append(metadata['time-complexity'])
            if 'space-complexity' in metadata:
                stats['space_complexity'].append(metadata['space-complexity'])
            if 'difficulty' in metadata:
                stats['difficulty'][metadata['difficulty']] += 1

# Calculate additional statistics
unique_problems = len(stats['problems_solved'])
avg_time_complexity = 'Not calculable' # Placeholder, requires parsing and averaging logic
avg_space_complexity = 'Not calculable' # Placeholder, requires parsing and averaging logic

# Prepare the statistics summary
stats_summary = f"""
## LeetCode Statistics Summary

- Unique Problems Solved: {unique_problems}
- Difficulty Distribution: {dict(stats['difficulty'])}
- Average Time Complexity: {avg_time_complexity} (Placeholder)
- Average Space Complexity: {avg_space_complexity} (Placeholder)
"""

# Update or append the statistics summary to the README.md
if os.path.exists(readme_path):
    with open(readme_path, 'r+') as readme:
        content = readme.read()
        stats_marker = "## LeetCode Statistics Summary"
        if stats_marker in content:
            # Update the existing statistics section
            new_content = re.sub(f"{stats_marker}.*?##", f"{stats_summary}\n##", content, flags=re.DOTALL)
        else:
            # Append the new statistics section
            new_content = content + stats_summary
        readme.seek(0)
        readme.write(new_content)
        readme.truncate()
else:
    with open(readme_path, 'w') as readme:
        readme.write(stats_summary)

