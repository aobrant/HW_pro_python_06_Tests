import unittest
from src.main import documents,directories,  get_doc_owner_name, check_document_existance
from parameterized import parameterized



class TestFunction(unittest.TestCase):
    @parameterized.expand(
        [
        (1, False),
        (10006, False),
        ("2207 876234",True)
        ]
    )

    def test_check_document_existance(self, a, result):

       calc_result = check_document_existance(a)
       self.assertEqual(calc_result, result)
    
    
    @parameterized.expand(
        [
        ("10006","Аристарх Павлов" ),
        ("2207 876234",  "Василий Гупкин"),
        ]
    )
    def test_get_doc_owner_name(self,a,result):

        calc_result = get_doc_owner_name(a) 
        self.assertEqual(calc_result, result)
       
        

       