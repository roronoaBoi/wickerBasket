import requests
import json

print('paste the api bearer token')
token = input()

url = "https://api.safetyculture.io/feed/users"
headers = {
    "accept": "application/json",
    "sc-integration-id": "sc-readme",
    "Authorization": "Bearer " + token
}
response = requests.get(url, headers=headers)
cleaned = json.loads(response.text)
toRead = json.dumps(cleaned, indent = 4)
print(toRead)

# simple example. need to do the equivalent of a PUSH to a list...
# {
#   "metadata": {
#     "next_page": null,
#     "remaining_records": 0
#   },
#   "data": []
# }
# example
# while response.metadata.next_page:
    # update url