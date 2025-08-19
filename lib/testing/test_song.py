import unittest
from song import Song

class TestSong(unittest.TestCase):
    def setUp(self):
        # Reset before each test
        Song.count = 0
        Song.artists = []
        Song.genres = []
        Song.genre_count = {}
        Song.artist_count = {}

    def test_song_initialization(self):
        song = Song("99 Problems", "Jay-Z", "Rap")
        assert song.name == "99 Problems"
        assert song.artist == "Jay-Z"
        assert song.genre == "Rap"

    def test_song_count(self):
        Song("99 Problems", "Jay-Z", "Rap")
        Song("Halo", "Beyonce", "Pop")
        assert Song.count == 2

    def test_unique_artists(self):
        Song("99 Problems", "Jay-Z", "Rap")
        Song("Encore", "Jay-Z", "Rap")
        Song("Halo", "Beyonce", "Pop")
        assert set(Song.artists) == {"Jay-Z", "Beyonce"}

    def test_unique_genres(self):
        Song("99 Problems", "Jay-Z", "Rap")
        Song("Halo", "Beyonce", "Pop")
        Song("Formation", "Beyonce", "Pop")
        assert set(Song.genres) == {"Rap", "Pop"}

    def test_genre_count(self):
        Song("99 Problems", "Jay-Z", "Rap")
        Song("God's Plan", "Drake", "Rap")
        Song("Halo", "Beyonce", "Pop")
        assert Song.genre_count == {"Rap": 2, "Pop": 1}

    def test_artist_count(self):
        Song("99 Problems", "Jay-Z", "Rap")
        Song("Encore", "Jay-Z", "Rap")
        Song("Halo", "Beyonce", "Pop")
        assert Song.artist_count == {"Jay-Z": 2, "Beyonce": 1}
