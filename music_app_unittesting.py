import unittest
from music_app import Artist, Song, Album, Subscriber


class appTest(unittest.TestCase):

    def test_stage_name(self):
        art1 = Artist('sean', 'john', 'puffy')
        self.assertEqual(art1.get_stage_name(), 'puffy')

    def test_get_name(self):
        art2 = Artist('Penn', 'Hardaway', 'Lil me')
        self.assertEqual(art2.get_name, 'Penn,Hardaway')


class AlbumTest(unittest.TestCase):

    def test_get_genre_album(self):
        alb1 = Album('Tupac shakur', 'hit dem up', 'suge_knight', 'hip-hop')
        self.assertEqual(alb1.get_genre(), 'hip-hop')

    def test_artist(self):
        alb2 = Album('christopher wallace', 'ready to die', 'bad-boys', 'hip-hop')
        self.assertEqual(alb2.get_artist(), 'christopher wallace')

    def test_get_title_album(self):
        alb3 = Album('curtis jackson', 'in da club', 'g-unit', 'hip-hop')
        self.assertEqual(alb3.get_title(), 'in da club')


class SubscriptionTest(unittest.TestCase):

    def test_set_subscription_type(self):
        sub = Subscriber('temi', 'adeyera', 'platinum')
        self.assertEqual(sub.set_subscription_type('free'), 'free')

    def test_get_subscription_type(self):
        sub1 = Subscriber('temi', 'adeyera', 'gold')
        self.assertEqual(sub1.get_subscription_type(), 'gold')

    def test_add_to_playlist_with_valid_subscrption(self):
        sub2 = Subscriber('femi', 'stone', 'platinum')
        song1 = Song('dear mama', '4.5min', '2pac', 'hip-hop')
        sub2.add_to_playlist(song1)
        self.assertIn(song1, sub2.get_playlist())
        self.assertEqual(song1.get_listen_to(), 1)

    def test_add_to_playlist_with_None_subscription(self):
        sub4 = Subscriber('tolu', 'jacobs', ' ')
        song3 = Song('dear God', '3min', 'boy2men', 'blues')
        sub4.add_to_playlist(song3)
        self.assertNotIn(song3, sub4.get_playlist())
        self.assertEqual(song3.get_listen_to(), 0)


class SongTest(unittest.TestCase):

    def test_get_genre(self):
        song1 = Song('dear mama', '4.5min', '2pac', 'hip-hop')
        self.assertEqual(song1.get_genre(), 'hip-hop')

    def test_get_title(self):
        song2 = Song('big-poppa', '5.5min', 'biggie', 'hip-hop')
        self.assertEqual(song2.get_title, 'big-poppa')

    def test_get_listen_to(self):
        song3 = Song('stilmatic', '5.5min', 'nas', 'rap-song')
        self.assertEqual(song3.get_listen_to(), 0)


if __name__ == "__main__":
    unittest.main()
