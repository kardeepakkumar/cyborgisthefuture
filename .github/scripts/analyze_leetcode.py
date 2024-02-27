import os
import re
from collections import defaultdict
from datetime import datetime
import json

leetcode_dir = '/home/runner/work/cyborgisthefuture/cyborgisthefuture/leetcode'
readme_path = '/home/runner/work/cyborgisthefuture/cyborgisthefuture/leetcode/README.md'
data_json_path = '/home/runner/work/cyborgisthefuture/cyborgisthefuture/docs/data.json'


local = False
if local:
    leetcode_dir = '../../leetcode'
    readme_path = '../../leetcode/README.md'
    data_json_path = '../../docs/data.json'

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

datewise = ""
headers = ["Date", "Easy", "Medium", "Hard", "Total", "Cumulative"]
datewise += "|".join(f"{header:^10}" for header in headers) + "\n"
cumulative_easy, cumulative_medium, cumulative_hard = 0, 0, 0
total_easy, total_medium, total_hard = 0, 0, 0
for date in sorted(stats['date_count'].keys()):
    easy = stats['date_count'][date]['easy']
    medium = stats['date_count'][date]['medium']
    hard = stats['date_count'][date]['hard']
    total = easy + medium + hard
    cumulative_easy += easy
    cumulative_medium += medium
    cumulative_hard += hard
    cumulative_total = cumulative_easy + cumulative_medium + cumulative_hard
    total_easy += easy
    total_medium += medium
    total_hard += hard
    formatted_date = datetime.strptime(date, "%Y%m%d").strftime("%d %b %Y")
    datewise += f"{formatted_date:^10} | {easy:^4} | {medium:^6} | {hard:^4} | {total:^5} | {cumulative_total:^10}\n"
datewise += f"{'Total':^10} | {total_easy:^4} | {total_medium:^6} | {total_hard:^4} | {total_easy + total_medium + total_hard:^5} | \n"

stats_summary = f"""## LeetCode Statistics Summary

- Unique Problems Solved: {len(stats['unique_problems'])}
- Datewise Attempts
{datewise}

"""

update_readme_statistics(readme_path, stats_summary)

def defaultdict_to_dict(d):
    if isinstance(d, defaultdict):
        d = {k: defaultdict_to_dict(v) for k, v in d.items()}
    return d
date_count_dict = defaultdict_to_dict(stats['date_count'])

with open(data_json_path, 'w') as json_file:
    json.dump({"date_count": date_count_dict}, json_file, indent=4)