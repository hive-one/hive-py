# Hive PY


## Install

1. Sign up for an Account at [hive.one](https://hive.one/)
2. Get an API Key [here](https://hive.one/api/)
3. Install via `pip`
```
pip install hiveone-py
```


## Usage
Import into your project
```python 
from hiveone_py import Hive
api_client = Hive(API_KEY_HERE)
```

### [**List Available Influencers**](https://docs.hive.one/core-resources/available)
```python
# Default
response = api_client.available_influencers()

# Requesting twitter_id's
response = api_client.available_influencers(id_format: 'id')

```
Argument | Required | Default | Options | Purpose
--- | --- | --- | --- | --- 
`id_format` | No | `screenName` | `screenName`, `id` | Change the format of the influencer ID

### [**Top Influencers**](https://docs.hive.one/core-resources/top-influencers)
```python
# Default
response = api_client.top_influencers()

# BTC with pagination
response = api_client.top_influencers(cluster: 'BTC', after: 50)
```
Argument | Required | Default | Options | Purpose
--- | --- | --- | --- | --- 
`cluster` | No | `Crypto` | `Crypto`, `BTC`, `ETH`, `XRP` | Specify the cluster you want the top influencers for
`after` | No | `0` | Multiples of `50` | Used for pagination

### [**Influencer Details**](https://docs.hive.one/core-resources/profile-details-twitter-screen-name)
```python
# Default
response = api_client.influencer_details(influencer_id: 'jack')

# Personal Rank Type
response = api_client.influencer_details(influencer_id: 'jack', rank_type: 'personal')

# Include Followers
response = api_client.influencer_details(influencer_id: 'jack', include_followers: 1)

# Request using twitter_id
response = api_client.influencer_details(influencer_id: '12', id_format: 'id')
```
Argument | Required | Default | Options | Purpose
--- | --- | --- | --- | --- 
`influencer_id` | Yes |  | | Unique ID (Screen Name or Twitter ID) for the influencer you are requesting.
`id_format` | No | `screenName` | `screenName`, `id` | Change the format of the influencer ID
`rank_type` | No | `all` | `all`, `personal` | People are treated differently from other types of influencers (Companies, bots, etc.), if you request `all` an influencers rank/score will reflect their influence across the entire cluster, if you request `personal` their rank/score will reflect their influence across other people in the cluster.
`include_followers` | No | `0` | `0`, `1` | Allows you to get top followers for the requested influencer.

### [**Influencer Rank/Score History**](https://docs.hive.one/core-resources/influencer-rank-score-history-twitter-screen-name)
```python
# Default
response = api_client.influencer_history(influencer_id: 'jack')

# Personal Rank Type
response = api_client.influencer_history(influencer_id: 'jack', rank_type: 'personal')

# Request using twitter_id
response = api_client.influencer_history(influencer_id: '12', id_format: 'id')
```
Argument | Required | Default | Options | Purpose
--- | --- | --- | --- | --- 
`influencer_id` | Yes |  | | Unique ID (Screen Name or Twitter ID) for the influencer you are requesting.
`id_format` | No | `screenName` | `screenName`, `id` | Change the format of the influencer ID
`rank_type` | No | `all` | `all`, `personal` | People are treated differently from other types of influencers (Companies, bots, etc.), if you request `all` an influencers rank/score will reflect their influence across our entire dataset, if you request `personal` their rank/score will reflect their infulencer across other people.


### [**Influencers Podcasts**](https://docs.hive.one/core-resources/influencer-podcasts-twitter-screen-name)
```python
# Default
response = api_client.influencer_podcasts(influencer_id: 'jack')

# appearance_type
response = api_client.influencer_podcasts(influencer_id: 'jack', rank_type: 'personal')

# Pagination
response = api_client.influencer_podcasts(influencer_id: 'jack', after: 20)

# Request using twitter_id
response = api_client.influencer_podcasts(influencer_id: '12', id_format: 'id')
```
Argument | Required | Default | Options | Purpose
--- | --- | --- | --- | --- 
`influencer_id` | Yes |  | | Unique ID (Screen Name or Twitter ID) for the influencer you are requesting.
`id_format` | No | `screenName` | `screenName`, `id` | Change the format of the influencer ID
`appearance_type` | No | `all` | `all`, `host`, `guest` | Allows you to filter podcasts whether the requested influencer was a `host` or a `guest`
`after` | No | `0` | Multiples of `20` | Used for pagination

### [**Batch Influencer Details**](https://docs.hive.one/core-resources/batch-profile-details-twitter-id)
```python
# Default
response = api_client.influencer_batch(influencer_ids: [123, 123])
```
Argument | Required | Default | Options | Purpose
--- | --- | --- | --- | --- 
`influencer_ids` | Yes |  | | An array of twitter_ids for the influencers you want to retrieve.
`rank_type` | No | `all` | `all`, `personal` | People are treated differently from other types of influencers (Companies, bots, etc.), if you request `all` an influencers rank/score will reflect their influence across our entire dataset, if you request `personal` their rank/score will reflect their infulencer across other people.
`include_followers` | No | `0` | `0`, `1` | Allows you to get top followers for the requested influencer.


## Changing Defaults
You can change the defaults when initializing the library

You can change the default infleuncerID format like so:
```python
from hiveone_py import Hive
api_client = Hive(api_key=API_KEY_HERE, default_format='id')
```

You can also change the host the library connects to (Useful if you are caching hive.one data)
```python
from hiveone_py import Hive
api_client = Hive(api_key=API_KEY_HERE, host='https://hosthere/')
```


## Contributions

1. Reports for issues and suggestions can be made using the [issue submission](https://github.com/hive-one/hive-py/issues) interface.
2. Code contributions are submitted via [pull requests](https://github.com/hive-one/hive-py/pulls)