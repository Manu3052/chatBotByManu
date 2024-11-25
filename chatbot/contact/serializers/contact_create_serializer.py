from rest_framework import serializers
from contact.models import Contact


class ContactCreateSerializer(serializers.ModelSerializer):
    """
    Serializer for the Contact model where only the `name` field is required.
    Optional fields include `cpf`, `telephone`, and `email`.
    """

    class Meta:
        model = Contact
        fields = ['id', 'cpf', 'telephone', 'email', 'name']
        extra_kwargs = {
            'cpf': {'required': False, 'allow_null': True},
            'telephone': {'required': False, 'allow_null': True},
            'email': {'required': False, 'allow_null': True},
            'name': {'required': True, 'allow_null': False},
        }