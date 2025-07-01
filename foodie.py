
import pprint, json
import zomatopy
import csv

# user key for zomato api
config = {"user_key": "542a9a23276d99b25f34117e32a1f7c0"}
zomato = zomatopy.initialize_app(config)

# Tier1 and Tier2 cities
cities = {
    'X': ['bangaluru', 'bangalore','chennai', 'delhi ncr', 'delhi', 'new delhi', 'hyderabad', 'kolkata', 'mumbai', 'ahmedabad', 'pune'],
    'Y': ['agra', 'ajmer', 'aligarh', 'amravati', 'amritsar', 'asansol', 'aurangabad', 'bareilly',
          'belgaum', 'bhavnagar', 'bhiwandi', 'bhopal', 'bhubaneswar', 'bikaner', 'bilaspur',
          'bokaro steel city', 'chandigarh', 'coimbatore nagpur', 'cuttack', 'dehradun', 'dhanbad',
          'bhilai', 'durgapur', 'erode', 'faridabad', 'firozabad', 'ghaziabad', 'gorakhpur',
          'gulbarga', 'guntur', 'gwalior', 'gurgaon', 'guwahati', 'hubli-dharwad', 'indore',
          'jabalpur', 'jaipur', 'jalandhar', 'jammu', 'jamnagar', 'jamshedpur', 'jhansi', 'jodhpur',
          'kakinada', 'kannur', 'kanpur', 'kochi', 'kottayam', 'kolhapur', 'kollam', 'kota',
          'kozhikode', 'kurnool', 'ludhiana', 'lucknow', 'madurai', 'malappuram', 'mathura',
          'goa', 'mangalore', 'meerut', 'moradabad', 'mysore', 'nanded', 'nashik', 'nellore',
          'noida', 'palakkad', 'patna', 'pondicherry', 'purulia allahabad', 'raipur', 'rajkot',
          'rajahmundry', 'ranchi', 'rourkela', 'salem', 'sangli', 'siliguri', 'solapur', 'srinagar',
          'thiruvananthapuram', 'thrissur', 'tiruchirappalli', 'tirupati', 'tirunelveli', 'tiruppur',
          'tiruvannamalai', 'ujjain', 'bijapur', 'vadodara', 'varanasi', 'vasai-virar city',
          'vijayawada', 'vellore', 'warangal', 'surat', 'visakhapatnam'],
    'Z': ['all other']}

cuisine_dict_id = {1: 'american', 73: 'mexican', 50: 'north indian', 85: 'south indian', 55: 'italian', 25: 'chinese'}
cuisine_dict_name = {'mexican': 73, 'chinese': 25, 'south indian': 85, 'american': 1, 'north indian': 50, 'italian': 55}

# get zomato specific cuisine id from above dictionary
def get_cuisine_id(cuisine):
    if cuisine not in cuisine_dict_name:
        raise NotImplementedError("cusine not supported")
    return str(cuisine_dict_name[cuisine])

# checks if given city is tier1 or tier 2 or not
def is_loc_available(city):
    available_cities = []
    available_cities.extend(cities['X'])
    available_cities.extend(cities['Y'])

    if city.lower() not in available_cities:
        return False
    return True

# filter out expect top 5
def filter_n_on_rating(result, n=5):
    rated_result = sorted(result, key=lambda x: x.get('rating'), reverse=True)
    if len(rated_result) > n:
        return rated_result[0:n]
    else:
        return rated_result

# filter based on budget
def filter_on_budget(result, budget):
    budget_result = []
    if budget == 0:
        budget_result = [rest for rest in result if rest.get('cost_for_two') < 300]
    elif budget == 1:
        budget_result = [rest for rest in result if 300 <= rest.get('cost_for_two') <= 700]
    elif budget == 2:
        budget_result = [rest for rest in result if rest.get('cost_for_two') > 700]
    elif budget == 3:
        budget_result = [rest for rest in result]
    else:
        budget_result = [rest for rest in result if (budget-150) <= rest.get('cost_for_two') < (budget+150)]
    return budget_result

# get top 50 zomato results
def get_top_50(loc, cuisine_id, average_cost_for_two):
    return get_top_n(loc, cuisine_id, average_cost_for_two, n=50)

def get_top_n(loc=None, cuisine_id=None, average_cost_for_two=None, n=1):
    """
    Returns n restaurant list via zomato api

    :param loc: location of the user
    :param cuisine_id: id related to specific cuisine
    :param average_cost_for_two: price range of user
    :param n: number of restaurant to fetch in one call
    :return:
    """

    lat,lon = 0,0

    if cuisine_id is None and loc is None and average_cost_for_two is None:
        raise ValueError('Necessary details are not provided')

    if not str(loc).isnumeric():
        # get_location gets the lat-long coordinates of 'loc'
        location_detail = zomato.get_location(loc, 1)

        # store retrieved data as a dict
        d1 = json.loads(location_detail)

        # separate lat-long coordinates
        lat = d1["location_suggestions"][0]["latitude"]
        lon = d1["location_suggestions"][0]["longitude"]
    
    else:
        with open('data/pincodes_location.db') as csvfile:
                        readCSV = csv.reader(csvfile, delimiter=',') 
                        for row in readCSV:
                            if len(row)<1:
                                continue
                            if row[0] == str(loc):
                                lat,lon = row[1],row[2]
    cuisine_id = str(cuisine_id)
    results = zomato.restaurant_search("", lat, lon, cuisine_id, 50)
    results = json.loads(results)
    # print(results)

    simple_result = parse_to_readable(results)
    budget_result = filter_on_budget(simple_result, average_cost_for_two)
    pprint.pprint(budget_result)
    return budget_result

def parse_to_readable(data):
    """
    Converts complex result into simple readable one

    :param data: result from zomato api
    :return: simple result dict
    """
    parsed = []
    for restaurant in data.get('restaurants', []):
        tmp = {}
        restaurant = restaurant.get('restaurant', {})
        tmp['rating'] = float(restaurant.get('user_rating', {}).get('aggregate_rating'))
        tmp['cost_for_two'] = restaurant.get('average_cost_for_two')
        tmp['cuisines'] = restaurant.get('cuisines')
        tmp['address'] = restaurant.get('location', {}).get('address')
        tmp['name'] = restaurant.get('name')

        parsed.append(tmp)
    return parsed


def bot_template(result):
    text = text_tempalte(result)
    html = mail_template(result)
    return text, html


def text_tempalte(result):
    msg = "{idx}. {restaurant_name} in {restaurant_address} has been rated {rating}."
    final_message = []
    for idx, item in enumerate(result, start=1):
        if idx == 6:
            break
        bot_msg = msg.format(idx=idx, restaurant_name=item['name'], restaurant_address=item['address'],
                             rating=item['rating'])
        final_message.append(bot_msg)
    return '\n'.join(final_message)


def mail_template(result):
    html = """<!DOCTYPE html><html><head><title>Restarurants</title></head><body><p class="lw">Hi!</p><p>Here is the list result of Restaurants you wanted:</p><br><ol>{final_message}</ol>  <p>Thanks</p><p>HungryKya</p></body></html>"""
    items = []

    msg = "<li>{restaurant_name} in {restaurant_address} has been rated {rating}</li>"
    final_message = []
    for idx, item in enumerate(result, start=1):
        if idx == 11:
            break
        bot_msg = msg.format(idx=idx, restaurant_name=item['name'], restaurant_address=item['address'],
                             rating=item['rating'])
        final_message.append(bot_msg)
    # print(final_message)
    html = html.format(final_message='<br>'.join(final_message))
    print('===========')
    # html.format(items='\n'.join(final_message))
    return html.replace('\n', '<br>').replace('\'', '&apos;')


if __name__ == "__main__":
    loc = 'hiarpur'
    cuisine = "50"
    budget = 1
    mydata = get_top_50(loc=loc, cuisine_id=cuisine, average_cost_for_two=budget)
    res_5 = filter_n_on_rating(mydata, 10)
    tex, htm = bot_template(res_5)
    pprint.pprint(tex)
    pprint.pprint(htm)
