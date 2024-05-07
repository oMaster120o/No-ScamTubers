import customtkinter as CT
import modules
from os import path, makedirs

global Window_Width
global Window_Height

Window_Width = 720
Window_Height = 356

if not path.exists("./user/report/"):
    makedirs("./user/report/")


# Colors ====================================================================
BG_Color: str = "#000100100"
Soft_Green_Background: str = "#000200200"
Neon_Green: str = "#0f0"
Black: str = "#000"
Grey: str = "#100100100"


# User Interface ============================================================
class App(CT.CTk):
    def __init__(self):
        super().__init__()
        CT.set_appearance_mode("dark")
        self.configure(fg_color=f"{BG_Color}")
        self.title("No-ScamTubers")
        self.geometry(f"{Window_Width}x{Window_Height}")
        self.minsize(Window_Width, Window_Height)
        self.maxsize(Window_Width, Window_Height)

    # Widgets ================================================================
        self.Tabs = CT.CTkTabview(master=self,
                                  width=Window_Width,
                                  height=Window_Height-30,
                                  fg_color=f"{BG_Color}",
                                  anchor="sw",
                                  segmented_button_selected_color=f"{Black}",
                                  segmented_button_selected_hover_color=f"{Black}",
                                  segmented_button_fg_color=f"{Soft_Green_Background}",
                                  segmented_button_unselected_color=f"{Soft_Green_Background}",
                                  text_color_disabled="#100100100")

        self.Tabs.add("View")
        self.Tabs.add("Report")

        self.Top_Frame = CT.CTkFrame(master=self,
                                     width=Window_Width-3,
                                     height=33,
                                     fg_color=f"{Soft_Green_Background}",
                                     border_width=1,
                                     border_color=f"{Neon_Green}")

        self.Report_Frame_Left = CT.CTkFrame(master=self.Tabs.tab("Report"),
                                             width=110,
                                             height=100,
                                             fg_color="#200000000",
                                             border_width=1,
                                             border_color="#f00")

        self.Report_Frame_Right = CT.CTkFrame(master=self.Tabs.tab("Report"),
                                              width=585,
                                              height=270,
                                              fg_color=f"{Soft_Green_Background}",
                                              border_width=1,
                                              border_color=f"{Neon_Green}")

        self.Threat_Level = CT.CTkSlider(master=self.Report_Frame_Right,
                                         width=20,
                                         height=260,
                                         from_=0,
                                         to=3,
                                         number_of_steps=4,
                                         fg_color="#000",
                                         progress_color="#f00",
                                         button_color="#fff",
                                         orientation="vertical")
        self.Threat_Level.set(0)

        self.View_Panel = CT.CTkTextbox(master=self.Tabs.tab("View"),
                                        width=700,
                                        height=270,
                                        fg_color="#000100100",
                                        text_color="#0ff",
                                        border_color="#0ef",
                                        border_width=1,
                                        state="normal",
                                        wrap="none")

        self.Report_Message = CT.CTkTextbox(master=self.Report_Frame_Right,
                                            width=555,
                                            height=270,
                                            fg_color="#200200000",
                                            text_color="#ff0",
                                            wrap="none",
                                            border_width=1,
                                            border_color="#ff0")

        self.URL_Field = CT.CTkEntry(master=self.Top_Frame,
                                     width=400,
                                     height=30,
                                     fg_color=f"{Soft_Green_Background}",
                                     text_color="#ff0",
                                     border_width=1,
                                     border_color="#ff0")

        self.Is_Scam = CT.CTkSwitch(master=self.Report_Frame_Left,
                                    width=30,
                                    height=15,
                                    fg_color=f"{Grey}",
                                    progress_color="#ff0",
                                    text="Scam?",
                                    text_color="#ff0",
                                    button_color="#fff")

        self.Is_Malware = CT.CTkSwitch(master=self.Report_Frame_Left,
                                       width=30,
                                       height=15,
                                       fg_color=f"{Grey}",
                                       progress_color="#f00",
                                       text="Malware?",
                                       text_color="#f00",
                                       button_color="#fff")

        def Verify() -> None:
            URL: str = self.URL_Field.get()
            URL: str = URL.strip()
            self.View_Panel.delete("0.0", "end")

            self.View_Panel.configure(border_color="#0ef")
            self.View_Panel.configure(fg_color="#000100100")
            self.View_Panel.configure(text_color="#0ff")

            if URL.find("https://www.youtube.com/watch?v=") == 0:
                self.View_Panel.insert(CT.END, "Valid URL\n")

                if modules.Verify(URL) == "Found":
                    self.View_Panel.insert(CT.END, "This Channel has been detected on the list\n no matter what happens or what he says\n do NOT trust him in any ocasion\n\n<The Report Feature is still being developed>")
                    self.View_Panel.configure(border_color="#f00")
                    self.View_Panel.configure(fg_color="#100000000")
                    self.View_Panel.configure(text_color="#f00")

                else:
                    self.View_Panel.insert(CT.END, "Channel Not found in the list\n Be Careful Anyway")
            else:
                self.View_Panel.insert(CT.END, "Invalid URL: must be similar to that one: https://www.youtube.com/watch?v=dQw4w9WgXcQ")

        self.Verify_Button = CT.CTkButton(master=self.Top_Frame,
                                          width=50,
                                          height=30,
                                          corner_radius=3,
                                          fg_color=f"{Black}",
                                          text="Verify",
                                          text_color=f"{Neon_Green}",
                                          border_color="#ff0",
                                          hover_color="#0aa",
                                          command=Verify)

        def Report() -> None:
            URL: str = self.URL_Field.get()
            URL: str = URL.strip()

            if URL.find("https://www.youtube.com/watch?v=") == 0:
                print("Valid URL")

                CH_ID, VID_ID, CH_Name = modules.GetChannel(URL)
                modules.ReportChannel(Channel_ID=CH_ID,
                                      Video_ID=VID_ID,
                                      Danger=self.Threat_Level.get(),
                                      Is_Scam=self.Is_Scam.get(),
                                      Is_Malware=self.Is_Malware.get(),
                                      Message=self.Report_Message.get("1.0", CT.END),
                                      Channel_Name=CH_Name)
            else:
                return print("Invalid URL")

        self.Report_Button = CT.CTkButton(master=self.Report_Frame_Left,
                                          width=50,
                                          height=25,
                                          corner_radius=3,
                                          fg_color="#a00",
                                          text="Report",
                                          text_color="#fff",
                                          hover_color="#f00",
                                          border_color="#f00",
                                          command=Report)

        # Render Widgets ======================================================
        self.Top_Frame.place(x=1, y=1)
        self.URL_Field.place(x=100, y=1)
        self.Verify_Button.place(x=660, y=1)
        self.Tabs.place(x=1, y=40)

        # View tab widgets ====================================================
        self.View_Panel.place(x=1, y=1)
        # Report tab widgets ==================================================
        self.Report_Frame_Left.place(x=1, y=1)
        self.Report_Frame_Right.place(x=120, y=1)
        self.Report_Button.place(x=30, y=65)
        self.Is_Scam.place(x=3, y=5)
        self.Is_Malware.place(x=3, y=35)
        self.Threat_Level.place(x=560, y=1)
        self.Report_Message.place(x=0, y=0)


def main() -> None:
    app = App()
    app.mainloop()


if __name__ == "__main__":
    main()
