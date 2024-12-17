class PLayMusic:
    def __init__(self, playlist=[], volume=100):
        self.playlist = playlist
        self.volume = volume

    def play_song(self):
        song = input("The song you wanna hear:  ")
        print("---------------------------------")
        print("işte çalan şarkı = ", song)
        self.playlist.append(song)

    def show_volume(self):
        print("çalan şarkının ses seviyesi = ", self.volume)


songs = PLayMusic()
songs.add_song()
songs.show_volume()
