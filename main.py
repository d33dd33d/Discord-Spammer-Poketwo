from webserver import keep_alive
import requests

channelID = 1134727055796359189
headers = {
    "authorization":
    "MTA3MTA5NTA2ODkwMDk5NTA3Mw.GuKccf.H1aoot_RsnsNA5ATntEpwB8XEljNeiocQUJwJ0"
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
