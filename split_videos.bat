set /p vod=Twitch vod name:
set /p splits=Split file:
set /p name=Name of Tournament:
python video_splitter.py %vod% %splits% %name%