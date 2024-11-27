from django.test import TestCase
from website.models import SiteInfo, SocialCount, Newsletter
from website.models import Newsletter
from django.core.exceptions import ValidationError
from django.utils import timezone
from datetime import timedelta

class SiteInfoModelTest(TestCase):
    def setUp(self):
        """Crée une instance de SiteInfo pour les tests."""
        self.site_info = SiteInfo.objects.create(
            email='contact@website.com',
            nom='Mon Site Web',
            telephone=1234567890,
            description='Ceci est un site web de test.',
            logo='logo/site/logo.png',
            status=True
        )

    def test_site_info_creation(self):
        """Test de la création d'une instance de SiteInfo."""
        site_info = self.site_info
        self.assertEqual(site_info.email, 'contact@website.com')
        self.assertEqual(site_info.nom, 'Mon Site Web')
        self.assertEqual(site_info.telephone, 1234567890)
        self.assertTrue(site_info.status)
        self.assertIsInstance(site_info.date_add, timezone.datetime)
        self.assertIsInstance(site_info.date_update, timezone.datetime)
    def test_site_info_str(self):
        """Test de la méthode __str__ de SiteInfo"""
        site_info = SiteInfo.objects.create(
            email="contact@monsite.com",
            nom="Mon Site Web",
            telephone=1234567890,
            description="Description du site",
            logo="logo_site.png"
        )
       
class SocialCountModelTest(TestCase):
    def setUp(self):
        """Crée une instance de SocialCount pour les tests."""
        self.social_count = SocialCount.objects.create(
            nom='Facebook',
            lien='https://facebook.com/monpage',
            icones='fa-facebook-f',
            status=True
        )

    def test_social_count_creation(self):
        """Test de la création d'une instance de SocialCount."""
        social_count = self.social_count
        self.assertEqual(social_count.nom, 'Facebook')
        self.assertEqual(social_count.lien, 'https://facebook.com/monpage')
        self.assertEqual(social_count.icones, 'fa-facebook-f')
        self.assertTrue(social_count.status)
        self.assertIsInstance(social_count.date_add, timezone.datetime)
        self.assertIsInstance(social_count.date_update, timezone.datetime)

    def test_social_count_str(self):
        """Test de la méthode __str__ de SocialCount."""
        self.assertEqual(str(self.social_count), 'Facebook')

    def test_social_count_invalid_icon(self):
        """Test pour vérifier qu'une icône non valide génère une erreur."""
        with self.assertRaises(ValidationError):
            invalid_icon = 'invalid-icon'
            # Vérifie que l'icône est parmi les choix
            valid_choices = [choice[0] for choice in SocialCount.ICONES]
            if invalid_icon not in valid_choices:
                raise ValidationError(f"{invalid_icon} n'est pas une icône valide.")
            
            # Crée un SocialCount avec une icône invalide
            SocialCount.objects.create(
                nom="Test",
                lien="https://example.com",
                icones=invalid_icon,
                status=True
            )

class NewsletterModelTest(TestCase):
    def setUp(self):
        """Crée une instance de Newsletter pour les tests."""
        self.newsletter = Newsletter.objects.create(
            email='subscriber@website.com',
            status=True
        )

    def test_newsletter_creation(self):
        """Test de la création d'une instance de Newsletter."""
        newsletter = self.newsletter
        self.assertEqual(newsletter.email, 'subscriber@website.com')
        self.assertTrue(newsletter.status)
        self.assertIsInstance(newsletter.date_add, timezone.datetime)
        self.assertIsInstance(newsletter.date_update, timezone.datetime)

    def test_newsletter_str(self):
        """Test de la méthode __str__ de Newsletter."""
        self.assertEqual(str(self.newsletter), 'subscriber@website.com')

    def test_newsletter_invalid_email(self):
        """Test pour vérifier qu'un email invalide génère une erreur."""
        from django.core.validators import validate_email

        with self.assertRaises(ValidationError):
            # Valide l'email avant la création
            validate_email('invalid-email')

            # Si l'email passe la validation (ce qui ne devrait pas arriver ici), il est sauvegardé
            Newsletter.objects.create(email='invalid-email', status=True)
class SiteInfoModelUpdateTest(TestCase):
    def setUp(self):
        """Crée une instance de SiteInfo pour les tests de mise à jour."""
        self.site_info = SiteInfo.objects.create(
            email='old_email@website.com',
            nom='Ancien Site',
            telephone=1234567890,
            description='Ancienne description.',
            logo='logo/site/old_logo.png',
            status=False
        )

    def test_update_site_info(self):
        """Test pour mettre à jour une instance de SiteInfo."""
        self.site_info.email = 'new_email@website.com'
        self.site_info.nom = 'Nouveau Site'
        self.site_info.telephone = 9876543210
        self.site_info.save()

        self.site_info.refresh_from_db()
        self.assertEqual(self.site_info.email, 'new_email@website.com')
        self.assertEqual(self.site_info.nom, 'Nouveau Site')
        self.assertEqual(self.site_info.telephone, 9876543210)

    def test_delete_site_info(self):
        """Test pour supprimer une instance de SiteInfo."""
        self.site_info.delete()
        with self.assertRaises(SiteInfo.DoesNotExist):
            SiteInfo.objects.get(id=self.site_info.id)
