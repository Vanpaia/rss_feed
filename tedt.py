import feedparser
import json

with open('all_rss_data.json', 'r') as f:
    rss_library = json.load(f)

total = 0

for entry in rss_library:
    total += 1

print(total)

#with open("all_rss_data.json", "w") as data_file:
#    json.dump(rss_library[0:359], data_file, indent=3)