import pytest
import time 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
import requests
import json




def test_zip_run():
    my_input = "32607"
    response = requests.get(f"https://nwf.my.site.com/gfw/services/apexrest/ShopifyZipSearch?zipcode={my_input}")
    json_response = json.loads(response.content)
    #Checking the response is right for the URL
    assert response.status_code == 200
    product_list = zips(my_input)
    my_list = [i["title"] for i in json_response["product_available_sku_list"]]
    for products in product_list:
        assert products in my_list        



    #for i in json_response["product_available_sku_list"][0]:
    #    assert ["title"] == "Garden for Wildlife Eco Tote Bag"

def zips(my_input):
    if my_input == "21756":
        with open('21756.txt') as f:
            product_list = f.read().splitlines()
            return product_list
    elif my_input == "20164":
        with open("20164.txt","r") as f:
            product_list = f.read().splitlines()
            return product_list
    elif my_input == "70117":
        with open("70117.txt","r") as f:
            product_list = f.read().splitlines()
            return product_list
    elif my_input == "32607":
        with open("32607.txt","r") as f:
            product_list = f.read().splitlines()
            return product_list
    elif my_input == "75559":
        with open("75559.txt","r") as f:
            product_list = f.read().splitlines()
            return product_list

