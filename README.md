# telegram-harvester

Requirements:
 - python3
 - telethon module installed

Config file:

```
[Source]
Channel1-name
Channel2-name

[Recipients]
recepient-channel-name
recepient2

[Default]
api_id=#api id from my.telegram.org
api_hash=#api hash from my.telegram.org
phone='+380xxxxxxxxx'

```

to run: `python3 service.py`