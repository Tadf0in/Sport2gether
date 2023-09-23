from django.db import models
from django.contrib.auth.models import User
from sport_api.models import Sport   


class AppUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

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

    friends = models.ManyToManyField(User, related_name='friends', blank=True)
    sports = models.ManyToManyField(Sport, related_name='sports', blank=True)

    def get_friends(self):
        return self.friends.all()
    
    def get_sports(self):
        return self.sports.all()

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name ='App User'
        verbose_name_plural ='App Users'


class FeedBack(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    raison_choice = models.CharField(
        max_length=3,
        choices=[
            ("ami", "Un ami m'en a parlé"),
            ("pub", "Une publicité"),
            ("app", "Depuis l'AppStore"),
            ("oth", "Autre")
        ],
        default="oth"
    )
    raisons = models.CharField(max_length=128, blank=True)

    attente_choice = models.CharField(
        max_length=3,
        choices=[
            ("ren", "Faire des rencontres"),
            ("mot", "Trouver de la motivation"),
            ("oth", "Autre")
        ],
        default="oth"
    )
    attentes = models.CharField(max_length=128, blank=True)

    class Meta:
        verbose_name ='Feedback'
        verbose_name_plural ='Feedbacks'


class FriendRequest(models.Model):
    from_user = models.ForeignKey(User, related_name='from_user', on_delete=models.CASCADE)
    to_user = models.ForeignKey(User, related_name='to_user', on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True, editable=False)

    class Meta:
        unique_together = ('from_user', 'to_user')