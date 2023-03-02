
# action-react

`action-react` is a tool that reacts to Telegram chat messages.

![GitHub](https://img.shields.io/github/license/yd-wu/action-react)
![GitHub](https://img.shields.io/github/issues/yd-wu/action-react)

[Project Board](https://github.com/users/yd-wu/projects/1/views/1)

## Overview
`action-react` specifically listens to an account in a Telegram chat and makes corresponding http calls given the content of the message. This is inspired by [tuixue.online-visa](https://github.com/Trinkle23897/tuixue.online-visa), a tool that periodically checks and publishes US consulate visa appointment availabilities across the world.

A possible application of this tool is to use it to listen to a Telegram bot publishing messages about new visa appointments, and makes http calls to the consulate appointment service to grab the desired spot.
