import customtkinter as CT
import modules
from threading import Thread
from modules.Server import Listen, ServerClose

global Window_Width
global Window_Height
global Threat

Window_Width = 720
Window_Height = 356

# Colors ====================================================================
BG_Color: str = "#000100100"
Soft_Green_Background: str = "#000200200"
Neon_Green: str = "#0f0"
Black: str = "#000"
Grey: str = "#100100100"


# Backend Funcions ==========================================================
class Server():
    def Connect():
        return Listen()

    def Close():
        return ServerClose()

    def Start():
        if Server.Connect():
            Thread(target=Server.Close()).start()


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

    # Widgets ===================================================================
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
                                        fg_color=f"{Soft_Green_Background}",
                                        text_color=f"{Neon_Green}",
                                        border_color="#0ef",
                                        border_width=1,
                                        state="disabled",
                                        wrap="none")

        self.Report_Message = CT.CTkTextbox(master=self.Report_Frame_Right,
                                            width=555,
                                            height=270,
                                            fg_color="#200200000",
                                            text_color="#ff0",
                                            wrap="none",
                                            border_width=1,
                                            border_color="#ff0")

        self.Listener = CT.CTkSwitch(master=self.Top_Frame,
                                     width=30,
                                     height=29,
                                     fg_color="#f00",
                                     progress_color=f"{Neon_Green}",
                                     button_color="#fff",
                                     text="Listener",
                                     text_color="#fff")

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

        def Report() -> None:
            print("EEEEEEEEEEEEEE")

        self.View_Button = CT.CTkButton(master=self.Top_Frame,
                                        width=50,
                                        height=25,
                                        corner_radius=3,
                                        fg_color=f"{Soft_Green_Background}",
                                        text="View",
                                        text_color=f"{Neon_Green}",
                                        hover_color=f"{Black}")

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

        # Render Widgets ==============================================================
        self.Top_Frame.place(x=1, y=1)
        self.Listener.place(x=1, y=1)
        self.Tabs.place(x=1, y=40)

        # View tab widgets ======================================================
        self.View_Panel.place(x=1, y=1)
        # Report tab widgets ======================================================
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
