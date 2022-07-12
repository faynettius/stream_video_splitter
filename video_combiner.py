from moviepy.editor import VideoFileClip, concatenate_videoclips
import sys
# Usage
# python video_combiner.py vod1.mp4 vod2.mp4 combined_name.mp4

clip1 = VideoFileClip(sys.argv[1])
clip2 = VideoFileClip(sys.argv[2])
final_clip= concatenate_videoclips([clip1,clip2])
final_clip.write_videofile(sys.argv[3])
