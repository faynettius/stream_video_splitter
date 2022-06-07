from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
import os
import sys

def change_to_seconds(time_format):
    smh = [1,60,3600]
    time_list = time_format.split(":")
    smh = smh[:len(time_list)]
    smh.reverse()
    total_seconds = 0
    for i,t in enumerate(time_list):
        total_seconds += int(t)*smh[i]
    return total_seconds

if "clips" not in os.listdir(os.getcwd()):
    os.mkdir("clips")

mp4_file =   "TLT36.mp4"
split_file = "TLT36.txt"
# Accept arguments
if len(sys.argv) > 2:
    mp4_file = sys.argv[1]
    split_file = sys.argv[2]
# Add tourney name
tourney_name = ""
if len(sys.argv) > 3:
    tourney_name = sys.argv[3]

with open(split_file) as f:
    doc = f.read()
lines = doc.split("\n")
old_time = 0
for n, line in enumerate(lines):
    print(line)
    split_line = line.split("_")
    times = split_line[0]
    vod_name = split_line[1].strip()
    if len(tourney_name) > 0:
        vod_name = tourney_name + " " + vod_name
    both_times = times.strip().split("-")
    span = [change_to_seconds(both_times[0]), change_to_seconds(both_times[1])]
    print(span)

    ffmpeg_extract_subclip(mp4_file, span[0], span[1], targetname= "clips/" + vod_name+".mp4")
