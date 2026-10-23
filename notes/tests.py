from django.test import TestCase
from django.urls import reverse
from .models import Note
class NoteTests(TestCase):
    def setUp(self):
        self.note = Note.objects.create(title='Test', text='Hello')
    def test_list_page(self):
        r = self.client.get(reverse('note_list'))
        self.assertEqual(r.status_code, 200)
    def test_create_note(self):
        r = self.client.post(reverse('note_create'), {'title':'New','text':'Body'})
        self.assertRedirects(r, reverse('note_list'))
        self.assertEqual(Note.objects.count(), 2)
    def test_detail_page(self):
        r = self.client.get(reverse('note_detail', args=[self.note.pk]))
        self.assertEqual(r.status_code, 200)
    def test_delete_note(self):
        r = self.client.post(reverse('note_delete', args=[self.note.pk]))
        self.assertRedirects(r, reverse('note_list'))
        self.assertEqual(Note.objects.count(), 0)
