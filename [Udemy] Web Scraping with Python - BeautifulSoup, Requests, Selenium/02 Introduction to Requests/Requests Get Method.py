import requests 

'''MOST COMMONLY USED TYPES OF REQUEST
GET 	- retrieve info
POST 	- send info
'''

url = "https://www.google.com"

response = requests.get(url)

#print(response)
#print(response.content)


'''RESPONSE STATUS CODES
1xx 	- Informational
2xx 	- Success
3xx 	- Redirection
4xx 	- Client Error
5xx 	- Server Error
''' 

print(response.status_code)

'''HEADERS'''

#print(response.headers)
for key, value in response.headers.items():
	print(key, "  ", value)