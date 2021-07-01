"""A video playlist class."""
from .video import Video

class Playlist:
    """A class used to represent a Playlist."""
    def __init__(self, name):
        self.name = name
        self.videos = []

    def add_video(self, video):
        self.videos.append(video)