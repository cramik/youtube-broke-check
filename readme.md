Checks for dead youtube channels by using the python-youtube wrapper for YouTube's API

Tested with both terminated and deleted channels

Good for keeping track of at-risk YouTube channels (especially when paired with a backup script)

Necessary installation tips:
1. pip install --upgrade python-youtube
2. Get API key from https://console.developers.google.com/
3. If the channel you want to track is in the form /c/channelname, either use https://commentpicker.com/youtube-channel-id.php or Inspect Element -> Ctrl+F -> canonical till you see `link rel="canonical" href="https://www.youtube.com/channel/UC..."`
