# importing the requests library
import requests

# defining the api-endpoint
API_ENDPOINT = "https://api.groupme.com/v3/bots/post"

# your API key here
API_KEY = "XXXXXXXXXXXXXXXXX"

# your source code here
source_code = '''
print("Hello, world!")
a = 1
b = 2
print(a + b)
'''

# data to be sent to api
data = {
  "bot_id"  : "da96ef27fe192e9049930c41bf",
  "text"    : "Hmmm, looks like my thought process will be built in Python. I'm excited to meet this Snek!"
}

# sending post request and saving response as response object
r = requests.post(url = API_ENDPOINT, data = data)

# extracting response text
# pastebin_url = r.text
# print("The pastebin URL is:%s"%pastebin_url)
