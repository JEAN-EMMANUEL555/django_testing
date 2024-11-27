from django.test import TestCase
from .models import (
    Categorie, Publication, Commentaire, 
    ReponseCommentaire, Like, Evenement, 
    Cours, Textes, Video
)
from datetime import datetime
from django.utils.text import slugify


class CategorieModelTest(TestCase):

    def test_categorie_creation(self):
        # Test de la création d'une catégorie
        categorie = Categorie.objects.create(
            nom="Test Category",
            description="Test description"
        )
        self.assertEqual(categorie.nom, "Test Category")
        self.assertTrue(categorie.status)
        self.assertIsNotNone(categorie.date_add)


class PublicationModelTest(TestCase):

    def test_publication_creation(self):
        # Création d'une catégorie pour la publication
        categorie = Categorie.objects.create(
            nom="Test Category",
            description="Test description"
        )

        # Test de la création d'une publication
        publication = Publication.objects.create(
            titre="Test Publication",
            description="Test content",
            image="path/to/image.jpg",
            categorie=categorie
        )
        self.assertEqual(publication.titre, "Test Publication")
        self.assertTrue(publication.status)
        self.assertIn(slugify(publication.titre), publication.slug)
        self.assertIsNotNone(publication.date_add)


class CommentaireModelTest(TestCase):

    def test_commentaire_creation(self):
        # Création des objets nécessaires pour le test
        categorie = Categorie.objects.create(
            nom="Test Category",
            description="Test description"
        )
        publication = Publication.objects.create(
            titre="Test Publication",
            description="Test content",
            image="path/to/image.jpg",
            categorie=categorie
        )

        # Test de la création d'un commentaire
        commentaire = Commentaire.objects.create(
            publication=publication,
            nom="Test User",
            email="test@example.com",
            commentaire="This is a test comment"
        )
        self.assertEqual(commentaire.nom, "Test User")
        self.assertTrue(commentaire.status)
        self.assertEqual(commentaire.publication, publication)


class ReponseCommentaireModelTest(TestCase):

    def test_reponse_creation(self):
        # Création des objets nécessaires pour le test
        categorie = Categorie.objects.create(
            nom="Test Category",
            description="Test description"
        )
        publication = Publication.objects.create(
            titre="Test Publication",
            description="Test content",
            image="path/to/image.jpg",
            categorie=categorie
        )
        commentaire = Commentaire.objects.create(
            publication=publication,
            nom="Test User",
            email="test@example.com",
            commentaire="This is a test comment"
        )

        # Test de la création d'une réponse à un commentaire
        reponse = ReponseCommentaire.objects.create(
            commentaire=commentaire,
            nom="Responder",
            email="responder@example.com",
            reponse="This is a response"
        )
        self.assertEqual(reponse.nom, "Responder")
        self.assertTrue(reponse.status)
        self.assertEqual(reponse.commentaire, commentaire)


class LikeModelTest(TestCase):

    def test_like_creation(self):
        # Création des objets nécessaires pour le test
        categorie = Categorie.objects.create(
            nom="Test Category",
            description="Test description"
        )
        publication = Publication.objects.create(
            titre="Test Publication",
            description="Test content",
            image="path/to/image.jpg",
            categorie=categorie
        )

        # Test de la création d'un like
        like = Like.objects.create(
            publication=publication
        )
        self.assertEqual(like.publication, publication)
        self.assertTrue(like.status)
        self.assertIsNotNone(like.date_add)


class EvenementModelTest(TestCase):

    def test_evenement_creation(self):
        # Test de la création d'un événement
        evenement = Evenement.objects.create(
            titre="Test Event",
            description="Event description",
            image="path/to/event.jpg"
        )
        self.assertEqual(evenement.titre, "Test Event")
        self.assertTrue(evenement.status)
        self.assertIn(slugify(evenement.titre), evenement.slug)


class CoursModelTest(TestCase):

    def test_cours_creation(self):
        # Test de la création d'un cours
        cours = Cours.objects.create(
            titre="Test Course",
            niveau="Beginner",
            annee=2024,
            description="Course description",
            image="path/to/course.jpg",
            cours="path/to/course.pdf"
        )
        self.assertEqual(cours.titre, "Test Course")
        self.assertEqual(cours.niveau, "Beginner")
        self.assertTrue(cours.status)


class TextesModelTest(TestCase):

    def test_textes_creation(self):
        # Test de la création d'un texte de référence
        textes = Textes.objects.create(
            titre="Test Texte",
            description="Texte description",
            image="path/to/texte.jpg",
            pdf="path/to/texte.pdf"
        )
        self.assertEqual(textes.titre, "Test Texte")
        self.assertTrue(textes.status)


class VideoModelTest(TestCase):

    def test_video_creation(self):
        # Test de la création d'une vidéo
        video = Video.objects.create(
            titre="Test Video",
            description="Video description",
            image="path/to/video.jpg",
            video="https://youtube.com/watch?v=example"
        )
        self.assertEqual(video.titre, "Test Video")
        self.assertTrue(video.status)
        self.assertIn("example", video.get_video)
