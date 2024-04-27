import requests

Replaces: list[str] = ["/channel/", "/about/", "/video", "/video/"]


def GetChannel(CH_URL: str):
    response = requests.get(CH_URL)
    name: str = str(response.text)
    lines = name.split("\"", -1)
    response.close()

# https://www.youtube.com/watch?v=GOeKo-uioXc
# Channel id: UCJ4BgU996P32qwkUXN73drQ
    VID_ID: str = CH_URL.strip("https://www.youtube.com/watch?v=")
    CH_ID: str = ""
    print("Scanning URL")
    for Line in lines:
        if CH_ID == "" and Line.find("/channel/") != -1:
            CH_ID: str = Line
            for word in Replaces:
                CH_ID: str = CH_ID.replace(word, "")

    return CH_ID, VID_ID
