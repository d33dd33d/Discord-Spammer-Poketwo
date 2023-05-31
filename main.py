from webserver import keep_alive
import requests

channelID = 1113549649538719794
headers = {
    "authorization":
    "1107738462452457564"
}
keep_alive()
file = open("text.txt", "r")
lines = file.readlines()

while True:
    for line in lines:
        requests.post(
            f"https://discord.com/api/v9/channels/{1113549649538719794}/messages",
            headers=headers,
            json={"content": line})
