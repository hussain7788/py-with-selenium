from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.


class Company(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name

@receiver(post_save, sender=Company)
def create_programmer(sender, instance, created, **kwargs):

    l_names = ['hussain', 'valli', 'anil', 'sunil']

    if created:
        for name in l_names:
            if not Programmer.objects.filter(name=name).exists():
                Programmer.objects.create(name=name, company= instance)
                print("Programmer was Created..........")
                break

# post_save.connect(receiver=create_programmer, sender=Company)

class Language(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name

class Programmer(models.Model):
    name = models.CharField(max_length=50)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, default=True, null=True)
    language = models.ManyToManyField(Language, null=True)

    def __str__(self) -> str:
        return self.name

## Adding language to Every Programmer
@receiver(post_save, sender=Language)
def create_language_for_programmer(sender, instance, created, **kwargs):

    if created:
        l_programmers = Programmer.objects.all()
        for pro in l_programmers:
            pro.language.add(instance)
            pro.save()
            print("Successfully added language to all Programmers...")
