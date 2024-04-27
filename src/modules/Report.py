import json
from shutil import move
from os import remove


def ReportChannel(Channel_ID: str,
                  Video_ID: str,
                  Danger: int,
                  Is_Scam: bool,
                  Is_Malware: bool,
                  Message: str,
                  Channel_Name: str):

    Report_File: dict = {
            "ch_name": f"{Channel_Name}",
            "ch_id": f"{Channel_ID}",
            "vid_id": f"{Video_ID}",
            "danger": Danger,
            "scam": Is_Scam,
            "malware": Is_Malware,
            "message": f"{Message}"
            }
    with open(f"{Channel_Name}.json", "w") as report:
        json.dump(Report_File, report)
        print("Report Created")
        report.close()
    try:
        move(f"./{Channel_Name}.json", "./user/report/")
    except Exception:
        print(Exception, "This Report Already Exists\n")
        remove(f"./{Channel_Name}.json")
    finally:
        return print("Report Script finished\n")
