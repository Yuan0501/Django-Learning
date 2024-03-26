from django.test import TestCase
from .models import Logger


# Create your tests here.
class LoggerModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.reservation = Logger.objects.create(
            first_name = "Annie",
            last_name = "Stephen",
            time_log = "13:22",
            
        )
# check the firstname and lastname is string type
    def test_fields(self):
        self.assertIsInstance(self.reservation.first_name, str)

        self.assertIsInstance(self.reservation.last_name, int)

     
        # self.assertIsInstance(self.time_log, datetime)
