from django.test import TestCase
from .models import (
    Categorie, Publication, Commentaire, ReponseCommentaire, 
    Like, Evenement, Cours, Textes, Video
)

class CategorieIntegrationTest(TestCase):

    def test_create_categorie(self):
        """
        Test de création d'une catégorie.
        """
        categorie = Categorie.objects.create(
            nom="Technologie",
            description="Catégorie dédiée aux articles technologiques.",
            status=True
        )
        self.assertEqual(Categorie.objects.count(), 1)
        self.assertEqual(categorie.nom, "Technologie")


class PublicationIntegrationTest(TestCase):

    def test_create_publication(self):
        """
        Test de création d'une publication.
        """
        categorie = Categorie.objects.create(
            nom="Technologie",
            description="Catégorie dédiée aux articles technologiques."
        )
        publication = Publication.objects.create(
            titre="Les avancées en IA",
            description="<p>Un aperçu des dernières avancées.</p>",
            image="image/publication/ia.jpg",
            categorie=categorie,
            status=True
        )
        self.assertEqual(Publication.objects.count(), 1)
        self.assertEqual(publication.categorie.nom, "Technologie")


class CommentaireIntegrationTest(TestCase):

    def test_create_commentaire(self):
        """
        Test de création d'un commentaire.
        """
        categorie = Categorie.objects.create(nom="Technologie")
        publication = Publication.objects.create(
            titre="Les avancées en IA",
            description="<p>Un aperçu des dernières avancées.</p>",
            image="image/publication/ia.jpg",
            categorie=categorie
        )
        commentaire = Commentaire.objects.create(
            publication=publication,
            nom="Alice",
            email="alice@example.com",
            commentaire="Très intéressant !",
            status=True
        )
        self.assertEqual(Commentaire.objects.count(), 1)
        self.assertEqual(commentaire.publication.titre, "Les avancées en IA")


class ReponseCommentaireIntegrationTest(TestCase):

    def test_create_reponse_commentaire(self):
        """
        Test de création d'une réponse à un commentaire.
        """
        categorie = Categorie.objects.create(nom="Technologie")
        publication = Publication.objects.create(
            titre="Les avancées en IA",
            description="<p>Un aperçu des dernières avancées.</p>",
            image="image/publication/ia.jpg",
            categorie=categorie
        )
        commentaire = Commentaire.objects.create(
            publication=publication,
            nom="Alice",
            commentaire="Très intéressant !"
        )
        reponse = ReponseCommentaire.objects.create(
            commentaire=commentaire,
            nom="Bob",
            reponse="Merci pour le retour !",
            status=True
        )
        self.assertEqual(ReponseCommentaire.objects.count(), 1)
        self.assertEqual(reponse.commentaire.nom, "Alice")


class LikeIntegrationTest(TestCase):

    def test_create_like(self):
        """
        Test de création d'un 'Like' pour une publication.
        """
        categorie = Categorie.objects.create(nom="Technologie")
        publication = Publication.objects.create(
            titre="Les avancées en IA",
            description="<p>Un aperçu des dernières avancées.</p>",
            image="image/publication/ia.jpg",
            categorie=categorie
        )
        like = Like.objects.create(publication=publication, status=True)
        self.assertEqual(Like.objects.count(), 1)
        self.assertEqual(like.publication.titre, "Les avancées en IA")


class EvenementIntegrationTest(TestCase):

    def test_create_evenement(self):
        """
        Test de création d'un événement.
        """
        evenement = Evenement.objects.create(
            titre="Conférence IA",
            image="evenement/image/conference.jpg",
            description="<p>Conférence sur les technologies IA.</p>",
            status=True
        )
        self.assertEqual(Evenement.objects.count(), 1)
        self.assertEqual(evenement.titre, "Conférence IA")


class CoursIntegrationTest(TestCase):

    def test_create_cours(self):
        """
        Test de création d'un cours.
        """
        cours = Cours.objects.create(
            titre="Introduction à l'IA",
            niveau="Débutant",
            annee=2024,
            description="Cours de base pour découvrir l'intelligence artificielle.",
            image="cours/image/intro_ia.jpg",
            cours="cours/cours/intro_ia.pdf",
            status=True
        )
        self.assertEqual(Cours.objects.count(), 1)
        self.assertEqual(cours.niveau, "Débutant")


class TextesIntegrationTest(TestCase):

    def test_create_textes(self):
        """
        Test de création d'un texte de référence.
        """
        texte = Textes.objects.create(
            titre="Manuel d'IA",
            description="Guide complet sur l'intelligence artificielle.",
            image="textes/image/manuel_ia.jpg",
            pdf="pdf/textes/manuel_ia.pdf",
            status=True
        )
        self.assertEqual(Textes.objects.count(), 1)
        self.assertEqual(texte.titre, "Manuel d'IA")


class VideoIntegrationTest(TestCase):

    def test_create_video(self):
        """
        Test de création d'une vidéo.
        """
        video = Video.objects.create(
            titre="Introduction à l'IA",
            description="Vidéo introductive sur l'IA.",
            image="video/image/intro_ia.jpg",
            video="https://www.youtube.com/watch?v=abcdef",
            status=True
        )
        self.assertEqual(Video.objects.count(), 1)
        self.assertEqual(video.titre, "Introduction à l'IA")
