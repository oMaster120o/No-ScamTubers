from socket import socket, AF_INET, SOCK_STREAM

report_path = "./user/report/"
IP: str = ""
PORT: int = 


def SendReport(File_Name: str) -> str:
    print("Starting Sender.py file...")

    with open(f"{report_path}{File_Name}.json", "rb") as Report:
        message: bytes = Report.readline()

        Socket = socket(family=AF_INET, type=SOCK_STREAM)
        try:
            Socket.connect((IP, PORT))

            try:
                Socket.send(message)
            except Exception:
                print(f"Couldn't send Report: {Exception}")
                Socket.close()
                Report.close()

        except Exception:
            print(f"Couldn't connect to {IP, PORT}: {Exception}")
            Socket.close()
            Report.close()

        Socket.close()
        Report.close()
        return
