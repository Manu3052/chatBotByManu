import pytest
from rest_framework.test import APIClient
from rest_framework import status
from contact.models import Contact
from unittest.mock import patch

@pytest.fixture
def create_contact():
    return Contact.objects.create(
        name="John Doe",
        email="johndoe@example.com",
        cpf="12345678901",
        telephone="987654321"
    )

@pytest.fixture
def client():
    return APIClient()

def test_create_contact(client):
    url = '/contacts/'
    data = {
        'name': 'Jane Doe',
        'email': 'janedoe@example.com',
        'cpf': '10987654321',
        'telephone': '123456789'
    }
    response = client.post(url, data, format='json')
    assert response.status_code == status.HTTP_201_CREATED
    assert response.data['contact_created'] == True

def test_partial_update_contact(client, create_contact):
    url = f'/contacts/{create_contact.id}/'
    data = {'telephone': '111222333'}
    response = client.patch(url, data, format='json')
    create_contact.refresh_from_db()
    assert response.status_code == status.HTTP_200_OK
    assert create_contact.telephone == '111222333'

def test_list_contacts(client):
    url = '/contacts/'
    response = client.get(url, format='json')
    assert response.status_code == status.HTTP_200_OK
    assert len(response.data['results']) > 0

def test_destroy_contact(client, create_contact):
    url = f'/contacts/{create_contact.id}/'
    response = client.delete(url, format='json')
    assert response.status_code == status.HTTP_200_OK
    assert response.data['contact_deleted'] == True
    assert not Contact.objects.filter(id=create_contact.id).exists()

@patch('contact.services.contact_service.ContactService.get_contact_by_name')
def test_get_by_name(client, mock_get_contact_by_name, create_contact):
    url = f'/contacts/get_by_name/John Doe/'
    mock_get_contact_by_name.return_value = [create_contact]
    response = client.get(url, format='json')
    assert response.status_code == status.HTTP_200_OK
    assert len(response.data['results']) == 1
    assert response.data['results'][0]['name'] == 'John Doe'

def test_create_contact_invalid_data(client):
    url = '/contacts/'
    data = {'email': 'invalidemail'}
    response = client.post(url, data, format='json')
    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert 'error' in response.data

def test_update_contact_not_found(client):
    url = '/contacts/999/'
    data = {'telephone': '333444555'}
    response = client.patch(url, data, format='json')
    assert response.status_code == status.HTTP_404_NOT_FOUND

def test_destroy_contact_not_found(client):
    url = '/contacts/999/'
    response = client.delete(url, format='json')
    assert response.status_code == status.HTTP_404_NOT_FOUND
