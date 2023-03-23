from moviepy.editor import VideoFileClip

video_path = "video/brujula.mp4"
video_name = video_path[video_path.rindex("/")+1:video_path.rindex(".")]
clip = VideoFileClip(video_path)
initial_format = video_path[video_path.index(".")+1:]
dicc = {1: "avi", 2: "mp4", 3: "mov", 4: "wmv", 5: "mkv", 6: "webm"}
is_finished = False

print("\nWelcome to the Video Converter!\n\nThe initial format is:", initial_format)

while not is_finished:
    try:
        chosen_format = int(input("""
            Choose format to convert:
            ------------------
            1.    AVI
            2.    MP4
            3.    MOV
            4.    WMV
            5.    MKV
            6.    WEBM
            7.    GIF

            Select: """))

        if chosen_format == 7:
            clip.write_gif(f"result/gif/{video_name}.gif")
            break
        if initial_format == dicc[chosen_format]:
            print("\nCan't choice same format!")
            continue

        clip.write_videofile(
            f"result/video/{video_name}.{dicc[chosen_format]}", codec='libx264')

        is_finished = True
    except ValueError:
        print("\nYou have to choice a valid option!")

print("\nConversion successful! Thanks for try me, see on next time!")
