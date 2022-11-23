import json
from googleapiclient.discovery import build


api_key = "Your_API"
youtube = build("youtube", "v3", developerKey=api_key)

# find it with this website https://commentpicker.com/youtube-channel-id.php
channel_id = "Your Channel ID"

channels_response = (
    youtube.channels().list(part="contentDetails", id=channel_id).execute()
)
uploads_playlist_id = channels_response["items"][0]["contentDetails"][
    "relatedPlaylists"
]["uploads"]

videos = []
next_page_token = None
while True:
    playlist_items_response = (
        youtube.playlistItems()
        .list(
            part="snippet",
            playlistId=uploads_playlist_id,
            maxResults=50,
            pageToken=next_page_token,
        )
        .execute()
    )

    for item in playlist_items_response["items"]:
        video_data = {
            "title": item["snippet"]["title"],
            "description": item["snippet"]["description"],
        }
        videos.append(video_data)

    next_page_token = playlist_items_response.get("nextPageToken")
    if not next_page_token:
        break

with open("video_data.json", "w", encoding="utf-8") as outfile:
    json.dump(videos, outfile, ensure_ascii=False)
