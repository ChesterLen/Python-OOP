from typing import List
from project.song import Song

class Album:
    def __init__(self, name: str, *songs_args):
        self.name = name
        self.published = False
        self.songs: List[Song] = list(songs_args)

    def add_song(self, song: Song) -> str:
        if song in self.songs:
            return "Song is already in the album."
        elif self.published == True:
            return "Cannot add songs. Album is published."
        elif song.single == True:
            return f"Cannot add {song.name}. It's a single"
    
        self.songs.append(song)
        return f"Song {song.name} has been added to the album {self.name}."
    
    def remove_song(self, song_name: str) -> str:
        removed_song = [s for s in self.songs if s.name == song_name][0]

        if not removed_song:
            return "Song is not in the album."
        elif self.published == True:
            return "Cannot remove songs. Album is published."
        
        self.songs.remove(removed_song)
        return f"Removed song {song_name} from album {self.name}."
    
    def publish(self):
        if self.published == True:
            return f"Album {self.name} is already published."
        
        self.published = True
        return f"Album {self.name} has been published."
    
    def details(self):
        songs_names = "\n".join([f"== {song.get_info()}" for song in self.songs])

        return f"Album {self.name}\n" \
               f"{songs_names}"