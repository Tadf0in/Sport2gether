from django.db import models
from django.contrib.auth.models import User



class Sport(models.Model):
    abrev = models.CharField(max_length=5, unique=True)
    name = models.CharField(max_length=128, unique=True)
    icon_url = models.URLField(max_length=128, blank=True)

    def __str__(self):
        return self.name
    


class AppUser(models.Model):
    user_id = models.OneToOneField(User, on_delete=models.CASCADE)

    age = models.PositiveSmallIntegerField()
    sexe = models.CharField(
        max_length=1,
        choices = [('H', "Homme"), ("F", "Femme")],
        null=True, blank=True
    )
    ville = models.CharField(max_length=128)
    tel = models.CharField(max_length=15, blank=True, null=True)

    FREQUENCE_ENTRAINEMENT_CHOICES = [
        ("tlj", "Très élevée (Tous les jours)"),
        ("elv", "Élevée (4 à 5 fois par semaine)"),
        ("nrm", "Normale (2 à 3 fois par semaine)"),
        ("bas", "Basse (1 fois par semaine)"),
        ("tet", "Très basse (De temps en temps)"),
        ("non", "Non renseignée"),
        ("var", "Variable")
    ]
    frequence_entrainement = models.CharField(
        max_length=3,
        choices=FREQUENCE_ENTRAINEMENT_CHOICES,
        default="non",
    )
    objectif_court_terme = models.CharField(max_length=128, blank=True)
    objectif_long_terme = models.CharField(max_length=128, blank=True)
    plus_gros_defi_releve = models.CharField(max_length=128, blank=True)

    def __str__(self):
        return self.user_id.username
    
    class Meta:
        verbose_name ='App User'
        verbose_name_plural ='App Users'



class UserSports(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    sport_id = models.ForeignKey(Sport, on_delete=models.CASCADE)

    def __str__(self):
        return self.user_id.username  + " - " + self.sport_id.name

    class Meta:
        verbose_name ='User Sports'
        verbose_name_plural ='Users Sports'



class FeedBack(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

    raison_choice = models.CharField(
        max_length=3,
        choices=[
            ("oth", "Autre")
        ]
    )
    raisons = models.CharField(max_length=128, blank=True)

    attente_choice = models.CharField(
        max_length=3,
        choices=[
            ("oth", "Autre")
        ]
    )
    attentes = models.CharField(max_length=128, blank=True)

    class Meta:
        verbose_name ='Feedback'
        verbose_name_plural ='Feedbacks'