from modules import GetChannel
import requests


def Verify(YT_URL: str) -> str:
    CH_ID, VID_ID, CH_Name = GetChannel(YT_URL)
    CH_ID: str = CH_ID
    response = requests.get("https://github.com/Incrypters/YT-ScamDatabase/blob/main/Scam_IDs.JSON")
    response.close()

    Data: str = str(response.text).split(r'\r","    \"', -1)
    for line in range(len(Data)):

        if line > 0 and Data[line].startswith("UC") and Data[line].endswith(","):

            if Data[line][0:24] == CH_ID:
                print(CH_ID)
                print("The Line: ", Data[line])
                return "Found"
            else:
                continue
        else:
            continue
    return "Not Found"
