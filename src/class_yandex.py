import requests

url = "https://cloud-api.yandex.net/v1/disk/resources"

class YandexDisk:

    def __init__(self, token):
        self.token = token
        self.url = 'https://cloud-api.yandex.net/v1/disk/resources/'
    
    
    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)
        }
    

    def create_folder(self,path = 'T_TEST'):

        
         headers = self.get_headers()
         response = requests.put(f'{url}?path={path}', headers=headers) 
         return response.status_code
    
    
    def delete_folder(self,path = 'T_TEST'):   

        headers = self.get_headers()
        response = requests.delete(f'{url}?path={path}', headers=headers) 
        return 
    
    def get_folder_existance(self,folder_name = 'T_TEST'):


        headers = self.get_headers()
        params = {'path': folder_name}
        response = requests.get(url, headers=headers, params=params)
        return response.status_code
        
        
    