from webserver import keep_alive
import requests

channelID = 756173881697370233
headers = {
    "authorization":
    "MTAzNDg4NTExODQwNzQ5NTcwMA.GgHmgT.7Ep61sRYFXE1j35-6TriAi4E9J5sp7lr1qmNc4"
}
keep_alive()
file = open("text.txt", "r")
lines = file.readlines()

while True:
    for line in lines:
        requests.post(
            f"https://discord.com/api/v9/channels/{channelID}/messages",
            headers=headers,
            json={"content": line})
