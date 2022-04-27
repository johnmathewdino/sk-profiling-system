from django.db import models

# Create your models here.
class Profile (models.Model):
    education_level_choices = (

        ("College","College"),
        ("High School","High School"),
        ("Elementary","Elementary"),
        ("Kindergarten", "Kindergarten"),
        ("Day Care", "Day Care"),
        ("Out of School","Out of School"),
        ("Graduates","Graduates")
    )
    education_year_choices = (
        ("K1", "K1"),
        ("K2", "K2"),
        ("Grade 1","Grade 1"),
        ("Grade 2", "Grade 2"),
        ("Grade 3", "Grade 3"),
        ("Grade 4", "Grade 4"),
        ("Grade 5", "Grade 5"),
        ("Grade 6", "Grade 6"),
        ("Grade 7", "Grade 7"),
        ("Grade 8", "Grade 8"),
        ("Grade 9", "Grade 9"),
        ("Grade 10", "Grade 10"),
        ("Grade 11", "Grade 11"),
        ("Grade 12", "Grade 12"),
        ("1st Year", "1st Year"),
        ("2nd Year", "2nd Year"),
        ("3rd Year", "3rd Year"),
        ("4th Year", "4th Year"),
        ("5th Year", "5th Year"),
    )
    sex_choices = (
        ("Male","Male"),
        ("Female","Female"),
    )
    full_name = models.CharField(max_length=250)
    first_name = models.CharField(max_length=250)
    middle_name = models.CharField(max_length=250, null=True, blank=True)
    last_name = models.CharField(max_length=250)
    birthday = models.DateField(null=True, blank=True)
    age = models.IntegerField( null=True, blank=True)
    education_level = models.CharField(max_length=250, choices=education_level_choices)
    education_year = models.CharField(max_length=250, choices=education_year_choices,null=True, blank=True)
    school = models.CharField(max_length=250, null=True, blank=True)
    sex = models.CharField(max_length=250, null=True, blank=True, choices=sex_choices)
    purok = models.CharField(max_length=250, null=True, blank=True)
    slug = models.SlugField(max_length=250)

    def __str__(self):
        return self.full_name

