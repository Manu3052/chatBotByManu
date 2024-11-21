from django.db import models


class Contact(models.Model):
    """
    Model to store contact information.
    Fields:
        - id: Unique identifier for each contact (Primary Key).
        - cpf: CPF of the contact (optional).
        - telephone: Telephone number of the contact (optional).
        - email: Unique and non-null email address of the contact.
        - name: Full name of the contact (non-null).
    """
    id = models.AutoField(primary_key=True)
    cpf = models.CharField(max_length=11, blank=True, null=True)
    telephone = models.CharField(max_length=15, blank=True, null=True)
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=255)

    def __str__(self):
        """
        Return the full name of the contact as a string.
        """
        return self.name
