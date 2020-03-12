import requests

class Hive:
    def __init__(self, api_key, default_format = 'screen_name', host = 'https://hive.one/'):
        if len(api_key) == 0: raise Exception('You must provide an API Key')
        self.api_key = api_key
        self.default_format = default_format
        self.host = host
    

    def available_influencers(self, id_format = None, etag = ''):
        if id_format is None:
            id_format = self.default_format
        else:
            if id_format not in ["screen_name", "id"]:
                raise Exception("{passed_id_format} is not one of: screen_name, id".format(passed_id_format=id_format))
        
        response = requests.get(
            "{host}api/v1/influencers/".format(host=self.host),
            headers={
                "Authorization": "Token {api_key}".format(api_key=self.api_key),
                "If-None-Match": etag
            }
        )

        if response.status_code == 200:
            data = response.json()
            
            def return_id(id_arr):
                return id_arr[0 if self.default_format == 'id' else 1]
            return list(map(return_id, data['data']['available']))
        elif response.status_code == 304:
            return True
        else:
            pass

    def top_influencers(self):
        pass
    
    def influencer_details(self):
        pass
    
    def influencer_history(self):
        pass
    
    def influencer_podcasts(self):
        pass
    
    def influencer_batch(self):
        pass