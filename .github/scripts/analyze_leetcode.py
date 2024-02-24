import os
import re
import collections

print("Starting script...")

# Define the path to the leetcode directory
leetcode_dir = '/home/runner/work/cyborgisthefuture/cyborgisthefuture/leetcode'
readme_path = '/home/runner/work/cyborgisthefuture/cyborgisthefuture/README.md'

print(f"LeetCode directory set to {leetcode_dir}")
print(f"README path set to {readme_path}")

# Regex patterns to extract metadata
metadata_pattern = re.compile(r'# (.*?): (.*)')
print("Regex pattern for metadata extraction compiled.")

# Data structure to hold the statistics
stats = {
    'problems_solved': set(),
    'time_complexity': [],
    'space_complexity': [],
    'difficulty': collections.Counter()
}
print("Initialized data structures for storing statistics.")

# Traverse the leetcode directory and parse each Python file
print("Traversing the LeetCode directory...")
for filename in os.listdir(leetcode_dir):
    print(f"Processing file: {filename}")
    if filename.endswith('.py'):
        filepath = os.path.join(leetcode_dir, filename)
        print(f"Reading file at {filepath}")
        with open(filepath, 'r') as file:
            content = file.read()
            metadata = dict(metadata_pattern.findall(content))
            print(f"Extracted metadata: {metadata}")
            problem_id = filename.split('.')[0]
            stats['problems_solved'].add(problem_id)
            if 'time-complexity' in metadata:
                stats['time_complexity'].append(metadata['time-complexity'])
            if 'space-complexity' in metadata:
                stats['space_complexity'].append(metadata['space-complexity'])
            if 'difficulty' in metadata:
                stats['difficulty'][metadata['difficulty']] += 1

print("Finished processing all files.")

# Calculate additional statistics
unique_problems = len(stats['problems_solved'])
print(f"Unique problems solved: {unique_problems}")

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

print("Statistics summary prepared.")

# Update or append the statistics summary to the README.md
if os.path.exists(readme_path):
    with open(readme_path, 'r+') as readme:
        content = readme.read()
        stats_marker = "## LeetCode Statistics Summary"
        print("README.md exists, checking for existing statistics summary...")
        if stats_marker in content:
            # Update the existing statistics section
            print("Updating existing statistics summary...")
            new_content = re.sub(f"{stats_marker}.*?##", f"{stats_summary}\n##", content, flags=re.DOTALL)
        else:
            # Append the new statistics section
            print("Appending new statistics summary...")
            new_content = content + stats_summary
        readme.seek(0)
        readme.write(new_content)
        readme.truncate()
else:
    print("README.md does not exist, creating new file with statistics summary...")
    with open(readme_path, 'w') as readme:
        readme.write(stats_summary)

print("Script execution complete.")
