from webserver import keep_alive
import requests

channelID =1022809302664220693
headers = {
    "authorization":
    "MTAxNDA1NDEzNjQzOTkxODcwMg.G3I-EP.LvBkFjHSReaUz6g0oxDH7NjZh2QP_0ju8inKv0"
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
