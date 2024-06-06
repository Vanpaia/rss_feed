import feedparser
import json
import datetime
import logging

with open('/home/hagen/PycharmProjects/rss_feed/all_rss_data.json', 'r') as f:
    rss_library = json.load(f)

rss_new = []

nieuws_algemeen = "https://feeds.nos.nl/nosnieuwsalgemeen"
nieuws_binnenland = "https://feeds.nos.nl/nosnieuwsbinnenland"
nieuws_buitenland = "https://feeds.nos.nl/nosnieuwsbuitenland"
nieuws_politiek = "https://feeds.nos.nl/nosnieuwspolitiek"
nieuws_economie = "https://feeds.nos.nl/nosnieuwseconomie"
nieuws_opmerkelijk = "https://feeds.nos.nl/nosnieuwsopmerkelijk"
nieuws_koningshuis = "https://feeds.nos.nl/nosnieuwskoningshuis"
nieuws_cultuur_en_media = "https://feeds.nos.nl/nosnieuwscultuurenmedia"
nieuws_tech = "https://feeds.nos.nl/nosnieuwstech"
sport_algemeen = "https://feeds.nos.nl/nossportalgemeen"
sport_voetbal = "https://feeds.nos.nl/nosvoetbal"
sport_wielrennen = "https://feeds.nos.nl/nossportwielrennen"
sport_schaatsen = "https://feeds.nos.nl/nossportschaatsen"
sport_tennis = "https://feeds.nos.nl/nossporttennis"
sport_formule_1 = "https://feeds.nos.nl/nossportformule1"
nieuwsuur = "https://feeds.nos.nl/nieuwsuuralgemeen"
NOS_op_3 = "https://feeds.nos.nl/nosop3"
NOS_jeugdjournaal = "https://feeds.nos.nl/jeugdjournaal"

rss_feeds = [
    nieuws_algemeen,
    nieuws_binnenland,
    nieuws_buitenland,
    nieuws_politiek,
    nieuws_economie,
    nieuws_opmerkelijk,
    nieuws_koningshuis,
    nieuws_cultuur_en_media,
    nieuws_tech,
    sport_algemeen,
    sport_voetbal,
    sport_wielrennen,
    sport_schaatsen,
    sport_tennis,
    sport_formule_1,
    nieuwsuur,
    NOS_op_3,
    NOS_jeugdjournaal
    ]


for feed in rss_feeds:
    NewsFeed = feedparser.parse(feed)
    for entry in NewsFeed.entries:
        rss_new.append(entry)

newfound_entries = 0

for new_entry in rss_new:
    duplicate = False
    for data in rss_library:
        if new_entry["id"] == data["id"] and new_entry["summary_detail"]["base"] == data["summary_detail"]["base"]:
            duplicate = True
            break
    if duplicate is False:
        rss_library.append(new_entry)
        newfound_entries += 1

with open('/home/hagen/PycharmProjects/rss_feed/all_rss_data.json', 'w') as data_file:
    json.dump(rss_library, data_file, indent=3)

logging.basicConfig(level=logging.INFO, filename="/home/hagen/PycharmProjects/rss_feed/py_log.log",filemode="a",
                    format="%(asctime)s %(levelname)s %(message)s")
logging.info(f'We have found {newfound_entries} new RSS entries, bringing us to a total of {len(rss_library)} RSS entries.')

