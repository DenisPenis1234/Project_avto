import sender_stand_request

import data


def test_post1():
    assert sender_stand_request.post_new_client_kit(data.kit_body).status_code == 201
    assert sender_stand_request.post_new_client_kit(data.kit_body).json()["name"] == data.kit_body["name"]

def test_post2():
    
    sender_stand_request.put_new_name_to_kit_body("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC")
    assert sender_stand_request.post_new_client_kit(data.kit_body).status_code == 201
    assert sender_stand_request.post_new_client_kit(data.kit_body).json()["name"] == data.kit_body["name"]

def test_post3():
    
    sender_stand_request.put_new_name_to_kit_body("")
    assert sender_stand_request.post_new_client_kit(data.kit_body).status_code == 400

def test_post4():
    
    sender_stand_request.put_new_name_to_kit_body("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD")
    assert sender_stand_request.post_new_client_kit(data.kit_body).status_code == 400

def test_post5():
    sender_stand_request.put_new_name_to_kit_body("QWErty")
    assert sender_stand_request.post_new_client_kit(data.kit_body).status_code == 201
    assert sender_stand_request.post_new_client_kit(data.kit_body).json()["name"] == data.kit_body["name"]

def test_post6():
    sender_stand_request.put_new_name_to_kit_body("Мария")
    assert sender_stand_request.post_new_client_kit(data.kit_body).status_code == 201
    assert sender_stand_request.post_new_client_kit(data.kit_body).json()["name"] == data.kit_body["name"]

def test_post7():
    sender_stand_request.put_new_name_to_kit_body("№%@№%@")
    assert sender_stand_request.post_new_client_kit(data.kit_body).status_code == 201
    assert sender_stand_request.post_new_client_kit(data.kit_body).json()["name"] == data.kit_body["name"]

def test_post8():
    sender_stand_request.put_new_name_to_kit_body(" Человек и КО ")
    assert sender_stand_request.post_new_client_kit(data.kit_body).status_code == 201
    assert sender_stand_request.post_new_client_kit(data.kit_body).json()["name"] == data.kit_body["name"]

def test_post9():
    sender_stand_request.put_new_name_to_kit_body("123")
    assert sender_stand_request.post_new_client_kit(data.kit_body).status_code == 201
    assert sender_stand_request.post_new_client_kit(data.kit_body).json()["name"] == data.kit_body["name"]

def test_post10():
    data.kit_body.pop("name")
    assert sender_stand_request.post_new_client_kit(data.kit_body).status_code == 400
def test_post11():
    sender_stand_request.put_new_name_to_kit_body(123)
    assert sender_stand_request.post_new_client_kit(data.kit_body).status_code == 400
    