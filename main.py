from webserver import keep_alive
import requests

channelID = 1210823070458056745
headers = {
    "AUTHOIRIZATION":
    "MTExNzgzMDk4NTQ3Njc1MTQ3MA.GoH-Fk.tohiJ4mMpknz89gdiA0z9mnjHNAZGG9xxcpCJU"
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
