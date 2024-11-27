from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from .models import SiteInfo, SocialCount, Newsletter


class SiteInfoModelTest(TestCase):
    def setUp(self):
        self.site_info = SiteInfo.objects.create(
            email="test@example.com",
            nom="Facebook",  # Assurez-vous que `nom` correspond à la valeur que vous attendez
            telephone=123456789,
            description="Ceci est une description de test",
            logo=SimpleUploadedFile(name='test_logo.jpg', content=b'', content_type='image/jpeg'),
        )


    def test_site_info_dates(self):
        self.assertIsNotNone(self.site_info.date_add)
        self.assertIsNotNone(self.site_info.date_update)


class SocialCountModelTest(TestCase):
    def setUp(self):
        self.social_count = SocialCount.objects.create(
            nom="Facebook",
            lien="https://www.facebook.com",
            icones="facebook",
        )

    def test_social_count_creation(self):
        self.assertEqual(self.social_count.nom, "Facebook")
        self.assertEqual(self.social_count.lien, "https://www.facebook.com")
        self.assertEqual(self.social_count.icones, "facebook")
        self.assertTrue(self.social_count.status)

    def test_social_count_string_representation(self):
        self.assertEqual(str(self.social_count), "Facebook")

    def test_social_count_dates(self):
        self.assertIsNotNone(self.social_count.date_add)
        self.assertIsNotNone(self.social_count.date_update)


class NewsletterModelTest(TestCase):
    def setUp(self):
        self.newsletter = Newsletter.objects.create(
            email="user@example.com"
        )

    def test_newsletter_creation(self):
        self.assertEqual(self.newsletter.email, "user@example.com")
        self.assertTrue(self.newsletter.status)

    def test_newsletter_string_representation(self):
        self.assertEqual(str(self.newsletter), "user@example.com")

    def test_newsletter_dates(self):
        self.assertIsNotNone(self.newsletter.date_add)
        self.assertIsNotNone(self.newsletter.date_update)
