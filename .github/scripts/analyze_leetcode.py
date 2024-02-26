import os
import re
import collections
import numpy as np

def parse_percentage(value):
    return float(value.strip('%')) / 100

def update_readme_statistics(readme_path, stats_summary):
    with open(readme_path, 'r+') as readme:
        content = readme.read()
        stats_marker = "## LeetCode Statistics Summary"
        if stats_marker in content:
            new_content = re.sub(f"{stats_marker}.*?##", f"{stats_summary}\n##", content, flags=re.DOTALL)
        else:
            new_content = content + stats_summary
        print("New Content:", new_content)
        print("README: ", readme.read())
        readme.seek(0)
        readme.write(new_content)
        print("README: ", readme.read())
        readme.truncate()

leetcode_dir = '/home/runner/work/cyborgisthefuture/cyborgisthefuture/leetcode'
readme_path = '/home/runner/work/cyborgisthefuture/cyborgisthefuture/README.md'

metadata_pattern = re.compile(r'# (.*?): (.*)')

stats = {
    'problems_solved': set(),
    'time_complexity': [],
    'space_complexity': [],
    'difficulty': collections.Counter(),
    'language': collections.Counter(),
    'latest_update': '00000000'
}

for filename in os.listdir(leetcode_dir):
    if filename.endswith('.py'):
        filepath = os.path.join(leetcode_dir, filename)
        with open(filepath, 'r') as file:
            content = file.read()
            metadata = dict(metadata_pattern.findall(content))
            problem_id = filename.split('.')[0]
            stats['problems_solved'].add(problem_id)
            if 'time-complexity' in metadata:
                stats['time_complexity'].append(parse_percentage(metadata['time-complexity'].split()[-1]))
            if 'space-complexity' in metadata:
                stats['space_complexity'].append(parse_percentage(metadata['space-complexity'].split()[-1]))
            if 'difficulty' in metadata:
                stats['difficulty'][metadata['difficulty']] += 1
            if 'language' in metadata:
                stats['language'][metadata['language']] += 1
            if 'date' in metadata and metadata['date'] > stats['latest_update']:
                stats['latest_update'] = metadata['date']

avg_time_complexity = np.mean(stats['time_complexity'])
avg_space_complexity = np.mean(stats['space_complexity'])
median_time_complexity = np.median(stats['time_complexity'])
median_space_complexity = np.median(stats['space_complexity'])

stats_summary = f"""
## LeetCode Statistics Summary

- Unique Problems Solved: {len(stats['problems_solved'])}
- Difficulty Distribution: {dict(stats['difficulty'])}
- Average Time Complexity: {avg_time_complexity:.2f}
- Average Space Complexity: {avg_space_complexity:.2f}
- Median Time Complexity: {median_time_complexity:.2f}
- Median Space Complexity: {median_space_complexity:.2f}
- Languages Used: {dict(stats['language'])}
- Last Updated: {stats['latest_update']}
"""

update_readme_statistics(readme_path, stats_summary)
