from moviepy.editor import VideoFileClip
import tkinter as tk
import sys, os

result = ""


def convert_video(chosen_format):
    global result

    current_dir = os.path.dirname(__file__)
    print("ASD:", chosen_format)

    video_path = current_dir + "/video/brujula.mp4"
    video_name = video_path[video_path.rindex("/")+1:video_path.rindex(".")]
    clip = VideoFileClip(video_path)
    initial_format = video_path[video_path.index(".")+1:]
    dicc = {1: "avi", 2: "mp4", 3: "mov", 4: "wmv", 5: "mkv", 6: "webm"}
    is_finished = False

    try:
        chosen_format = int(chosen_format)

        if chosen_format == 7:
                clip.write_gif(f"{current_dir}/result/gif/{video_name}.gif")

        elif initial_format == dicc[chosen_format]:
            result = "Can't choice same format!"

        else:
             clip.write_videofile(
                f"{current_dir}/result/video/{video_name}.{dicc[chosen_format]}", codec='libx264')

             result = "Successful!"
    except ValueError:
        result = "Error: you have to choice a valid option!"



# la parte grafica
screen = tk.Tk()
screen.title("Super Video Converter")
screen.geometry("600x480")
label_title = tk.Label(screen, text="Welcome to Super Video Converter!")
label_title.pack()
text_options = """
    Choose format to convert:
    ------------------
        1.    AVI
        2.    MP4
        3.    MOV
        4.    WMV
        5.    MKV
        6.    WEBM
        7.    GIF

        Select:"""
label_options = tk.Label(screen, text=text_options)
label_options.pack()
chose_option = tk.Text(screen, width=7, height=2)
chose_option.insert("1.0", "")
chose_option.pack()
btn_convert = tk.Button(screen, text="Convert!",
                        command=lambda: convert_video(chose_option.get("1.0", tk.END)))
btn_convert.pack()
label_result = tk.Label(screen, text=result)
btn_exit=tk.Button(screen, text = "Exit", command = screen.quit)
btn_exit.pack()
# mostrar ventana
screen.mainloop()
# exit program
print("Thanks for try me, see on next time!")
sys.exit()
