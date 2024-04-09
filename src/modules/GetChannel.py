import requests


def GetChannel(CH_URL: str):
    response = requests.get(CH_URL)
    name: str = str(response.text)
    lines = name.split("\"", -1)

    for Line in lines:
        if Line.find("/@") != -1:
            return str(Line.strip("https://www.youtube.com/@"))
            break
    response.close()
