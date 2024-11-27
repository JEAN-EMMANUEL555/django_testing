from django.test import TestCase
from .models import Curriculum, Contact, Prestation, Presentation, Gallerie

class CurriculumIntegrationTest(TestCase):

    def test_create_curriculum(self):
        """
        Test pour la création d'un curriculum.
        """
        curriculum = Curriculum.objects.create(
            photo="images/curriculum/photo.jpg",
            nom="John Doe",
            description="<p>Développeur full-stack</p>",
            cv="cv/curriculum/john_doe.pdf",
            status=True
        )
        self.assertEqual(Curriculum.objects.count(), 1)
        self.assertEqual(curriculum.nom, "John Doe")
        self.assertTrue(curriculum.status)

class ContactIntegrationTest(TestCase):

    def test_create_contact(self):
        """
        Test pour la création d'un contact.
        """
        contact = Contact.objects.create(
            nom="Jane Doe",
            email="jane.doe@example.com",
            subject="Demande de renseignements",
            telephone=123456789,
            message="Pouvez-vous m'envoyer plus d'informations ?",
            status=True
        )
        self.assertEqual(Contact.objects.count(), 1)
        self.assertEqual(contact.nom, "Jane Doe")
        self.assertEqual(contact.email, "jane.doe@example.com")

class PrestationIntegrationTest(TestCase):

    def test_create_prestation(self):
        """
        Test pour la création d'une prestation.
        """
        prestation = Prestation.objects.create(
            titre="Conception Web",
            description="Création de sites web modernes.",
            image="images/prestations/web_design.jpg",
            status=True
        )
        self.assertEqual(Prestation.objects.count(), 1)
        self.assertEqual(prestation.titre, "Conception Web")

class PresentationIntegrationTest(TestCase):

    def test_create_presentation(self):
        """
        Test pour la création d'une présentation.
        """
        presentation = Presentation.objects.create(
            titre="Présentation d'entreprise",
            image="image/presentation/company.jpg",
            description="<p>Nous sommes une entreprise innovante.</p>",
            status=True
        )
        self.assertEqual(Presentation.objects.count(), 1)
        self.assertEqual(presentation.titre, "Présentation d'entreprise")

class GallerieIntegrationTest(TestCase):

    def test_create_gallerie(self):
        """
        Test pour la création d'une image dans la galerie.
        """
        gallerie = Gallerie.objects.create(
            gallerie="gallerie/image/photo1.jpg",
            titre="Coucher de soleil",
            status=True
        )
        self.assertEqual(Gallerie.objects.count(), 1)
        self.assertEqual(gallerie.titre, "Coucher de soleil")
