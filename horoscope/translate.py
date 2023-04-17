import requests

url = "https://microsoft-translator-text.p.rapidapi.com/translate"

querystring = {"to[0]":"ru","api-version":"3.0","profanityAction":"NoAction","textType":"plain"}


def translate(input_text: str):
    payload = [{"Text": input_text}]
    headers = {
        "content-type": "application/json",
        "X-RapidAPI-Key": "6008c5edc4msh1d654540d19737fp1dc20bjsn5a68576504f9",
        "X-RapidAPI-Host": "microsoft-translator-text.p.rapidapi.com"
    }

    response = requests.request("POST", url, json=payload, headers=headers, params=querystring)
    return response.json()[0]['translations'][0]['text']


print(translate('Translates input text, returning translated text'))
