import re

keyPhrase = r'Hello'

timeRegex = r'(?P<time>\d{4}-\d{1,2}-\d{1,2} \d{2}:\d{2}:\d{2})'

severityRegex = r'(?P<severity>DBG|INF|WRN|ERR)'

regex = f'^{timeRegex}.*?{severityRegex}.*{keyPhrase}'

desired_lines = []
with open('dummy.log', 'r') as file:
    for line in file:
        match = re.search(regex, line.strip())
        if match:
            print(match.groupdict())
