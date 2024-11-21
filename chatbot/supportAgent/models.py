from django.db import models
from django.contrib.auth.hashers import make_password

class SupportAgent(models.Model):
    """
    Model representing a support agent in the system.

    Attributes:
        id (int): Unique identifier for the agent (Primary Key).
        first_name (str): The agent's first name. Required field.
        last_name (str): The agent's last name. Required field.
        password (str): The agent's password, stored as a secure hash. Required field.
    """
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50, null=False, blank=False)
    last_name = models.CharField(max_length=50, null=False, blank=False)
    password = models.CharField(max_length=128, null=False, blank=False)

    def save(self, *args, **kwargs):
        """
        Overriding the save method to hash the password before saving to the database.
        """
        if not self.pk or not self.password.startswith("pbkdf2_"):
            self.password = make_password(self.password)
        super().save(*args, **kwargs)

    def __str__(self):
        """
        Returns a string representation of the agent, using their full name.
        """
        return f"{self.first_name} {self.last_name}"
