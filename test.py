from telethon import TelegramClient, events, utils
from telethon.tl.types import PeerChannel
import json
import os

api_id = # получить на my.telegram.org
api_hash = # получить на my.telegram.org
phone = '+38093#######'

client = TelegramClient(phone, api_id, api_hash)

source_channel_peer_name = 'Test-telethon-channel'
recievers = ['igorkauf','avtomonstr']


@client.on(events.NewMessage(outgoing=False))
async def handler(event):
    entity = await client.get_entity(event.message.to_dict()['peer_id']['channel_id'])
    if json.loads(entity.to_json())['title'] == source_channel_peer_name:
        print(event.message.to_dict()['message'])
        result = await client.download_media(event.message.media)
        print(result)
        for reciever in recievers:
            await client.send_message(reciever, event.message.to_dict()['message'], file=result)

client.start()

with client:
    client.add_event_handler(handler)
    client.run_until_disconnected()