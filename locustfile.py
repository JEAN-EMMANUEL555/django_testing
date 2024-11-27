from locust import HttpUser, task, between
from random import choice

class WebsiteUser(HttpUser):
    # Simulation d'un délai entre les requêtes (en secondes)
    wait_time = between(1, 3)

    # Liste d'URL à tester, ajuste en fonction de tes routes
    urls_to_test = [
        '/newsletter/',
        '/home/',
        '/about/',
    ]

    @task
    def index(self):
        """Test de la page d'accueil"""
        self.client.get("/")

    @task(2)  # Le nombre "2" indique qu'il faut appeler cette tâche deux fois plus souvent
    def subscribe_newsletter(self):
        """Test de la création d'un abonnement à la newsletter"""
        invalid_email = "invalid-email@domain"
        self.client.post("/newsletter/", data={"email": invalid_email, "status": True})

    @task(3)
    def visit_random_page(self):
        """Visite une page aléatoire"""
        page = choice(self.urls_to_test)
        self.client.get(page)

    @task
    def test_social_count(self):
        """Simule une requête sur les réseaux sociaux"""
        self.client.get("/social-count/")
