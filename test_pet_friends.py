from api import PetFriends
from settings import valid_email, valid_password, wrong_password, wrong_email

pf = PetFriends()

def test_get_api_key_for_valid_user(email = valid_email, password = valid_password):
    status, result = pf.get_api_key(email, password)
    assert status == 200
    assert 'key' in result

def test_get_all_pets_with_valid_key(filter=''):
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.get_list_of_pets(auth_key, filter)
    assert status == 200
    assert len(result['pets'])>0

def test_add_new_pet_with_valid_data(name='vasia', animal_type='cat',
                                     age='7', pet_photo='images/pet.jpg'):
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)

    assert status == 200
    assert result['name'] == name

def test_add_new_pet_simple_with_valid_data(name='crug', animal_type='brug',age='4'):

    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet_simple(auth_key, name, animal_type, age)

    assert status == 200
    assert result['name'] == name

def test_add_photo_to_pet( pet_photo='images/pet.jpg'):

    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")
    if len(my_pets['pets']) > 0:
        status, result = pf.add_photo_to_pet(auth_key,my_pets['pets'][0]['id'], pet_photo)
        assert status == 200
        assert result ['pet_photo']  !=0
    else:
        raise Exception ("No pets")

def test_get_api_key_for_invalid_username(email = valid_email, password = wrong_password):
    status, result = pf.get_api_key(email, password)
    assert status == 403
    if status != 200:
        raise Exception("Invalid email or password")

def test_get_api_key_for_invalid_username(email = wrong_email, password = valid_password):
    status, result = pf.get_api_key(email, password)
    assert status == 403
    if status != 200:
        raise Exception("Invalid email or password")

def test_add_new_pet_with_valid_data(name='vasia', animal_type='cat',
                                     age='very_old', pet_photo='images/pet.jpg'):
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)

    assert status == 200
    assert result['name'] == name
    if status == 200:
        raise Exception ("Invalid age field")

def test_add_new_pet_with_valid_data(name='', animal_type='cat',
                                     age='7', pet_photo='images/pet.jpg'):
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)

    assert status == 200
    assert result['name'] == name
    if status == 200:
        raise Exception ("Empty field name")

def test_add_new_pet_with_valid_data(name='Bob', animal_type='',
                                     age='7', pet_photo='images/pet.jpg'):
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)

    assert status == 200
    assert result['name'] == name
    if status == 200:
        raise Exception ("Empty field animal_type")

def test_add_new_pet_with_valid_data(name='Bob', animal_type='cat',
                                     age='', pet_photo='images/pet.jpg'):
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)

    assert status == 200
    assert result['name'] == name
    if status == 200:
        raise Exception ("Empty field age")