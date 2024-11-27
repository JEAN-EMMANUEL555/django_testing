from django.test import TestCase
from .models import Poesie
import time
class PoesieModelTest(TestCase):

    def setUp(self):
        # Cette méthode sera exécutée avant chaque test
        self.poesie = Poesie.objects.create(
            titre="La Nature",
            description="Un poème sur la beauté de la nature",
            poeme="<p>La nature est belle, et ses couleurs changent.</p>"
        )

    def test_poesie_creation(self):
        # Vérifie que la poésie a été correctement créée
        self.assertEqual(self.poesie.titre, "La Nature")
        self.assertEqual(self.poesie.description, "Un poème sur la beauté de la nature")
        self.assertEqual(self.poesie.poeme, "<p>La nature est belle, et ses couleurs changent.</p>")
        self.assertTrue(self.poesie.status)  # Statut par défaut doit être True

    def test_poesie_string_representation(self):
        # Vérifie que la méthode __str__ renvoie le titre
        self.assertEqual(str(self.poesie), "La Nature")

    def test_poesie_date_fields(self):
        # Vérifie que les champs date_add et date_update sont bien définis automatiquement
        self.assertIsNotNone(self.poesie.date_add)
        self.assertIsNotNone(self.poesie.date_update)

    def test_default_status(self):
        # Vérifie que le champ status par défaut est True
        poesie = Poesie.objects.create(
            titre="Soleil Couchant",
            description="Un poème sur le coucher de soleil",
            poeme="<p>Le soleil se couche sur l'horizon.</p>"
        )
        self.assertTrue(poesie.status)

    def test_update_poesie(self):
         time.sleep(1) 
         self.poesie.titre = "Beauté de la Nature"
         self.poesie.save()

         self.poesie.refresh_from_db()

         self.assertEqual(self.poesie.titre, "Beauté de la Nature")
         self.assertNotEqual(self.poesie.date_add, self.poesie.date_update)

    def test_create_multiple_poesies(self):
        # Test de la création de plusieurs poésies
        Poesie.objects.create(
            titre="Les Vagues",
            description="Un poème sur la mer",
            poeme="<p>Les vagues déferlent sur le rivage.</p>"
        )
        Poesie.objects.create(
            titre="Le Vent",
            description="Un poème sur le souffle du vent",
            poeme="<p>Le vent murmure à travers les arbres.</p>"
        )
