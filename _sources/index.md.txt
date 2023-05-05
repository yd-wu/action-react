# Welcome to action-react's documentation!

## Overview
`action-react` specifically listens to an account in a Telegram chat and makes corresponding http calls given the content of the message. This is inspired by [tuixue.online-visa](https://github.com/Trinkle23897/tuixue.online-visa), a tool that periodically checks and publishes US consulate visa appointment availabilities across the world.

A possible application of this tool is to use it to listen to a Telegram bot publishing messages about new visa appointments, and makes http calls to the consulate appointment service to grab the desired spot.

## Installation
Install the library's dependencies and build the library using:

`pip install action-react`

## Usage
In your code, begin by importing the package:

`from action-react import main`

You can connect it to a telegram chat using:

`main(api_id, api_hash, phone, username, target_date, cities)`

For example, you can use `main("123", "hash123", "+12345678901", "username", datetime.date(2022,2,2), ["boston", "houston"])` to start the function. While the script containing `main` is running, you'll get a prompt `enter entity (telegram URL or entity id) to listen to`, to which you can enter the listener target, for example `https://t.me/tuixue_h_visa`. Afterwards, if the client is successfully connected to the chat, the script will print out logs like the ones below.

```
received message: London H: 5/17 -> 4/26
received message: Vancouver H: 2024/7/18 -> 2024/7/10
received message: Dublin H: 4/27 -> 4/21
received message: Guadalajara H: 7/25 -> 6/28
received message: Paris H: 5/2 -> 4/7
received message: Paris H: 5/2 -> 4/20
```

If a good date has been found, something like `found a good appointment in Paris on 2023-05-16` will be printed.

Alternatively, you can directly run `python main.py` after setting up the configurations in `config.ini`. The functionality will be the same as described above as the usage of the `main` function.

## API reference

```eval_rst
.. automodule:: action_react.main
    :members:
.. automodule:: action_react.react
    :members:

.. toctree::
   :maxdepth: 2
   :caption: Contents:

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
```
