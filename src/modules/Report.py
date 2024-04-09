import json


def Report(Channel_Name: str, Link: str, Danger: int, Is_Scam: bool, Is_Malware: bool, Message: str):

    Report_File: dict = {
            "name": f"{Channel_Name}",
            "link": f"{Link}",
            "danger": Danger,
            "scam": Is_Scam,
            "malware": Is_Malware,
            "message": f"{Message}"
            }
    with open(f"{Channel_Name}.json", "w") as report:
        json.dump(Report_File, report)
        report.close()

    return "Report Created"
