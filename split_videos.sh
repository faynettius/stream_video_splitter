read -p 'Twitch VoD name: ' vod
read -p 'Split file: ' splits
read -p 'Name of Tournament: ' name
python video_splitter.py $vod $splits $name
