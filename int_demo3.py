import requests
import json

class InstagramStoryDownloader:
    def __init__(self, username):
        self.username = username
        self.stories = []

    def get_stories(self):
        url = f"https://www.instagram.com/{self.username}/story_highlights/"
        response = requests.get(url)
        data = json.loads(response.content)

        for story in data["stories"]:
            self.stories.append(story)

    def download_stories(self):
        for story in self.stories:
            if story["media_type"] == "VIDEO":
                url = story["video_url"]
            else:
                url = story["image_url"]

            filename = f"{story['id']}.jpg"
            response = requests.get(url)

            with open(filename, "wb") as f:
                f.write(response.content)

if __name__ == "__main__":
    username = "avs_24k"

    downloader = InstagramStoryDownloader(username)
    downloader.get_stories()
    downloader.download_stories()
