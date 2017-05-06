class Person():

    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname


class Artist(Person):

    def __init__(self, firstname, lastname, stage_name):
        super().__init__(firstname, lastname)
        self.stage_name = stage_name

    @property
    def get_name(self):
        return (self.firstname + ',' + self.lastname)

    def get_stage_name(self):
        return self.stage_name


class Song():
    def __init__(self, song_title, Lenght_of_song, list_of_artist, genre):
        self.song_title = song_title
        self.Lenght_of_song = Lenght_of_song
        self.list_of_artist = list_of_artist
        self.genre = genre
        self.listen_to = 0

    def listen_to_song(self):
        self.listen_to = self.listen_to + 1
        return self

    def get_listen_to(self):
        return self.listen_to

    def get_genre(self):
        return self.genre

    @property
    def get_title(self):
        return self.song_title


class Album():

    def __init__(self, list_of_artist, album_name, record_label, genre=None, list_of_songs=[]):
        self.list_of_artist = list_of_artist
        self.album_name = album_name
        self.record_label = record_label
        self.genre = genre
        self.list_of_songs = list_of_songs

    def get_artist(self):
        return self.list_of_artist

    def get_title(self):
        return self.album_name

    def get_record_label(self):
        return self.record_label

    def get_genre(self):
        return self.genre


class Subscriber(Person):

    subscription_types = {"platinum": "e20", "gold": "e12", "free": "free"}

    def __init__(self, firstname, lastname, subscription):
        super().__init__(firstname, lastname)
        if subscription in self.subscription_types.keys():
            self.subscription = subscription

        self.playlist = []

    def get_subscription_type(self):
        return self.subscription

    def get_subscriber_info(self):
        return self.firstname + ',' + self.lastname + ':' + self.subscription

    def set_subscription_type(self, new_subscription):
        if new_subscription in self.subscription_types.keys():
            self.subscription = new_subscription
            return self.subscription

    def get_playlist(self):
        for songs in self.playlist:
            return self.playlist

    def add_to_playlist(self, song):
        if self.subscription in self.subscription_types.keys():
            self.playlist.append(song)
            song.listen_to_song()
            return self
        else:
            raise Exception('invalid subscription')


def main():

    sub1 = Subscriber('temi', 'adeyera', 'platinum')
    sub2 = Subscriber('temi', 'adeyera', 'platinum')
    song1 = Song('ready to die', '4.5min', 'notorious big', 'hip-hop')
    song2 = Song('big-poppa', '5.5min', 'notorious big', 'hip-hop')

    print(sub1.add_to_playlist(song1))
    # print(sub1.add_to_playlist(song2))
    # print(sub1 .get_playlist())
    # print(sub1.get_playlist())
    # print(sub2.get_playlist())
    # print(sub3.get_playlist())
    print(sub1.set_subscription_type('gold'))
    print(song1.get_listen_to())


if __name__ == "__main__":
    main()
