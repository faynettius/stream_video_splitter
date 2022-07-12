set /p vod=Video 1 Name:
set /p splits=Video 2 Name:
set /p name=Name of combined clips:
python video_combiner.py %vod% %splits% %name%