from django.test import TestCase
from .models import Curriculum, Contact, Prestation, Presentation, Gallerie
from django.core.files.uploadedfile import SimpleUploadedFile

class CurriculumModelTest(TestCase):
    
    def setUp(self):
        self.curriculum = Curriculum.objects.create(
            photo=SimpleUploadedFile("photo.jpg", b"image content", content_type="image/jpeg"),
            nom="Test Curriculum",
            description="<p>Test description</p>",
            cv=SimpleUploadedFile("cv.pdf", b"pdf content", content_type="application/pdf")
        )

    def test_curriculum_creation(self):
        # Vérifie que l'objet Curriculum a bien été créé
        self.assertEqual(Curriculum.objects.count(), 1)
        self.assertEqual(self.curriculum.nom, "Test Curriculum")

    def test_curriculum_str(self):
        # Vérifie la méthode __str__
        self.assertEqual(str(self.curriculum), "Test Curriculum")


class ContactModelTest(TestCase):

    def setUp(self):
        self.contact = Contact.objects.create(
            nom="John Doe",
            email="john@example.com",
            subject="Test Subject",
            telephone=1234567890,
            message="This is a test message."
        )

    def test_contact_creation(self):
        # Vérifie que l'objet Contact a bien été créé
        self.assertEqual(Contact.objects.count(), 1)
        self.assertEqual(self.contact.nom, "John Doe")
        self.assertEqual(self.contact.email, "john@example.com")

    def test_contact_str(self):
        # Vérifie la méthode __str__
        self.assertEqual(str(self.contact), "John Doe")


class PrestationModelTest(TestCase):

    def setUp(self):
        self.prestation = Prestation.objects.create(
            titre="Test Prestation",
            description="This is a test description.",
            image=SimpleUploadedFile("image.jpg", b"image content", content_type="image/jpeg")
        )

    def test_prestation_creation(self):
        # Vérifie que l'objet Prestation a bien été créé
        self.assertEqual(Prestation.objects.count(), 1)
        self.assertEqual(self.prestation.titre, "Test Prestation")

    def test_prestation_str(self):
        # Vérifie la méthode __str__
        self.assertEqual(str(self.prestation), "Test Prestation")


class PresentationModelTest(TestCase):

    def setUp(self):
        self.presentation = Presentation.objects.create(
            titre="Test Presentation",
            description="<p>Test description</p>",
            image=SimpleUploadedFile("image.jpg", b"image content", content_type="image/jpeg")
        )

    def test_presentation_creation(self):
        # Vérifie que l'objet Presentation a bien été créé
        self.assertEqual(Presentation.objects.count(), 1)
        self.assertEqual(self.presentation.titre, "Test Presentation")

    def test_presentation_str(self):
        # Vérifie la méthode __str__
        self.assertEqual(str(self.presentation), "Test Presentation")


class GallerieModelTest(TestCase):

    def setUp(self):
        self.gallerie = Gallerie.objects.create(
            gallerie=SimpleUploadedFile("gallery_image.jpg", b"image content", content_type="image/jpeg"),
            titre="Test Gallery"
        )

    def test_gallerie_creation(self):
        # Vérifie que l'objet Gallerie a bien été créé
        self.assertEqual(Gallerie.objects.count(), 1)
        self.assertEqual(self.gallerie.titre, "Test Gallery")

    def test_gallerie_str(self):
        # Vérifie la méthode __str__
        self.assertEqual(str(self.gallerie), "Test Gallery")
