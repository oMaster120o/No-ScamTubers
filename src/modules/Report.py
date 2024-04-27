import json


def ReportChannel(Channel_ID: str, Video_ID: str, Danger: int, Is_Scam: bool, Is_Malware: bool, Message: str):

    Report_File: dict = {
            "ch_id": f"{Channel_ID}",
            "vid_id": f"{Video_ID}",
            "danger": Danger,
            "scam": Is_Scam,
            "malware": Is_Malware,
            "message": f"{Message}"
            }
    with open(f"{Channel_ID}.json", "w") as report:
        json.dump(Report_File, report)
        print("Report Created")
        report.close()
