import json
from os import remove, rename
from modules.Sender import SendReport

report_path: str = "./user/report/"

Hazard_Float: list[float] = [0.0, 0.75, 1.5, 2.25, 3]
Hazard: list[str] = ["low", "moderate", "high", "insane", "EXTREME"]


def ReportChannel(Channel_ID: str,
                  Video_ID: str,
                  Danger: float,
                  Is_Scam: bool,
                  Is_Malware: bool,
                  Message: str,
                  Channel_Name: str):

    for num in range(len(Hazard_Float)):
        if Danger == Hazard_Float[num]:
            Danger: str = Hazard[num]
        else:
            continue

    if Channel_Name == "":
        print("Channel name is None: perhaps the URL is not a valid video")
        return

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

    try:
        rename(f"./{Channel_Name}.json", f"{report_path}{Channel_Name}.json")
        print("Report Created")
        SendReport(File_Name=Channel_Name)
    except Exception:
        print(Exception, "This Report Already Exists\n")
        remove(f"./{Channel_Name}.json")
    finally:
        print("Report Script finished\n")
