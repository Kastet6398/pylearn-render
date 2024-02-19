import requests

url = 'https://api.languagetoolplus.com/v2/check'
headers = {
    'accept': 'application/json',
    'Content-Type': 'application/x-www-form-urlencoded',
}

data = {
    'text': 'Hii, rorld! Hello,, world!',
    'language': 'en-US',
    'enabledOnly': 'false',
    'level': 'picky',
}

for i in range(40):
    response = requests.post(url, headers=headers, data=data)

    if response.status_code == 200:
        parsed_data = response.json()

        matches = parsed_data['matches']

        formatted_matches = []

        for i in matches:
            formatted_matches.append({
                "message": i["message"],
                "shortMessage": i["shortMessage"],
                "replacements": [j["value"] for j in i["replacements"][:5]],
                "context": i["context"]["text"][i["context"]["offset"]:i["context"]["offset"] + i["context"]["length"]]
            })

        print(formatted_matches)
    else:
        print(f"Error: {response.status_code}, {response.text}")
