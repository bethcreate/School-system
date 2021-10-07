from django.test import TestCase

class TrainerModelTestCase(TestCase):
    def setUp(self):
        self.trainer=Trainer(first_name="James",
        last_name="Mwai",
        age=32,
        Languages="English",
        Email_address="smartemwa@gmail.com",
        )
    def test_full_name_contains_first_name(self):
        self.assertIn(self.trainer.first_name,self.trainer.full_name())
    def test_full_name_contains_last_name(self):
        self.assertIn(self.trainer.last_name,self.trainer.full_name())
    def test_trainer_year_of_birth(self):
        current_year=datetime.datetime.now().year
        year=current_year-self.trainer.age
        self.assertEqual(year,self.trainer.date_of_birth())
    def test_register_trainer_view(self):
        url=reverse("register_trainer")
        data={"first_name":self.trainer.first_name,
        "last_name":self.trainer.last_name,
        "age":self.trainer.age,
        "Email_address":self.trainer.Email_address,
        }
        request=self.client.post(url,data)
        self.assertEqual(request.status_code,200)
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    def date_of_birth(self):
            current_year=datetime.datetime.now().year
