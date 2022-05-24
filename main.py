from helper import youtube_api
from tkinter import *
import customtkinter
from PIL import Image, ImageTk
import config_parser

# TODO
# - as in test.py create frames for buttons to work
# - figure out better way to display channel icons, maybe get them from somewhere else, not downlaod manually

# FURTHER TODO
# - enable to input your own yt channels
# - some kind of login system
# - liked or marked channels
# - marked watched videos => figure out a way to limit api invocations, save already downloaded data somewhere

API_KEY = config_parser.api_key
ekipa_wk_id = 'UCnvrd6z-UgyX0n-Db7sQI4Q'
wk_dzik_pl_id = 'UCUr1w6sHtgj1JniKV8vWXMw'
warszawski_koks_id = 'UC2AyohFiDUS3K98h5dJVfog'
kuchnia_wk_id = 'UC4TYJ_RcqwL9lAZgkQlk11g'
wk_gaming_id = 'UCeLWHfuhwnObampm0M6oH4w'

debug = True

if not debug:
    yt = youtube_api(API_KEY, warszawski_koks_id, 1)
    yt.get_channel_video_data()

    for vid in yt.videos:
        print(vid)

customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"


class App(customtkinter.CTk):

    WIDTH = 920
    HEIGHT = 720

    def __init__(self):
        super().__init__()

        self.title("Warszawski Koks")
        self.geometry(f"{App.WIDTH}x{App.HEIGHT}")

        self.protocol("WM_DELETE_WINDOW", self.on_closing)  # call .on_closing() when app gets closed

        # =========== read logo images ==============
        image_size = 150
        wk_kuchnia_logo = ImageTk.PhotoImage(Image.open("/Users/krasnowsky/wk_youtube/assets/logos/dzik_kuchnia.jpg").resize((image_size, image_size), Image.ANTIALIAS))
        wk_dzik_logo = ImageTk.PhotoImage(Image.open("/Users/krasnowsky/wk_youtube/assets/logos/dzik_wkdzik.pl.jpg").resize((image_size, image_size), Image.ANTIALIAS))
        wk_gaming_logo = ImageTk.PhotoImage(Image.open("/Users/krasnowsky/wk_youtube/assets/logos/wkgaming.jpg").resize((image_size, image_size), Image.ANTIALIAS))
        ekipa_wk_logo = ImageTk.PhotoImage(Image.open("/Users/krasnowsky/wk_youtube/assets/logos/dzik_ekipawk.jpg").resize((image_size, image_size), Image.ANTIALIAS))
        warszawski_koks_logo = ImageTk.PhotoImage(Image.open("/Users/krasnowsky/wk_youtube/assets/logos/warszawski_koks.jpg").resize((image_size, image_size), Image.ANTIALIAS))

        # ============ create two frames ============

        # configure grid layout (2x1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.frame_left = customtkinter.CTkFrame(master=self,
                                                 width=180,
                                                 corner_radius=0)
        self.frame_left.grid(row=0, column=0, sticky="nswe")

        self.frame_right = customtkinter.CTkFrame(master=self)
        self.frame_right.grid(row=0, column=1, sticky="nswe", padx=20, pady=20)

        # ============ frame_left ============

        # configure grid layout (1x11)
        self.frame_left.grid_rowconfigure(0, minsize=10)   # empty row with minsize as spacing
        self.frame_left.grid_rowconfigure(5, weight=1)  # empty row as spacing
        self.frame_left.grid_rowconfigure(8, minsize=20)    # empty row with minsize as spacing
        self.frame_left.grid_rowconfigure(11, minsize=10)  # empty row with minsize as spacing

        self.label_1 = customtkinter.CTkLabel(master=self.frame_left,
                                              text="Menu",
                                              text_font=("Roboto Medium", -16))  # font name and size in px
        self.label_1.grid(row=1, column=0, pady=10, padx=10)

        self.button_1 = customtkinter.CTkButton(master=self.frame_left,
                                                text="Newest videos",
                                                fg_color=("gray75", "gray30"),  # <- custom tuple-color
                                                command=self.button_event)
        self.button_1.grid(row=2, column=0, pady=10, padx=20)

        self.button_2 = customtkinter.CTkButton(master=self.frame_left,
                                                text="Channels",
                                                fg_color=("gray75", "gray30"),  # <- custom tuple-color
                                                command=self.button_event)
        self.button_2.grid(row=3, column=0, pady=10, padx=20)

        self.switch_2 = customtkinter.CTkSwitch(master=self.frame_left,
                                                text="Dark Mode",
                                                command=self.change_mode)
        self.switch_2.grid(row=10, column=0, pady=10, padx=20, sticky="w")

        # ============ frame_right ============

        # configure grid layout (3x7)
        self.frame_right.rowconfigure((0, 1, 2, 3), weight=1)
        self.frame_right.rowconfigure(7, weight=10)
        self.frame_right.columnconfigure((0, 1), weight=1)
        self.frame_right.columnconfigure(2, weight=0)

        # ============ frame_right ============
        buttons_height = 200

        button_1 = customtkinter.CTkButton(master=self.frame_right, image=wk_gaming_logo, text="WK Gaming", width=130, height=buttons_height, border_width=0,
                                        corner_radius=10, compound="bottom", fg_color=("gray84", "gray25"), hover_color="#C77C78", command=self.button_event
                                        )
        button_1.grid(row=0, column=0, columnspan=1, padx=20, pady=10, sticky="ew")

        button_2 = customtkinter.CTkButton(master=self.frame_right, image=ekipa_wk_logo, text="Ekipa WK", width=130, height=buttons_height, border_width=0,
                                        corner_radius=10, compound="bottom", fg_color=("gray84", "gray25"), hover_color="#C77C78"
                                        )
        button_2.grid(row=0, column=1, columnspan=1, padx=20, pady=10, sticky="ew")

        button_3 = customtkinter.CTkButton(master=self.frame_right, image=warszawski_koks_logo, text="Warszawski Koks", width=130, height=buttons_height, border_width=0,
                                        corner_radius=10, compound="bottom", fg_color=("gray84", "gray25"), hover_color="#C77C78"
                                        )
        button_3.grid(row=1, column=0, columnspan=1, padx=20, pady=10, sticky="ew")

        button_4 = customtkinter.CTkButton(master=self.frame_right, image=wk_kuchnia_logo, text="Kuchnia WK", width=130, height=buttons_height, border_width=0,
                                        corner_radius=10, compound="bottom", fg_color=("gray84", "gray25"), hover_color="#C77C78"
                                        )
        button_4.grid(row=1, column=1, columnspan=1, padx=20, pady=10, sticky="ew")

        button_5 = customtkinter.CTkButton(master=self.frame_right, image=wk_dzik_logo, text="WK DZIK", width=130, height=buttons_height, border_width=0,
                                        corner_radius=10, compound="bottom", fg_color=("gray84", "gray25"), hover_color="#C77C78"
                                        )
        button_5.grid(row=2, column=0, columnspan=1, padx=20, pady=10, sticky="ew")

        self.switch_2.select()

    def button_event(self):
        print("Button pressed")

    def change_mode(self):
        if self.switch_2.get() == 1:
            customtkinter.set_appearance_mode("dark")
        else:
            customtkinter.set_appearance_mode("light")

    def on_closing(self, event=0):
        self.destroy()

    def start(self):
        self.mainloop()


if __name__ == "__main__":
    app = App()
    app.start()