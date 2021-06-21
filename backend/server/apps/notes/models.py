from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.fields import AutoField
from django.utils.translation import gettext as _

User = get_user_model()


class Book(models.Model):

    class Category(models.TextChoices):
        HISTORY = 'HISTORY', _('Historical')
        PROPHETS = 'PROPHETS', _('Prophetic')
        POETIC = 'POETIC', _('Poetic and Other Writings')
        PAUL = 'PAUL', _("Paul's Letters")
        LETTERS = 'LETTERS', _('Letters from Others')

    class Testament(models.TextChoices):
        OLD_TESTAMENT = 'OT', _('Old Testament')
        NEW_TESTAMENT = 'NT', _('New Testament')

    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    abbreviation = models.CharField(max_length=10, unique=True, blank=True)
    symbol = models.CharField(max_length=3, unique=True, blank=True)
    category = models.CharField(
        max_length=12, choices=Category.choices, default=Category.HISTORY)
    testament = models.CharField(
        max_length=2, choices=Testament.choices, default=Testament.OLD_TESTAMENT)
    canonical_order = models.PositiveSmallIntegerField(default=1)
    chronological_order = models.PositiveSmallIntegerField(default=1)

    def __str__(self):
        return self.name


class Note(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    updated_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=50, blank=True)
    reference = models.CharField(max_length=20, blank=True)
    content = models.TextField(blank=True)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, default=1)
    sort_order = models.PositiveSmallIntegerField(default=1)

    def __str__(self):
        return self.title
