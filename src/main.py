import customtkinter as CT

global Window_Width
global Window_Height

Window_Width = 720
Window_Height = 356

# Colors ====================================================================
BG_Color: str = "#000100100"
Soft_Green_Background: str = "#000200200"
Neon_Green: str = "#0f0"
Black: str = "#000"

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

    class Entrys():
        Link = CT.CTkEntry(master=app,
                           placeholder_text="Video Link",
                           width=680,
                           height=30,
                           border_width=1,
                           corner_radius=13,
                           fg_color=f"{Soft_Green_Background}",
                           placeholder_text_color="#0f0")

    class Buttons():
        Verif_Button = CT.CTkButton(master=Tabs.tab("Verify"),
                                    width=50,
                                    height=25,
                                    corner_radius=3,
                                    fg_color=f"{Soft_Green_Background}",
                                    text="Verify",
                                    text_color=f"{Neon_Green}",
                                    hover_color=f"{Black}")

    class TextBox():
        Response_Panel = CT.CTkTextbox(master=Tabs.tab("Verify"),
                                       width=600,
                                       height=600,
                                       fg_color=f"{Soft_Green_Background}",
                                       text_color=f"{Neon_Green}",
                                       state="disabled",
                                       wrap="none")
# Render Widgets ==============================================================

    Entrys.Link.pack(padx=10, pady=3)
    Tabs.pack(padx=3, pady=3)
    Buttons.Verif_Button.pack(side="left", padx=10, pady=10, anchor="nw")
    TextBox.Response_Panel.pack(side="right", padx=10, pady=10, anchor="ne")
    app.mainloop()

def main() -> None:
    app()


if __name__ == "__main__":
    main()
