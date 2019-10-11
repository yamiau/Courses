import requests
from fake_useragent import UserAgent

#Background on User Agents

ua = UserAgent()

header ={"user-agent" : ua.chrome}

print(ua.chrome)

page = requests.get("https://google.com", headers = header)

print(page.content)


#Background on Timeout