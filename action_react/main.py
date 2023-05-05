import configparser

from datetime import datetime
from action_react.react import react
from telethon import TelegramClient, events
from telethon.tl.types import PeerChannel

CATEGORY = "H"
FILENAME = "config.ini"


def read_configs(file_name):
    """
    Read configuration parameters from a file.

    Parameters
    ----------
    file_name: str, relative path from the root directory of this package

    Returns
    -------
    api_id: telegram api id
    api_hash: telegram api hash
    phone: telegram phone number
    username: telegram username
    target_date: the date upon which to improve
    cities: list of city names
    """
    config = configparser.ConfigParser()
    config.read(file_name)
    api_id = config["Telegram"]["api_id"]
    api_hash = str(config["Telegram"]["api_hash"])
    phone = config["Telegram"]["phone"]
    username = config["Telegram"]["username"]
    target_date = datetime.strptime(config["General"]["target-date"], "%m/%d/%Y").date()
    cities = config["General"]["cities"].split(", ")
    return api_id, api_hash, phone, username, target_date, cities


def get_target_channel():
    """
    Read telegram channel to listen to from command line.

    Returns
    -------
    listening_channel: channel name
    """
    listening_channel = input("enter entity (telegram URL or entity id) to listen to: ")
    if listening_channel.isdigit():
        return PeerChannel(int(listening_channel))
    return listening_channel


def connect_to_telegram(username, api_id, api_hash, phone):
    """
    Connect to telegram

    Parameters
    ----------
    username: str, user name
    api_id: str, telegram api id
    api_hash: str, telegram api hash
    phone: str, phone number

    Returns
    -------
    client: telegram client
    """
    client = TelegramClient(username, api_id, api_hash)
    client.start()
    return client


def check_message(message, target_date, cities):
    """
    Process incoming telegram messages

    Parameters
    ----------
    message: str, message
    target_date: date, the date upon which to improve
    cities: list of city names

    Returns
    -------
    A tuple. The first element indicates whether a good date
    can be retrieved from the message. The second element is None
    if the first element is False. Otherwise, it's a tuple whose
    first element is the date and the second element is the city
    """
    try:
        colon_list = message.split(":")
        message_list = [" ".join(colon_list[0].split()[:-1])] + [colon_list[0].split()[-1]] + colon_list[1].split()
        if message_list[1] == CATEGORY:
            city = message_list[0]
            date = message_list[-1]
            if len(date.split("/")) == 2:
                date = "2023/" + date
            date = datetime.strptime(date, "%Y/%m/%d").date()
            if date < target_date and city.lower() in cities:
                return True, (date, city)
        return False, None
    except Exception as e:
        print(f"error {e}")
        return False, None


def main(api_id, api_hash, phone, username, target_date, cities):
    """
    Main function that acts on a target telegram message. It runs
    until interrupted.

    Parameters
    ----------
    api_id: str, telegram api id
    api_hash: str, telegram api hash
    phone: str, telegram phone number
    username: str, telegram username
    target_date: date, the date upon which to improve
    cities: [str], list of city names
    """
    listening_channel = get_target_channel()
    client = connect_to_telegram(username, api_id, api_hash, phone)

    @client.on(events.NewMessage(chats=listening_channel))
    async def listener(event):
        message = event.message.message
        print("received message:\n" + message)
        is_good, info = check_message(message, target_date, cities)
        if is_good:
            date, city = info
            react(date, city)
            print(f"found a good appointment in {city} on {date} ")

    with client:
        client.run_until_disconnected()


if __name__ == "__main__":
    api_id, api_hash, phone, username, target_date, cities = read_configs(FILENAME)
    main(api_id, api_hash, phone, username, target_date, cities)
