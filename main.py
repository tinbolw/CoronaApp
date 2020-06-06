import requests

response = requests.get("https://www.worldometers.info/coronavirus/")
status = response.status_code
content = response.text
if response:
    print(status)
    print("Success")
    print(content)
else:
    print(status)
    print("Error: Not found")

