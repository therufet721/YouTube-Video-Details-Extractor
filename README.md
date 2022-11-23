# YouTube Video Data Scraper

This repository contains a Python script to extract data from YouTube videos using the YouTube Data API v3. It fetches video data from a specified YouTube channel and writes it to a JSON file.

## Requirements

This script requires Python 3.7 or later. The following Python packages are also required:

- google-api-python-client
- google-auth
- google-auth-httplib2
- google-auth-oauthlib

These can be installed via pip using the command: `pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib`

## Usage

1. First, replace the `api_key` variable in the script with your own YouTube Data API key. If you do not have an API key, you can obtain one from the [Google Cloud Console](https://console.developers.google.com/).

2. Replace the `channel_id` variable in the script with the ID of the YouTube channel you wish to scrape data from. You can find the channel ID by visiting the YouTube channel in a web browser and checking the URL, or you can use a tool such as the [YouTube Channel ID Finder](https://commentpicker.com/youtube-channel-id.php).

3. Run the script. It will fetch data for all the videos in the specified channel's "uploads" playlist, including the title and description of each video. This data is then written to a JSON file named `video_data.json`.

## Output

The output JSON file contains an array of objects, each representing a video. Each object has the following structure:

```json
{
    "title": "Video Title",
    "description": "Video description..."
}
```

## Disclaimer

This code is intended for personal use and should be used responsibly, in compliance with YouTube's Terms of Service and the YouTube Data API's usage policies. The developer is not responsible for any misuse of this code or any violations of these terms.


## License

This project is licensed under the [MIT](https://choosealicense.com/licenses/mit/).

