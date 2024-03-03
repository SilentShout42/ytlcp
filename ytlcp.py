#!/usr/bin/env python
import json
import sys

with open(sys.argv[1]) as f:
    for l in f.readlines():
        j = json.loads(l)
        try:
            lctmr = j["replayChatItemAction"]["actions"][0]["addChatItemAction"]["item"]["liveChatTextMessageRenderer"]
            author_name = lctmr["authorName"]["simpleText"]
            timestamp = lctmr["timestampText"]["simpleText"]
            runs = lctmr["message"]["runs"]
            simple_runs_list = []
            for run in runs:
                if 'text' in run.keys():
                    simple_runs_list.append(run["text"])
                elif 'emoji' in run.keys():
                    emoji_label = run["emoji"]["image"]["accessibility"]["accessibilityData"]["label"]
                    simple_runs_list.append(f":{emoji_label}:")
            s = " ".join(simple_runs_list)
            print(f"[{timestamp}] {author_name}: {s}")
            # print(lctmr)
        except Exception as e:
            print(f"Exception! {e}", file=sys.stderr)
            continue
