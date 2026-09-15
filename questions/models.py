from django.db import models


class Question(models.Model):

    DEPARTMENT_CHOICES = [
        ('CSE', 'CSE'),
        ('Data Science', 'Data Science'),
        ('AIML', 'AIML'),
        ('ECE', 'ECE'),
        ('MEC', 'MEC'),
    ]

    UNIT_CHOICES = [
        ('Unit 1', 'Unit 1'),
        ('Unit 2', 'Unit 2'),
        ('Unit 3', 'Unit 3'),
        ('Unit 4', 'Unit 4'),
        ('Unit 5', 'Unit 5'),
    ]

    DIFFICULTY_CHOICES = [
        ('Easy', 'Easy'),
        ('Medium', 'Medium'),
        ('Hard', 'Hard'),
    ]

    MARKS_CHOICES = [
        (2, '2 Marks'),
        (4, '4 Marks'),
        (8, '8 Marks'),
    ]

    department = models.CharField(
        max_length=50,
        choices=DEPARTMENT_CHOICES
    )

    subject = models.CharField(max_length=100)

    unit = models.CharField(
        max_length=20,
        choices=UNIT_CHOICES
    )

    difficulty = models.CharField(
        max_length=20,
        choices=DIFFICULTY_CHOICES
    )

    marks = models.IntegerField(
        choices=MARKS_CHOICES
    )

    question_text = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.question_text[:50]