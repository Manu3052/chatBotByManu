from contact.repositories.abstract_contact_repository import AbstractContactRepository
from contact.models import Contact

class ContactRepository(AbstractContactRepository):
    """
    Concrete implementation of the AbstractContactRepository class for managing Contact records.
    
    This repository provides CRUD operations (Create, Read, Update, Delete) for managing 
    Contact records. It interacts with the Django ORM to perform operations on the `Contact` model.
    """
    
    @staticmethod
    def create(data: dict) -> Contact:
        """
        Creates a new contact record in the database.
        
        Args:
            data (dict): A dictionary containing the data for the new contact. The dictionary 
                         should include the contact's attributes (e.g., 'name', 'cpf', 'email', etc.).
                         
        Returns:
            Contact: The created `Contact` object.
        
        Raises:
            ValueError: If the data provided is invalid or incomplete.
        """
        contact = Contact.objects.create(**data)
        contact.save()
        return contact

    @staticmethod
    def update(contact: Contact, message_data: dict) -> None:
        """
        Updates an existing contact record with the provided data.
        
        Args:
            contact (Contact): The `Contact` object to be updated.
            message_data (dict): A dictionary containing the new data for the contact.
            
        Raises:
            ValueError: If the data provided is invalid or incomplete.
        """
        chat = message_data.pop("chat")
        for key, value in message_data.items():
            setattr(contact, key, value)
        contact.chat.set(chat[0])  # Assuming 'chat' is a related model
        contact.save()

    @staticmethod
    def get_by_id(contact_id: int) -> Contact:
        """
        Retrieves a contact by its ID.
        
        Args:
            contact_id (int): The ID of the contact to be retrieved.
        
        Returns:
            Contact: The `Contact` instance corresponding to the provided ID. Returns None 
                     if no contact is found.
        """
        contact = Contact.objects.filter(id=contact_id).first()
        return contact

    @staticmethod
    def get_by_name(name: str) -> Contact:
        """
        Retrieves a contact by its name.
        
        Args:
            name (str): The name of the contact to be retrieved.
        
        Returns:
            Contact: The `Contact` instance corresponding to the provided name. Returns None 
                     if no contact is found.
        """
        contact = Contact.objects.filter(name=name).first()
        return contact

    @staticmethod
    def delete(contact_id: int) -> None:
        """
        Deletes the contact record with the given ID.
        
        Args:
            contact_id (int): The ID of the contact to be deleted.
        
        Raises:
            DoesNotExist: If no contact with the given ID exists.
        """
        Contact.objects.filter(id=contact_id).delete()

    @staticmethod
    def get_all() -> list[Contact]:
        """
        Retrieves all contact records from the database.
        
        Returns:
            list[Contact]: A list of all `Contact` objects.
        """
        contacts = Contact.objects.all()
        return contacts
