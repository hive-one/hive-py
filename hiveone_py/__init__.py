import requests
import json

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

    def top_influencers(self, cluster = 'Crypto', after = 0, sort_by = 'rank', order = 'asc', etag = ''):
        sort_map = [
            'followers',
            'following',
            'screen_name',
            'change_week',
            'score',
            'rank',
        ]
        if cluster not in ['Crypto', 'BTC', 'ETH', 'XRP']:
            raise Exception("{passed_cluster} is not one of: Crypto, BTC, ETH, XRP".format(passed_cluster=cluster))
        if type(after) != int:
            raise Exception("after should be type int")
        if sort_by not in sort_map:
            raise Exception("Sort: {passed_sort} is not supported`".format(passed_sort=sort_by))
        if order not in ['asc', 'desc']:
            raise Exception("Order: {passed_order} is not supported".format(passed_order=order))
        response = requests.get(
            "{host}api/v1/influencers/top/".format(host=self.host),
            headers={
                "Authorization": "Token {api_key}".format(api_key=self.api_key),
                "If-None-Match": etag
            },
            params=(
                ('cluster', cluster),
                ('after', after),
                ('sort_by', sort_by),
                ('order', order)
            )
        )

        if response.status_code == 200:
            data = response.json()
            
            def return_node(item):
                return item['node']
            return list(map(return_node, data['data']['people']['edges']))
        elif response.status_code == 304:
            return True
        else:
            pass
    
    def influencer_details(self, influencer_id = None, id_format = None, rank_type = 'all', include_followers = 0, etag = ''):
        if influencer_id is None:
            raise Exception('You must provide an influencers ID')
        if id_format is None:
            id_format = self.default_format
        else:
            if id_format not in ["screen_name", "id"]:
                raise Exception("{passed_id_format} is not one of: screen_name, id".format(passed_id_format=id_format))
        response = requests.get(
            "{host}api/v1/influencers/{id_format}/{influencer_id}".format(
                host=self.host,
                id_format=id_format,
                influencer_id=influencer_id
            ),
            headers={
                "Authorization": "Token {api_key}".format(api_key=self.api_key),
                "If-None-Match": etag
            },
            params=(
                ('rank_type', rank_type),
                ('include_followers', include_followers),
            )
        )

        if response.status_code == 200:
            data = response.json()
            
            return data
        elif response.status_code == 304:
            return True
        else:
            pass
    
    def influencer_history(self, influencer_id = None, id_format = None, rank_type = 'all', etag = ''):
        if influencer_id is None:
            raise Exception('You must provide an influencers ID')
        if id_format is None:
            id_format = self.default_format
        else:
            if id_format not in ["screen_name", "id"]:
                raise Exception("{passed_id_format} is not one of: screen_name, id".format(passed_id_format=id_format))
        
        response = requests.get(
            "{host}api/v1/influencers/{id_format}/{influencer_id}/history/".format(
                host=self.host,
                id_format=id_format,
                influencer_id=influencer_id
            ),
            headers={
                "Authorization": "Token {api_key}".format(api_key=self.api_key),
                "If-None-Match": etag
            },
            params=(
                ('rank_type', rank_type),
            )
        )

        if response.status_code == 200:
            data = response.json()
            
            return data
        elif response.status_code == 304:
            return True
        else:
            pass
        
    
    def influencer_podcasts(self, influencer_id = None, id_format = None, appearance_type = 'all', after = 0, etag = ''):
        if influencer_id is None:
            raise Exception('You must provide an influencers ID')
        if id_format is None:
            id_format = self.default_format
        else:
            if id_format not in ["screen_name", "id"]:
                raise Exception("{passed_id_format} is not one of: screen_name, id".format(passed_id_format=id_format))
        
        response = requests.get(
            "{host}api/v1/influencers/{id_format}/{influencer_id}/podcasts/".format(
                host=self.host,
                id_format=id_format,
                influencer_id=influencer_id
            ),
            headers={
                "Authorization": "Token {api_key}".format(api_key=self.api_key),
                "If-None-Match": etag
            },
            params=(
                ('appearance_type', appearance_type),
                ('after', after),
            )
        )

        if response.status_code == 200:
            data = response.json()
            
            return data
        elif response.status_code == 304:
            return True
        else:
            pass
    
    def influencer_batch(self, influencer_ids = [], rank_type = 'all', include_followers = 0):
        response = requests.get(
            "{host}api/v1/influencers/batch/".format(
                host=self.host,
            ),
            headers={
                "Authorization": "Token {api_key}".format(api_key=self.api_key)
            },
            params=(
                ('twitter_ids', json.dumps(influencer_ids)),
                ('rank_type', rank_type),
                ('include_followers', include_followers),
            )
        )

        if response.status_code == 200:
            data = response.json()
            
            return data['data']['success']
        elif response.status_code == 304:
            return True
        else:
            pass