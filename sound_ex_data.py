from soundex import get_soundex

cities_list = ['bangaluru', 'bangalore','chennai', 'delhi ncr', 'delhi', 'new delhi', 'hyderabad', 'kolkata', 'mumbai', 'ahmedabad', 'pune','agra', 'ajmer', 'aligarh', 'amravati', 'amritsar', 'asansol', 'aurangabad', 'bareilly','belgaum', 'bhavnagar', 'bhiwandi', 'bhopal', 'bhubaneswar', 'bikaner', 'bilaspur','bokaro steel city', 'chandigarh', 'coimbatore nagpur', 'cuttack', 'dehradun', 'dhanbad','bhilai', 'durgapur', 'erode', 'faridabad', 'firozabad', 'ghaziabad', 'gorakhpur','gulbarga', 'guntur', 'gwalior', 'gurgaon', 'guwahati', 'hubli-dharwad', 'indore','jabalpur', 'jaipur', 'jalandhar', 'jammu', 'jamnagar', 'jamshedpur', 'jhansi', 'jodhpur','kakinada', 'kannur', 'kanpur', 'kochi', 'kottayam', 'kolhapur', 'kollam', 'kota','kozhikode', 'kurnool', 'ludhiana', 'lucknow', 'madurai', 'malappuram', 'mathura','goa', 'mangalore', 'meerut', 'moradabad', 'mysore', 'nanded', 'nashik', 'nellore','noida', 'palakkad', 'patna', 'pondicherry', 'purulia allahabad', 'raipur', 'rajkot','rajahmundry', 'ranchi', 'rourkela', 'salem', 'sangli', 'siliguri', 'solapur', 'srinagar','thiruvananthapuram', 'thrissur', 'tiruchirappalli', 'tirupati', 'tirunelveli', 'tiruppur','tiruvannamalai', 'ujjain', 'bijapur', 'vadodara', 'varanasi', 'vasai-virar city','vijayawada', 'vellore', 'warangal', 'surat', 'visakhapatnam']

soundex_dict_tier={get_soundex(name):name for name in cities_list}

with open("settings.py","w") as set_file:
     set_file.write(f"soundex_dict_tier = {soundex_dict_tier}")
