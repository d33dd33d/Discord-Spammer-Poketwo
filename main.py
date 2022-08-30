from webserver import keep_alive
import requests

channelID = 1014267027101331486
headers = {
    "authorization":
    "MTAxMjYzNTcyODA4MzE1NzAxMg.GpJh9_.6civD5-SgseqWjYBdjBrlX62bW4lZXQpEwBS-c"
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
