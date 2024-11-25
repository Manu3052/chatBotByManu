from rest_framework import serializers
from contact.models import Contact

class ContactListSerializer(serializers.ModelSerializer):
    """
    Serializer for the Contact model.

    Purpose:
        - Converts Contact model instances to JSON format (serialization).
        - Validates and creates Contact model instances from JSON data (deserialization).

    Fields:
        - id (int): Auto-generated unique identifier for the contact (primary key, inherited from the model).
        - name (str): Full name of the contact (required).
        - email (str): Email address of the contact (optional).
        - cpf (str): CPF of the contact (optional).
        - telephone (str): Telephone number of the contact (optional).
    """

    class Meta:
        """
        Meta configuration for the ContactListSerializer.

        Attributes:
            - model (Contact): Specifies the model class that this serializer corresponds to.
            - fields (list): Defines the fields to be included in the serialized output or deserialized input.
        """
        model = Contact
        fields = [
            'id',
            'name',
            'email',
            'cpf',
            'telephone',
        ]
