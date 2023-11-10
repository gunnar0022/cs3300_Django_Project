
from django.test import TestCase, Client
from music_app.models import Song
from music_app.models import User

from django.urls import reverse
class SongModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up data for the whole TestCase
        # This method is called once before any test methods in this class.
        Song.objects.create(name='Imagine', instrument='piano', genre='rock')

    def test_song_content(self):
        # Test the content of the song object
        # This tests the Song model's attributes for expected values.
        song = Song.objects.get(id=1)
        expected_object_name = f'{song.name}'
        expected_object_instrument = f'{song.instrument}'
        expected_object_genre = f'{song.genre}'
        self.assertEqual(expected_object_name, 'Imagine')
        self.assertEqual(expected_object_instrument, 'piano')
        self.assertEqual(expected_object_genre, 'rock')

    def test_string_representation(self):
        # Test the __str__ method of the song model
        # Ensures the string representation of the song object is the song's name.
        song = Song.objects.get(id=1)
        self.assertEqual(str(song), song.name)

class SongModelTest2(TestCase):
    def setUp(self):
        # Set up non-modified objects used by test methods
        # This method is called before every test function to set up an individual song object.
        self.song = Song.objects.create(name='Imagine', instrument='guitar', genre='rock')

    def test_str_representation(self):
        # Test the __str__ method on the song model
        # Checks if the __str__ method of Song returns the correct string.
        self.assertEqual(str(self.song), 'Imagine')

class SongDetailViewTest(TestCase):
    def setUp(self):
        # Setup before each test method.
        # Creates a song object to be used in the detail view test.
        self.song = Song.objects.create(name='Wonderwall', instrument='guitar', genre='rock')

    def test_song_detail_view(self):
        # Test the song detail view to ensure it responds with a 200 (success)
        # and that the song's name is part of the response content.
        url = reverse('song_detail', args=[self.song.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'song_detail.html')
        self.assertContains(response, 'Wonderwall')

class SongTemplateTests(TestCase):

    def setUp(self):
        # Setup before each test method.
        # Establishes a test client and creates a song object for template tests.
        self.client = Client()
        self.song = Song.objects.create(
            name='Test Song',
            instrument='guitar',
            genre='rock'
        )
    
    def test_song_list_template(self):
        # Verify that the song_list template is used and the song's name appears in the content.
        response = self.client.get(reverse('song_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'song_list.html')
        self.assertContains(response, self.song.name)
    
    def test_song_detail_template(self):
        # Ensure that the song_detail template is used and the song's name and genre appear in the content.
        response = self.client.get(reverse('song_detail', args=[self.song.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'song_detail.html')
        self.assertContains(response, self.song.name)
        self.assertContains(response, self.song.genre)



