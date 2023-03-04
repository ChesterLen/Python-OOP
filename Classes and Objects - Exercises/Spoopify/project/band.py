from typing import List
from project.album import Album
from project.song import Song

class Band:
    def __init__(self, name: str):
        self.name = name
        self.albums: List[Album] = []

    def add_album(self, album: Album) -> str:
        if album in self.albums:
            return f"Band {self.name} already has {album.name} in their library."
        
        self.albums.append(album)
        return f"Band {self.name} has added their newest album {album.name}."
    
    def remove_album(self, album_name: str) -> str:
        remove_album = [a for a in self.albums if a.name == album_name][0]

        if not remove_album:
            return f"Album {album_name} is not found."
        elif remove_album.published == True:
            return "Album has been published. It cannot be removed."
        
        self.albums.remove(remove_album)
        return f"Album {remove_album.name} has been removed."
    
    def details(self):
        albums = "\n".join(f"{album.details()}" for album in self.albums)

        return f"Band {self.name}\n" \
               f"{albums}"