import customtkinter as CT
import modules

global Window_Width
global Window_Height

Window_Width = 720
Window_Height = 356

# Colors ====================================================================
BG_Color: str = "#000100100"
Soft_Green_Background: str = "#000200200"
Neon_Green: str = "#0f0"
Black: str = "#000"
Grey: str = "#100100100"

# Backend Funcions ==========================================================


# User Interface ============================================================
def app() -> None:
    app = CT.CTk()
    CT.set_appearance_mode("dark")
    app.configure(fg_color=f"{BG_Color}")
    app.title("No-ScamTubers")
    app.geometry(f"{Window_Width}x{Window_Height}")
    app.minsize(Window_Width, Window_Height)
    app.maxsize(Window_Width, Window_Height)


# Widgets ===================================================================
    Tabs = CT.CTkTabview(master=app,
                         width=Window_Width,
                         height=Window_Height-30,
                         fg_color=f"{BG_Color}",
                         anchor="sw",
                         segmented_button_selected_color=f"{Black}",
                         segmented_button_selected_hover_color=f"{Black}",
                         segmented_button_fg_color=f"{Soft_Green_Background}",
                         segmented_button_unselected_color=f"{Soft_Green_Background}",
                         text_color_disabled="#100100100")

    Tabs.add("Verify")
    Tabs.add("Report")

    class Frame():
        Report_Frame_Left = CT.CTkFrame(master=Tabs.tab("Report"),
                                        width=300,
                                        height=500,
                                        fg_color=f"{Soft_Green_Background}",
                                        border_width=1,
                                        border_color=f"{Neon_Green}")

        Report_Frame_Right = CT.CTkFrame(master=Tabs.tab("Report"),
                                         width=400,
                                         height=500,
                                         fg_color=f"{Soft_Green_Background}",
                                         border_width=1,
                                         border_color=f"{Neon_Green}")

    class Slider():
        Threat_Level = CT.CTkSlider(master=Frame.Report_Frame_Right,
                                    width=10,
                                    height=300,
                                    from_=0,
                                    to=3,
                                    number_of_steps=4,
                                    fg_color="#000",
                                    progress_color="#f00",
                                    button_color="#fff",
                                    orientation="vertical")
        Threat_Level.set(0)

    class TextBox():
        Response_Panel = CT.CTkTextbox(master=Tabs.tab("Verify"),
                                       width=600,
                                       height=600,
                                       fg_color=f"{Soft_Green_Background}",
                                       text_color=f"{Neon_Green}",
                                       state="disabled",
                                       wrap="none")

        Report_Message = CT.CTkTextbox(master=Frame.Report_Frame_Right,
                                       width=600,
                                       height=600,
                                       fg_color=f"{Soft_Green_Background}",
                                       text_color=f"{Neon_Green}",
                                       wrap="none",
                                       border_width=1,
                                       border_color=f"{Neon_Green}")

    class Switch():
        Is_Scam = CT.CTkSwitch(master=Frame.Report_Frame_Left,
                               width=30,
                               height=15,
                               fg_color=f"{Grey}",
                               progress_color="#ff0",
                               text="Is Scam?",
                               text_color="#ff0",
                               button_color="#fff")

        Is_Malware = CT.CTkSwitch(master=Frame.Report_Frame_Left,
                                  width=30,
                                  height=15,
                                  fg_color=f"{Grey}",
                                  progress_color="#f00",
                                  text="Is Malware?",
                                  text_color="#f00",
                                  button_color="#fff")

    class Entrys():
        Link = CT.CTkEntry(master=app,
                           placeholder_text="Video Link",
                           width=680,
                           height=30,
                           border_width=1,
                           corner_radius=13,
                           fg_color=f"{Soft_Green_Background}",
                           placeholder_text_color="#0f0")

    def Report() -> None:
        modules.Report(Channel_Name=modules.GetChannel(Entrys.Link.get()),
                       Link=Entrys.Link.get(),
                       Danger=Slider.Threat_Level.get(),
                       Is_Scam=Switch.Is_Scam.get(),
                       Is_Malware=Switch.Is_Malware.get(),
                       Message=TextBox.Report_Message.get("1.0", CT.END))

    class Buttons():
        Verif_Button = CT.CTkButton(master=Tabs.tab("Verify"),
                                    width=50,
                                    height=25,
                                    corner_radius=3,
                                    fg_color=f"{Soft_Green_Background}",
                                    text="Verify",
                                    text_color=f"{Neon_Green}",
                                    hover_color=f"{Black}")

        Report_Button = CT.CTkButton(master=Frame.Report_Frame_Left,
                                     width=50,
                                     height=25,
                                     corner_radius=3,
                                     fg_color="#c00",
                                     text="Report",
                                     text_color="#fff",
                                     hover_color="#f00",
                                     command=Report)

# Render Widgets ==============================================================
    Entrys.Link.pack(padx=3, pady=3, anchor="n", side="top")
    Tabs.pack(padx=3, pady=3)

    # Verify tab widgets ======================================================
    Buttons.Verif_Button.pack(side="left", padx=10, pady=10, anchor="nw")
    TextBox.Response_Panel.pack(side="right", padx=10, pady=10, anchor="ne")

    # Report tab widgets ======================================================
    Frame.Report_Frame_Left.pack(padx=10, pady=10, anchor="nw", side="left")
    Frame.Report_Frame_Right.pack(padx=10, pady=10, anchor="ne", side="right")
    Buttons.Report_Button.pack(side="top", padx=10, pady=10, anchor="nw")
    Slider.Threat_Level.pack(side="right", padx=10, pady=10, anchor="ne")
    Switch.Is_Scam.pack(side="top", padx=10, pady=10, anchor="nw")
    Switch.Is_Malware.pack(side="left", padx=10, pady=10, anchor="nw")
    TextBox.Report_Message.pack(side="right", padx=0, pady=0, anchor="center")
    app.mainloop()


def main() -> None:
    app()


if __name__ == "__main__":
    main()
