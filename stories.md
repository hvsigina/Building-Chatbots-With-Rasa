## Generated Story 5220515094077363435
* restaurant_search{"location": "nellore"}
    - slot{"location": "nellore"}
    - action_city
    - slot{"location": "nellore"}
    - slot{"location_type": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "north indian"}
    - slot{"cuisine": "north indian"}
    - action_get_cuisine
    - slot{"cuisine": "north indian"}
    - slot{"cuisine_type": true}
    - utter_ask_price
* restaurant_search{"price": "moderate"}
    - slot{"price": "moderate"}
    - action_restaurant
    - slot{"matches": "<!DOCTYPE html><html><head><title>Restarurants</title></head><body><p class=\"lw\">Hi!</p><p>Here is the list result of Restaurants you wanted:</p><br><ol><li>Hotel Reshma in Mahatma Gandhi Nagar Road, Vedayapalem, Nellore - 524004, Opposite Nallapa Reddy Srinivasulu Reddy Statue, Nellore Locality, Nellore has been rated 4.4</li><br><li>Hotel Riyaz in Achari street, Nellore - 524001, Opp Shivam International, Nellore Locality, Nellore has been rated 4.2</li><br><li>Pick N Move in Grand Trunk Road, Chandra Mouli Nagar, Grand Trunk Road, Chandra Mouli Nagar, Postal Colony, Vedayapalem, Nellore - 524004, Rashaker Reddy Statue, Current Office Center, Nellore Locality, Nellore has been rated 4.1</li><br><li>Indies Family Dhaba in Door No 2B, Mini Bypass, Bv Nagar, Nellore, Oppsite ANR Function Hall&near Royalenfield Service Station, Nellore Locality, Nellore has been rated 4.1</li><br><li>Salma Biriyani in Shop No -2(B), Balajinagar, Nellore - 524002, Masjid Center, Nellore Locality, Nellore has been rated 4.1</li><br><li>Celebrations Multicuisine Restaurant in Kings court Avenue, Magunta layout main road, Magunta Layout, Nellore has been rated 4.1</li><br><li>R Bawarchi 2 in 26/3/171, Mini Bypass Road, BV Nagar, Nellore.  has been rated 3.9</li><br><li>Sportello Presto in Survey No 200-1, Near sakshi Paper Office, Kondayapalem, Nellore., Nellore Locality, Nellore has been rated 3.7</li></ol>  <p>Thanks</p><p>HungryKya</p></body></html>"}
    - slot{"noresults": false}
    - utter_ask_ifmail
* deny
    - utter_goodbye
    - action_reset
    - reset_slots
    - export

