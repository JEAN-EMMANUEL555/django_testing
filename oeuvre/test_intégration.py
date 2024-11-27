from django.test import TestCase
from .models import Poesie

class PoesieIntegrationTest(TestCase):
    
    def setUp(self):
        """
        Initialisation des données pour les tests.
        """
        self.poeme_data = {
            "titre": "Ode à la Nuit",
            "description": "Un poème dédié à la tranquillité nocturne.",
            "poeme": "<p>Ô nuit, douce et silencieuse,</p><p>Embrasse mes pensées rêveuses.</p>",
            "status": True
        }
        self.poeme = Poesie.objects.create(**self.poeme_data)

    def test_create_poesie(self):
        """
        Test pour vérifier la création d'une poésie.
        """
        poesie = Poesie.objects.create(
            titre="Le Chant des Saisons",
            description="Un poème sur les cycles de la nature.",
            poeme="<p>Printemps verdoyant, été flamboyant...</p>",
            status=True
        )
        self.assertEqual(Poesie.objects.count(), 2)
        self.assertEqual(poesie.titre, "Le Chant des Saisons")
        self.assertTrue(poesie.status)

    def test_retrieve_poesie(self):
        """
        Test pour récupérer une poésie existante.
        """
        poesie = Poesie.objects.get(id=self.poeme.id)
        self.assertEqual(poesie.titre, "Ode à la Nuit")
        self.assertEqual(poesie.description, "Un poème dédié à la tranquillité nocturne.")

    def test_update_poesie(self):
        """
        Test pour mettre à jour une poésie existante.
        """
        self.poeme.titre = "Ode à l'Aube"
        self.poeme.save()
        poesie_updated = Poesie.objects.get(id=self.poeme.id)
        self.assertEqual(poesie_updated.titre, "Ode à l'Aube")

    def test_delete_poesie(self):
        """
        Test pour supprimer une poésie existante.
        """
        poesie_id = self.poeme.id
        self.poeme.delete()
        with self.assertRaises(Poesie.DoesNotExist):
            Poesie.objects.get(id=poesie_id)
