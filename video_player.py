"""A video player class."""
from random import randrange

from .video_library import VideoLibrary
from .video_playlist import Playlist


class VideoPlayer:
    """A class used to represent a Video Player."""

    playing = ""
    paused = False
    playlists = []

    def __init__(self):
        self._video_library = VideoLibrary()
        self.video_list = self._video_library.get_all_videos()

    def number_of_videos(self):
        num_videos = len(self._video_library.get_all_videos())
        print(f"{num_videos} videos in the library")

    def show_all_videos(self):
        # video_list = self._video_library.get_all_videos()

        for video in self.video_list:
            print(video.title, "(" + video.video_id + ")", video.tags)
        """Returns all videos."""

    def play_video(self, video_id):
        """Plays the respective video.

        Args:
            video_id: The video_id to be played.
        """
        video_title = ""

        for video in self.video_list:
            if video.video_id == video_id:
                video_title = video.title

        if video_title == "":
            print("Cannot play video: Video does not exist")
        elif self.playing == "":
            print("Playing video:", video_title)
            self.playing = video_title
        elif self.playing != "":
            print("Stopping video:", self.playing)
            self.playing = video_title
            print("Playing video:", self.playing)

    def stop_video(self):
        """Stops the current video."""

        if self.playing != "":
            print("Stopping video:", self.playing)
            self.playing = ""
        else:
            print("Cannot stop video: No video is currently playing")

    def play_random_video(self):
        """Plays a random video from the video library."""
        x = randrange(len(self.video_list))
        self.play_video(self.video_list[x].video_id)

    def pause_video(self):
        """Pauses the current video."""
        if not self.paused:
            if self.playing != "":
                print("Pausing video:", self.playing)
                self.paused = True
            else:
                print("Cannot pause video: No video is currently playing")
        else:
            print("Video already paused:", self.playing)

    def continue_video(self):
        """Resumes playing the current video."""
        if self.paused:
            if self.playing != "":
                print("Continuing video:", self.playing)
                self.paused = False
        else:
            print("Cannot continue video: No video is not paused")

    def show_playing(self):
        """Displays video currently playing."""

        if self.playing != "":
            if self.paused:
                print("Currently playing:", self.playing, "- PAUSED")
            else:
                print("Currently playing:", self.playing)
        else:
            print("No video is currently playing")

    def create_playlist(self, playlist_name):
        """Creates a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        if " " in playlist_name:
            print("playlist name cannot contain blank spaces")
            playlist_name = input("enter a valid playlist name:")

        is_in_list = False

        for new in self.playlists:
            if new.name.lower() == playlist_name.lower():
                is_in_list = True
                print("Cannot create playlist: A playlist with the same name already exists")

        if not is_in_list:
            self.playlists.append(Playlist(playlist_name))
            print("successfully created new playlist:", playlist_name)

    def add_to_playlist(self, playlist_name, video_id):
        """Adds a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be added.
        """
        for vid in self.video_list:
            if vid.video_id == video_id:
                # for x in self.playlists:
                #     if x.name.lower() == playlist_name.lower():
                #         x.append(vid)
                print("Added video to", playlist_name + ":", vid.title)


    def show_all_playlists(self):
        """Display all playlists."""

        print("show_all_playlists needs implementation")

    def show_playlist(self, playlist_name):
        """Display all videos in a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("show_playlist needs implementation")

    def remove_from_playlist(self, playlist_name, video_id):
        """Removes a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be removed.
        """
        print("remove_from_playlist needs implementation")

    def clear_playlist(self, playlist_name):
        """Removes all videos from a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("clears_playlist needs implementation")

    def delete_playlist(self, playlist_name):
        """Deletes a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("deletes_playlist needs implementation")

    def search_videos(self, search_term):
        """Display all the videos whose titles contain the search_term.

        Args:
            search_term: The query to be used in search.
        """
        print("search_videos needs implementation")

    def search_videos_tag(self, video_tag):
        """Display all videos whose tags contains the provided tag.

        Args:
            video_tag: The video tag to be used in search.
        """
        print("search_videos_tag needs implementation")

    def flag_video(self, video_id, flag_reason=""):
        """Mark a video as flagged.

        Args:
            video_id: The video_id to be flagged.
            flag_reason: Reason for flagging the video.
        """
        print("flag_video needs implementation")

    def allow_video(self, video_id):
        """Removes a flag from a video.

        Args:
            video_id: The video_id to be allowed again.
        """
        print("allow_video needs implementation")
