# Import the pickle module
import pickle

# Define the song class
class Song:
    def __init__(self, title, artist, album, genre, length):
        self.title = title
        self.artist = artist
        self.album = album
        self.genre = genre
        self.length = length

    def __repr__(self):
        return f"Song({self.title}, {self.artist}, {self.album}, {self.genre}, {self.length})"

# Define the music library class
class MusicLibrary:
    def __init__(self):
        self.songs = {} # A dictionary to store the songs and their metadata

    def add_song(self, song):
        # Add a song to the music library
        # Use the title as the key and the song object as the value
        # If the song already exists, do not add it
        if song.title not in self.songs:
            self.songs[song.title] = song

    def get_songs_by_artist(self, artist):
        # Return a list of songs by a given artist
        # Use the dictionary method get to return the songs that match the artist key
        return self.songs.get(artist, [])

    def get_songs_by_album(self, album):
        # Return a list of songs from a given album
        # Use a list comprehension to filter the songs by the album value
        return [song for song in self.songs.values() if song.album == album]

    def get_songs_by_genre(self, genre):
        # Return a list of songs from a given genre
        # Use a list comprehension to filter the songs by the genre value
        return [song for song in self.songs.values() if song.genre == genre]

    def get_songs_by_title(self, title):
        # Return a song by a given title
        # Use the dictionary method get to return the song that matches the title key
        return self.songs.get(title, None)

    def save_songs(self, filename):
        # Save the songs to a file using pickle
        # Use the pickle.dump function to write the songs dictionary to a binary file
        # Use the "wb" mode to open the file for writing
        with open(filename, "wb") as f:
            pickle.dump(self.songs, f)

    def load_songs(self, filename):
        # Load the songs from a file using pickle
        # Use the pickle.load function to read the songs dictionary from a binary file
        # Use the "rb" mode to open the file for reading
        with open(filename, "rb") as f:
            self.songs = pickle.load(f)

# Main Requirement:
# Create song examples
song1 = Song("Shape of You", "Ed Sheeran", "Divide", "Pop", "3:53")
song2 = Song("Despacito", "Luis Fonsi", "Vida", "Latin Pop", "4:42")
song3 = Song("Believer", "Imagine Dragons", "Evolve", "Rock", "3:24")

# Create a music library
library = MusicLibrary()

# Add songs to the music library
library.add_song(song1)
library.add_song(song2)
library.add_song(song3)

# Save the songs to a file
library.save_songs("songs.data")

# Load the songs from a file
library.load_songs("songs.data")

# Print the songs
print(library.songs)
