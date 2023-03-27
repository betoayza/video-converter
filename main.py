from moviepy.editor import VideoFileClip
import tkinter as tk
import sys
import os
from tkinter import filedialog

result = ""
video_path = ""


def open_file():
    global video_path

    video_path = filedialog.askopenfilename()
    label_video_path.config(text="File: " + video_path)


def convert_video(chosen_format):
    global result
    global video_path

    current_dir = os.path.dirname(__file__)

    try:
        video_name = video_path[video_path.rindex(
            "/")+1:video_path.rindex(".")]
        clip = VideoFileClip(video_path)
        initial_format = video_path[video_path.index(".")+1:]
        dict_options = {1: "avi", 2: "mp4", 3: "mov",
                        4: "wmv", 5: "mkv", 6: "webm", 7: "gif"}

        chosen_format = int(chosen_format)

        if initial_format == dict_options[chosen_format]:
            result = "Can't choice same format!"
            label_result.config(text=result, fg="red")

        else:
            result = "Converting..."
            label_result.config(text=result)

            if chosen_format == 6:
                clip.write_videofile(
                    f"{current_dir}/result/video/{video_name}.{dict_options[chosen_format]}", codec='libvpx', audio_codec='libvorbis')

            elif chosen_format == 7:
                clip.write_gif(f"{current_dir}/result/gif/{video_name}.gif")

            else:
                clip.write_videofile(
                    f"{current_dir}/result/video/{video_name}.{dict_options[chosen_format]}", codec='libx264')

            result = "Successful!"
            label_result.config(text=result, fg="yellowgreen")

    except ValueError:
        if video_path == "":
            result = "Error: you did not choice a video!"
            label_result.config(text=result, fg="red")
        else:
            result = "Error: you didn't have to choice a valid option!"
            label_result.config(text=result, fg="red")
    except IOError:
        result = "Error: something went wrong with codecs :/"
        label_result.config(text=result, fg="red")


# tkinter: gui
root = tk.Tk()
root.title("Super Video Converter")

frame = tk.Frame(root, bd=2, bg="#c9c0bb")
frame.pack()

# menu
menu_bar = tk.Menu(root, bg="black", fg="white")

file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Open...", command=lambda: open_file())
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

menu_bar.add_cascade(label="File", menu=file_menu)
root.config(menu=menu_bar)


# Labels, buttons, etc
label_title = tk.Label(frame, text="Welcome to Super Video Converter!", font=(
    "Arial", 18), bg="#c4aead")
label_video_path = tk.Label(frame, text="")
label_options = """Choose format to convert:
-------------------------
1.    AVI
2.    MP4
3.    MOV
4.    WMV
5.    MKV
6.    WEBM
7.    GIF

Select:"""

label_options = tk.Label(frame, text=label_options, bg="#bfc1c2", fg="maroon")

entry = tk.Entry(frame)
entry.config(font=('Arial', 12), width=7, bg="#004953", fg="white")

btn_convert = tk.Button(frame, text="Convert!", command=lambda: convert_video(
    entry.get()))

label_result = tk.Label(frame, text="", bg="black", fg="white")

# grid
label_title.grid(row=1, columnspan=4)
label_video_path.grid(row=2, columnspan=4, padx=1, pady=5)
label_options.grid(row=3, columnspan=4)
entry.grid(row=4, column=2, padx=0, pady=0)
btn_convert.grid(row=5, column=2, padx=0, pady=0)
label_result.grid(row=6, column=2, padx=0, pady=0)

# display gui
root.mainloop()
# exit program
print("Thanks for try me, see on next time!")
sys.exit()
