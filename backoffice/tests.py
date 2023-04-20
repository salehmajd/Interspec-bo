import datetime

from django.test import TestCase
from django.utils import timezone

from backoffice.models import emprunt


# Create your tests here.
class LivreModelTests(TestCase):

    def test_emprunte_recemment_avec_date_dans_le_futur(self):
        futur_time = timezone.now() + datetime.timedelta(days=30)
        e= emprunt(exemplaire=None, adherent=None, date_emprunt=futur_time, date_retour=None)
        self.assertIs(e.emprunte_recemment(), False)

    def test_emprunte_recemment_dans_un_jour(self):
        hier = timezone.now() - datetime.timedelta(days=1)
        e= emprunt(exemplaire=None, adherent=None, date_emprunt=hier, date_retour=None)
        self.assertIs(e.emprunte_recemment(), True)

    def test_en_retard_avec_date_passee(self):
        passed_time = timezone.now() - datetime.timedelta(days=30)
        e= emprunt(exemplaire=None, adherent=None, date_emprunt=None, date_retour=passed_time)
        self.assertIs(e.en_retard(), True)

    def test_en_retard_avec_date_dans_le_futur(self):
        futur_time = timezone.now() + datetime.timedelta(days=30)
        e= emprunt(exemplaire=None, adherent=None, date_emprunt=None, date_retour=futur_time)
        self.assertIs(e.en_retard(), False)

