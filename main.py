import tkinter as tk
import tkinter.ttk as ttk
import subprocess
import urllib.request
from PIL import Image, ImageTk
import io
stdin_parameter = subprocess.PIPE
window = tk.Tk()
window.title("YouTube Downloader")
window.geometry("800x400")
window.resizable(False, False)
label = tk.Label(window, text="")
image_label = tk.Label(window)
image_label.pack()
def download():
    video_id = get_video_id(entry.get())
    image_url = f"https://img.youtube.com/vi/{video_id}/maxresdefault.jpg"
    image_data = urllib.request.urlopen(image_url).read()
    image = Image.open(io.BytesIO(image_data))
    image = image.resize((341, 192))
    image = ImageTk.PhotoImage(image)
    image_label.config(image=image)
    image_label.image = image
    image_label.pack(side="bottom")
    subprocess.run(["yt-dlp", entry.get()],shell=True)
    label.config(text="Download Complete")
    window.after(5000, delete_message)
def delete_message():
    label.config(text="")
def get_video_id(url):
    return url.split("=")[-1]
entry = tk.Entry(window, width=80)
entry.pack()
button = tk.Button(window, text="Download", command=download)
button.pack()
label.pack()
label = tk.Label(window, text="hdoori", font=("Helvetica", 8))
label.pack(side="bottom", anchor="w")
window.mainloop()