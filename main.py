from webserver import keep_alive
import requests

channelID = 1000420864103292930
headers = {
    "authorization":
    "OTk5MjU1MTIyODQyNDkyOTgw.GEqdSz.a7knRrguyvdDr-H3ew8F14oiL2Y0Dqx6t6kyy4"
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
