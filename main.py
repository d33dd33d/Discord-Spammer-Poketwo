from webserver import keep_alive
import requests

channelID = 996652797976125481
headers = {
    "authorization":
    "OTU4MjkwMjkyOTk2NDY0Njcy.YkLLnA.aNWb3jtIjDxe42Xc15u2KVwP19k"
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
