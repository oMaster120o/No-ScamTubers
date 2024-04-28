import json
from os import remove, rename

report_path: str = "./user/report/"


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
        report.close()

    rename(f"./{Channel_Name}.json", f"{report_path}{Channel_Name}.json")
    try:
        print("Report Created")
    except Exception:
        print(Exception, "This Report Already Exists\n")
        remove(f"./{Channel_Name}.json")
    finally:
        return print("Report Script finished\n")
