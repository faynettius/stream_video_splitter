# Instructions for low-tech folks

**0.** Hit `Windows + R` and type in `powershell`, then hit enter. Type `python` and hit enter. Download whatever shows up. If this doesn't work, go download python manually from https://www.python.org/downloads/

**1.** Download the VoD via twitch leecher which you can download here: https://github.com/Franiac/TwitchLeecher/releases

**2.** Download this https://github.com/faynettius/stream_video_splitter , and also run the following on your command line from step 0

```
pip install ffmpeg
pip install moviepy
```
**If that that doesn't work**, run
```
python -m pip install ffmpeg
python -m pip install moviepy
```

**3.** Go through the VoD and note down the times and filename as follows:

`[time1]-[time2]_[Video Name]`

e.g. `12:45-17:22_Winner's Side smub vs ZD`

There is an example file called `example_splits.txt` you can look at for help.

I recommend you use VLC media (https://www.videolan.org/vlc/) player to do this, you can skip through the VOD with the arrow keys, and use `Ctrl + [Arrow Key]` to move 1 minute at a time (useful for finding the end of a match)

**4.** Once you have the split file and the video file, run the `split_videos.bat` and type in the information it asks for. It should ask for the name of the VoD file, the splits file, and the name of the tournament. You can tab-complete these fields (type in the first few letters of the file you want, then hit `TAB` and it will fill the rest in)

**5.** If you do this all correctly, it should populate the `clips` folder with your vods, split to the times you input for the splits file.

# Instructions for code-savvy folks

```
git clone https://github.com/faynettius/stream_video_splitter.git
cd stream_video_splitter
pip install -r requirements.txt
```

See steps 3 and 4 above for how to use the splitter
