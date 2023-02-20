import asyncio
import configparser
import json

from datetime import date, datetime

from telethon import TelegramClient
from telethon.errors import SessionPasswordNeededError
from telethon.tl.functions.messages import (GetHistoryRequest)
from telethon.tl.types import PeerChannel


class DateTimeEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, datetime):
            return o.isoformat()
        if isinstance(o, bytes):
            return list(o)
        return json.JSONEncoder.default(self, o)

def read_configs():
    config = configparser.ConfigParser()
    config.read("config.ini")
    api_id = config['Telegram']['api_id']
    api_hash = str(config['Telegram']['api_hash'])
    phone = config['Telegram']['phone']
    username = config['Telegram']['username']
    return api_id, api_hash, phone, username

async def main(phone):
    print("starting client")
    await client.start()
    print("client started")
    if await client.is_user_authorized() == False:
        await client.send_code_request(phone)
        try:
            await client.sign_in(phone, input('enter the code: '))
        except SessionPasswordNeededError:
            await client.sign_in(password=input('password: '))

    entity = input('enter telegram URL:')
    my_channel = await client.get_entity(entity)

    offset_id = 0
    limit = 10
    all_messages = []
    total_messages = 0
    total_count_limit = 30
    print("saving chat messages")
    while True:
        history = await client(GetHistoryRequest(
            peer=my_channel,
            offset_id=offset_id,
            offset_date=None,
            add_offset=0,
            limit=limit,
            max_id=0,
            min_id=0,
            hash=0
        ))
        messages = history.messages
        if not messages:
            break
        for message in messages:
            all_messages.append(message.to_dict())
        offset_id = messages[len(messages)-1].id
        total_messages = len(all_messages)
        if total_count_limit != 0 and total_messages >= total_count_limit:
            break
    print(f"saved {total_messages} messages")
    with open('messages.json', 'w') as outfile:
        json.dump(all_messages, outfile, cls=DateTimeEncoder)

if __name__ == "__main__":
    api_id, api_hash, phone, username = read_configs()
    with TelegramClient(username, api_id, api_hash) as client:
        client.loop.run_until_complete(main(phone))
