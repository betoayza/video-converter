from moviepy.editor import VideoFileClip
import tkinter as tk
import sys
import os

result = ""


def convert_video(chosen_format):
    global result

    current_dir = os.path.dirname(__file__)  

    video_path = current_dir + "/video/brujula.mp4"
    video_name = video_path[video_path.rindex("/")+1:video_path.rindex(".")]
    clip = VideoFileClip(video_path)
    initial_format = video_path[video_path.index(".")+1:]
    dicc = {1: "avi", 2: "mp4", 3: "mov", 4: "wmv", 5: "mkv", 6: "webm"}

    try:
        chosen_format = int(chosen_format)

        if initial_format == dicc[chosen_format]:
            result = "Can't choice same format!"
            label_result.config(text=result)
        else:
            # result = "Converting..."
            # label_result.config(text=result)

            if chosen_format == 7:
                clip.write_gif(f"{current_dir}/result/gif/{video_name}.gif")
            else:
                clip.write_videofile(
                    f"{current_dir}/result/video/{video_name}.{dicc[chosen_format]}", codec='libx264')

            result = "Successful!"
            label_result.config(text=result)

    except ValueError:
        result = "Error: you have to choice a valid option!"
        label_result.config(text=result)

# tkinter: la parte grafica
root = tk.Tk()
root.title("Super Video Converter")

frame = tk.Frame(root, bd=2, bg="#c9c0bb")
frame.pack()

label_title = tk.Label(frame, text="Welcome to Super Video Converter!", font=(
    "Arial", 18), bg="#c4aead")
label_title.pack()
label_options = '''
    Choose format to convert:
    -------------------------
    1.    AVI
    2.    MP4
    3.    MOV
    4.    WMV
    5.    MKV
    6.    WEBM
    7.    GIF

    Select:'''
label_options = tk.Label(frame, text=label_options, bg="#bfc1c2")

entry = tk.Entry(frame)
entry.config(font=('Arial', 12), width=7, bg="#004953", fg="white")

btn_convert = tk.Button(frame, text="Convert!", command=lambda: convert_video(
    entry.get()))

label_result = tk.Label(frame, text="", bg="black", fg="white")

btn_exit = tk.Button(frame, text="Exit", command=root.quit)

# ubicar elementos en grilla
label_title.grid(row=0, columnspan=4)
label_options.grid(row=1, columnspan=4)
entry.grid(row=2, column=2, padx=0, pady=0)
btn_convert.grid(row=3, column=2, padx=0, pady=0)
label_result.grid(row=4, column=2, padx=0, pady=0)
btn_exit.grid(row=5, column=3, padx=0)

# mostrar ventana
root.mainloop()
# exit program4
print("Thanks for try me, see on next time!")
sys.exit()
