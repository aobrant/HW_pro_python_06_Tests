from unittest import result
import pytest
import configparser
from src.class_yandex import YandexDisk



config = configparser.ConfigParser()
config.read("config.ini")
TOKEN_YD=(config.get('YandexDisc','token'))

class Test_YD:
    # def setup(self):
    #
    #
    #     Yad = YandexDisk(TOKEN_YD)
    #     YandexDisk.delete_folder(Yad)

    def setup(self):

        print("setup ==>")
    def teardown(self):

        print('Fin')
        Yad = YandexDisk(TOKEN_YD)
        YandexDisk.delete_folder(Yad)

    
    def test_yd_create(self):


        Yad = YandexDisk(TOKEN_YD)

        test_result = YandexDisk.create_folder(Yad)
        result = 201

        assert test_result == result
    def test_yd_wrong_token(self):

        Yad = YandexDisk('sdwsfdsf')

        test_result = YandexDisk.create_folder(Yad)
        result = 401
        assert test_result == result






