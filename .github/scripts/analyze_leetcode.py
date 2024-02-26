import os
import re
from collections import defaultdict
import numpy as np
from datetime import datetime


leetcode_dir = '/home/runner/work/cyborgisthefuture/cyborgisthefuture/leetcode'
readme_path = '/home/runner/work/cyborgisthefuture/cyborgisthefuture/leetcode/README.md'

local = True
if local:
    leetcode_dir = '/Users/kardeepak.kumar/MySprinklr/code/cyborgisthefuture/leetcode'
    readme_path = '/Users/kardeepak.kumar/MySprinklr/code/cyborgisthefuture/leetcode/README.md'

def parse_percentage(value):
    return float(value.strip('%')) / 100

def update_readme_statistics(readme_path, stats_summary):
    with open(readme_path, 'r+') as readme:
        content = readme.read()
        stats_marker = "## LeetCode Statistics Summary"
        if stats_marker in content:
            new_content = re.sub(f"{re.escape(stats_marker)}.*", stats_summary, content, flags=re.DOTALL)
        else:
            new_content = content + '\n' + stats_summary
        readme.seek(0)
        readme.write(new_content)
        readme.truncate()

metadata = []
for filename in os.listdir(leetcode_dir):
    if filename.endswith('.py'):
        filepath = os.path.join(leetcode_dir, filename)
        with open(filepath, 'r') as file:
            content = file.readlines()

            metadata.append({"problem_id":filename.split('.')[0]})
            metadata[-1]["attempt"] = filename.split('.')[1]
            metadata[-1]["alias"] = filename.split('.')[2]

            keys = ["relevant-topics", "time-complexity", "space-complexity", "language", "difficulty", "date"]
            start_scraping = False

            for line in content:
                if "# metadata" in line:
                    start_scraping = True
                if start_scraping and any(key in line for key in keys):
                    _, key, value = line.strip().split(' ', 2)
                    metadata[-1][key] = value

stats = {
    "unique_problems": set(),
    "date_count": defaultdict(lambda: defaultdict(int))
}
for m in metadata:
    stats['unique_problems'].add(m['problem_id'])
    stats['date_count'][m['date']][m['difficulty']] += 1

# Initialize the string variable
datewise = ""

# Headers
headers = ["Date", "Easy", "Medium", "Hard", "Total", "Cumulative"]
datewise += "|".join(f"{header:^10}" for header in headers) + "\n"

# Initialize cumulative counters
cumulative_easy, cumulative_medium, cumulative_hard = 0, 0, 0

# Totals
total_easy, total_medium, total_hard = 0, 0, 0

for date in sorted(stats['date_count'].keys()):
    easy = stats['date_count'][date]['easy']
    medium = stats['date_count'][date]['medium']
    hard = stats['date_count'][date]['hard']
    total = easy + medium + hard

    # Update cumulative totals
    cumulative_easy += easy
    cumulative_medium += medium
    cumulative_hard += hard
    cumulative_total = cumulative_easy + cumulative_medium + cumulative_hard

    # Update totals
    total_easy += easy
    total_medium += medium
    total_hard += hard

    # Format date
    formatted_date = datetime.strptime(date, "%Y%m%d").strftime("%d %b %Y")

    # Append to datewise string
    datewise += f"{formatted_date:^10} | {easy:^4} | {medium:^6} | {hard:^4} | {total:^5} | {cumulative_total:^10}\n"

# Append totals to datewise string
datewise += f"{'Total':^10} | {total_easy:^4} | {total_medium:^6} | {total_hard:^4} | {total_easy + total_medium + total_hard:^5} | \n"

# Print the final string
print(datewise)

stats_summary = f"""## LeetCode Statistics Summary

- Unique Problems Solved: {len(stats['unique_problems'])}
- Datewise Attempts
{datewise}

"""

update_readme_statistics(readme_path, stats_summary)
