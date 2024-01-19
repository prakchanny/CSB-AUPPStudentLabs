
import pickle

class Song:
    def __init__(self, title, artist, album, genre, length):
        self.title = title
        self.artist = artist
        self.album = album
        self.genre = genre
        self.length = length

    def __repr__(self):
        return f"Song({self.title}, {self.artist}, {self.album}, {self.genre}, {self.length})"

class MusicLibrary:
    def __init__(self):
        self.songs = {} 

    def add_song(self, song):
        if song.title not in self.songs:
            self.songs[song.title] = song

    def get_songs_by_artist(self, artist):
        return self.songs.get(artist, [])

    def get_songs_by_album(self, album):
        return [song for song in self.songs.values() if song.album == album]

    def get_songs_by_genre(self, genre):
        return [song for song in self.songs.values() if song.genre == genre]

    def get_songs_by_title(self, title):
        return self.songs.get(title, None)

    def save_songs(self, filename):
        with open(filename, "wb") as f:
            pickle.dump(self.songs, f)

    def load_songs(self, filename):
        with open(filename, "rb") as f:
            self.songs = pickle.load(f)

song1 = Song("Shape of You", "Ed Sheeran", "Divide", "Pop", "3:53")
song2 = Song("Despacito", "Luis Fonsi", "Vida", "Latin Pop", "4:42")
song3 = Song("Believer", "Imagine Dragons", "Evolve", "Rock", "3:24")

library = MusicLibrary()

library.add_song(song1)
library.add_song(song2)
library.add_song(song3)

library.save_songs("songs.data")

library.load_songs("songs.data")

print(library.songs)
