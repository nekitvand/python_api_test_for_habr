import pytest
import requests
import logging


@pytest.mark.full
@pytest.mark.smoke
def test_cat_facts():
    query = {"animal_type": "cat", "amount": "2"}
    response = requests.get("https://cat-fact.herokuapp.com/facts/random", params=query)
    logging.info(f"Request url: {response.request.url}, body: {response.request.body}")
    logging.info(f"Request status: {response.status_code}, body: {response.text}")
    assert response.status_code == 200

@pytest.mark.full
@pytest.mark.smoke
def test_dog_facts():
    query = {"animal_type": "dog", "amount": "2"}
    response = requests.get("https://cat-fact.herokuapp.com/facts/random", params=query)
    logging.info(f"Request url: {response.request.url}, body: {response.request.body}")
    logging.info(f"Request status: {response.status_code}, body: {response.text}")
    assert response.status_code == 200


@pytest.mark.full
def test_horse_facts():
    query = {"animal_type": "horse", "amount": "2"}
    response = requests.get("https://cat-fact.herokuapp.com/facts/random", params=query)
    logging.info(f"Request url: {response.request.url}, body: {response.request.body}")
    logging.info(f"Request status: {response.status_code}, body: {response.text}")
    assert response.status_code == 200

@pytest.mark.bird
def test_bird_facts():
    query = {"animal_type": "bird", "amount": "2"}
    response = requests.get("https://cat-fact.herokuapp.com/facts/random", params=query)
    logging.info(f"Request url: {response.request.url}, body: {response.request.body}")
    logging.info(f"Request status: {response.status_code}, body: {response.text}")
    assert response.status_code == 200