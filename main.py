from helper import youtube_api
from tkinter import *
import customtkinter
from PIL import Image, ImageTk

API_KEY = 'AIzaSyC-nrN3dQG2myUiOVRW7uOeCMib-YnJ344'
ekipa_wk_id = 'UCnvrd6z-UgyX0n-Db7sQI4Q'
wk_dzik_pl_id = 'UCUr1w6sHtgj1JniKV8vWXMw'
warszawski_koks_id = 'UC2AyohFiDUS3K98h5dJVfog'
kuchnia_wk_id = 'UC4TYJ_RcqwL9lAZgkQlk11g'
wk_gaming_id = 'UCeLWHfuhwnObampm0M6oH4w'

'''yt = youtube_api(API_KEY, ekipa_wk_id, 1)
yt.get_channel_video_data()

for vid in yt.videos:
    print(vid)'''

customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

app = customtkinter.CTk()  # create CTk window like you do with the Tk window
app.geometry("800x600")

def button_function():
    print("button pressed")

# load images as PhotoImage
image_size = 20

add_user_image = ImageTk.PhotoImage(Image.open("/Users/krasnowsky/wk_youtube/assets/logos/wkgaming.jpg"))


app.grid_rowconfigure(0, weight=1)
app.grid_columnconfigure(0, weight=1, minsize=200)

frame_1 = customtkinter.CTkFrame(master=app, width=250, height=240, corner_radius=15)
frame_1.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")

frame_1.grid_columnconfigure(0, weight=1)
frame_1.grid_columnconfigure(1, weight=1)
frame_1.grid_rowconfigure(0, minsize=10)  # add empty row for spacing

button_5 = customtkinter.CTkButton(master=app, image=add_user_image, text="WK Gaming", width=130, height=70, border_width=3,
                                   corner_radius=10, compound="bottom", border_color="#D35B58", fg_color=("gray84", "gray25"), hover_color="#C77C78",
                                   command=button_function)
button_5.grid(row=0, column=0, padx=20, pady=20)

app.mainloop()