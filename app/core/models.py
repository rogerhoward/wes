import uuid

from django.conf import settings
from django.db import models
from django.urls import reverse
from django.utils.functional import cached_property

# --------------------------------------------------
# Abstract base classes
# --------------------------------------------------

class GenericBaseClass(models.Model):
    """
    The standard abstract base class for primary classes provides basic fields and infrastructure for
    all Model classes in this project
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    rec_updated = models.DateTimeField(auto_now=True, null=True, blank=True, help_text='The datetime this actual object was updated.', )
    rec_created = models.DateTimeField(auto_now_add=True, null=True, blank=True, help_text='The datetime this actual object was created.', )

    class Meta:
        abstract = True
        get_latest_by = '-datetime_updated'
        indexes = [
            models.Index(fields=['rec_updated']),
            models.Index(fields=['rec_created']),
        ]


# --------------------------------------------------
# Treatment Groups
# --------------------------------------------------

class Group(GenericBaseClass):
    """
    A group of treatments.
    """
    inpatient = models.BooleanField()
    start_date = models.DateField(null=True, blank=True, )
    end_date = models.DateField(null=True, blank=True, )

    class Meta:
        abstract = False
        indexes = [
            models.Index(fields=['inpatient']),
            models.Index(fields=['start_date']),
            models.Index(fields=['end_date']),
            models.Index(fields=['start_date', 'end_date']),
            ]

    def __str__(self):
        return f"group {self.id}"

    # def get_absolute_url(self):
    #     return reverse('core-asset-detail', args=[str(self.pk)])



class Treatment(GenericBaseClass):
    """
    An instance of treatment.
    """
    group = models.ForeignKey('Group', on_delete=models.CASCADE, null=True, blank=True, )

    kind = models.TextField(null=False, blank=False, )

    start_date = models.DateField(null=True, blank=True, )
    end_date = models.DateField(null=True, blank=True, )

    class Meta:
        abstract = False
        indexes = [
            models.Index(fields=['start_date']),
            models.Index(fields=['end_date']),
            models.Index(fields=['start_date', 'end_date']),
        ]

    def __str__(self):
        return f"{self.kind} on {self.start_date}"



