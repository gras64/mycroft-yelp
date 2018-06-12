from test.integrationtests.skills.skill_tester import SkillTest
from unittest.mock import MagicMock, patch
from mycroft.util.log import getLogger

LOGGER = getLogger(__name__)

json_response = {'businesses': [{'alias': 'sushi-iwa-clayton-clayton-2',
   'categories': [{'alias': 'sushi', 'title': 'Sushi Bars'},
    {'alias': 'asianfusion', 'title': 'Asian Fusion'},
    {'alias': 'thai', 'title': 'Thai'}],
   'coordinates': {'latitude': 35.65473, 'longitude': -78.47785},
   'display_phone': '(919) 585-6140',
   'distance': 1751.161429011724,
   'id': 'LeHWKBOD_klTuyOOROBnRQ',
   'image_url': 'https://s3-media3.fl.yelpcdn.com/bphoto/VCpbqrIJE9pFjhUbidyn0Q/o.jpg',
   'is_closed': False,
   'location': {'address1': '11629 US-70 Bus',
    'address2': None,
    'address3': '',
    'city': 'Clayton',
    'country': 'US',
    'display_address': ['11629 US-70 Bus', 'Clayton, NC 27520'],
    'state': 'NC',
    'zip_code': '27520'},
   'name': 'Sushi Iwa Clayton',
   'phone': '+19195856140',
   'price': '$$',
   'rating': 4.5,
   'review_count': 32,
   'transactions': [],
   'url': 'https://www.yelp.com/biz/sushi-iwa-clayton-clayton-2?adjust_creative=q-p1D6Eu9I--5Izrrb1AuA&utm_campaign=yelp_api_v3&utm_medium=api_v3_business_search&utm_source=q-p1D6Eu9I--5Izrrb1AuA'},
  {'alias': 'sushi-bonsai-clayton',
   'categories': [{'alias': 'japanese', 'title': 'Japanese'},
    {'alias': 'sushi', 'title': 'Sushi Bars'}],
   'coordinates': {'latitude': 35.6365052150107, 'longitude': -78.447613},
   'display_phone': '(919) 550-6030',
   'distance': 1767.5820999210964,
   'id': 'xAbwYdYFfILn84DOQQ_SkA',
   'image_url': 'https://s3-media1.fl.yelpcdn.com/bphoto/NfYNNHwDQHV8Y5t7LWcYCA/o.jpg',
   'is_closed': False,
   'location': {'address1': '11629 US Hwy 70 W',
    'address2': '',
    'address3': '',
    'city': 'Clayton',
    'country': 'US',
    'display_address': ['11629 US Hwy 70 W', 'Clayton, NC 27520'],
    'state': 'NC',
    'zip_code': '27520'},
   'name': 'Sushi Bonsai',
   'phone': '+19195506030',
   'price': '$$',
   'rating': 2.5,
   'review_count': 38,
   'transactions': [],
   'url': 'https://www.yelp.com/biz/sushi-bonsai-clayton?adjust_creative=q-p1D6Eu9I--5Izrrb1AuA&utm_campaign=yelp_api_v3&utm_medium=api_v3_business_search&utm_source=q-p1D6Eu9I--5Izrrb1AuA'},
  {'alias': 'kobe-japanese-steak-house-and-sushi-bar-clayton',
   'categories': [{'alias': 'sushi', 'title': 'Sushi Bars'},
    {'alias': 'japanese', 'title': 'Japanese'},
    {'alias': 'steak', 'title': 'Steakhouses'}],
   'coordinates': {'latitude': 35.6668019795573,
    'longitude': -78.4963542222977},
   'display_phone': '(919) 359-9060',
   'distance': 4029.545191775742,
   'id': 'Rbktq9E297bDDmD-JicW1A',
   'image_url': 'https://s3-media3.fl.yelpcdn.com/bphoto/w6gQBUmikvES6gsdplPvWg/o.jpg',
   'is_closed': False,
   'location': {'address1': '820 Gulley Dr',
    'address2': None,
    'address3': None,
    'city': 'Clayton',
    'country': 'US',
    'display_address': ['820 Gulley Dr', 'Clayton, NC 27520'],
    'state': 'NC',
    'zip_code': '27520'},
   'name': 'Kobe Japanese Steak House & Sushi Bar',
   'phone': '+19193599060',
   'price': '$$',
   'rating': 3.0,
   'review_count': 64,
   'transactions': [],
   'url': 'https://www.yelp.com/biz/kobe-japanese-steak-house-and-sushi-bar-clayton?adjust_creative=q-p1D6Eu9I--5Izrrb1AuA&utm_campaign=yelp_api_v3&utm_medium=api_v3_business_search&utm_source=q-p1D6Eu9I--5Izrrb1AuA'},
  {'alias': 'sun-arch-buffet-clayton',
   'categories': [{'alias': 'sushi', 'title': 'Sushi Bars'},
    {'alias': 'chinese', 'title': 'Chinese'},
    {'alias': 'buffets', 'title': 'Buffets'}],
   'coordinates': {'latitude': 35.663436, 'longitude': -78.499689},
   'display_phone': '(919) 553-0035',
   'distance': 4159.925308925987,
   'id': 'gK1iRgrr0NTxtS7mtyOPqw',
   'image_url': 'https://s3-media4.fl.yelpcdn.com/bphoto/IlhJPR6cSFSaNFdqS4dcZw/o.jpg',
   'is_closed': False,
   'location': {'address1': '877 Town Centre Blvd',
    'address2': '',
    'address3': None,
    'city': 'Clayton',
    'country': 'US',
    'display_address': ['877 Town Centre Blvd', 'Clayton, NC 27520'],
    'state': 'NC',
    'zip_code': '27520'},
   'name': 'Sun Arch Buffet',
   'phone': '+19195530035',
   'rating': 4.5,
   'review_count': 10,
   'transactions': [],
   'url': 'https://www.yelp.com/biz/sun-arch-buffet-clayton?adjust_creative=q-p1D6Eu9I--5Izrrb1AuA&utm_campaign=yelp_api_v3&utm_medium=api_v3_business_search&utm_source=q-p1D6Eu9I--5Izrrb1AuA'},
  {'alias': 'lowes-foods-clayton',
   'categories': [{'alias': 'grocery', 'title': 'Grocery'},
    {'alias': 'beer_and_wine', 'title': 'Beer, Wine & Spirits'},
    {'alias': 'chicken_wings', 'title': 'Chicken Wings'}],
   'coordinates': {'latitude': 35.672358451083,
    'longitude': -78.5069274902344},
   'display_phone': '(919) 550-6740',
   'distance': 5161.291098184567,
   'id': '3h5JS-8yMqF0N_yXMQmDQQ',
   'image_url': 'https://s3-media4.fl.yelpcdn.com/bphoto/ubdhqqItgVkYzMPj9ZqrfQ/o.jpg',
   'is_closed': False,
   'location': {'address1': '11711 Us Highway 70 Business W',
    'address2': '',
    'address3': '',
    'city': 'Clayton',
    'country': 'US',
    'display_address': ['11711 Us Highway 70 Business W', 'Clayton, NC 27520'],
    'state': 'NC',
    'zip_code': '27520'},
   'name': 'Lowes Foods',
   'phone': '+19195506740',
   'price': '$$$$',
   'rating': 3.5,
   'review_count': 9,
   'transactions': [],
   'url': 'https://www.yelp.com/biz/lowes-foods-clayton?adjust_creative=q-p1D6Eu9I--5Izrrb1AuA&utm_campaign=yelp_api_v3&utm_medium=api_v3_business_search&utm_source=q-p1D6Eu9I--5Izrrb1AuA'}],
 'region': {'center': {'latitude': 35.650711, 'longitude': -78.456391}},
 'total': 6}


def test_runner(skill, example, emitter, loader):
    s = [s for s in loader.skills if s and s.root_dir == skill]
    with patch(s[0].__module__ + '.YelpAPI.search_query') as m:
        s[0].is_closed = json_response['businesses'][0]['is_closed']
        s[0].restaurant_phone = json_response['businesses'][0]['phone']
        s[0].restaurant_address = json_response['businesses'][0]['location']['display_address'][0] + \
                              " " + json_response['businesses'][0]['location']['display_address'][1]
        m.return_value = json_response
        return SkillTest(skill, example, emitter).run(loader)