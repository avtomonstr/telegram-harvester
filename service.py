from telethon import TelegramClient, events, utils
from telethon.tl.types import PeerChannel
import json
import os
import configparser

# reading config from config.ini file
config = configparser.ConfigParser(allow_no_value=True)
config.optionxform=str
config.read('config.ini')

source_channels = []
recipients_channels = []

for item in config['Source']:
    source_channels.append(str(item))

for item in config['Recipients']:
    recipients_channels.append(str(item))

api_id = config['Default']['api_id'] 
api_hash = config['Default']['api_hash']
phone = config['Default']['phone']


#client instance creation
client = TelegramClient(phone, api_id, api_hash)

messageText = ''

# handling all events
@client.on(events.NewMessage(outgoing=False))
async def handler(event):
    # get event source name
    entity = await client.get_entity(event.message.to_dict()['peer_id']['channel_id'])
    if json.loads(entity.to_json())['title'] in source_channels:
        print(event.message.to_dict()['message'])
        print(messageText)  
        result = await client.download_media(event.message.media)
        if messageText != event.message.to_dict()['message']:
            for recipient in recipients_channels:
                # get reciepient peer
                entity = await  client.get_entity(recipient)
                # send
                await client.send_message(entity, message=event.message.to_dict()['message'], file=result)
            messageText = event.message.to_dict()['message']

client.start()

with client:
    client.add_event_handler(handler)
    client.run_until_disconnected()