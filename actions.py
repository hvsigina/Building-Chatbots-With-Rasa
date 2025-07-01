from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_core.actions.action import Action
from rasa_core.events import SlotSet, AllSlotsReset, Restarted
from soundex import get_soundex
from settings import soundex_dict_tier
from foodie import is_loc_available, get_cuisine_id,get_top_50, filter_n_on_rating, bot_template
from sendmail import Mail
import csv

# Action to check if city or pincode is tier 1 or tier2 city
class ActionSearchCity(Action):
        def name(self):
                return 'action_city'

        def run(self, dispatcher, tracker, domain):
                loc=tracker.get_slot('location')
                
                loc_found = False
                if not str(loc).isnumeric():
                    loc_soundex=get_soundex(loc)

                    loc_found = False
                    if loc_soundex in soundex_dict_tier.keys():
                        loc=soundex_dict_tier[loc_soundex]
                        loc_found = True

                else:
                    with open('data/pincodes_location.db') as csvfile:
                        readCSV = csv.reader(csvfile, delimiter=',') 
                        for row in readCSV:
                            if len(row)<1:
                                continue
                            if row[0] == str(loc):
                                loc_found = True
                                break
                
                if loc_found == False:
                    dispatcher.utter_message("Currently we do not provide our service at your selected location. Please try again.")
                    return[Restarted()]

                return [SlotSet('location',loc), SlotSet("location_type",loc_found)]

# Action to check if entered cuisine is correct
class ActionCheckCuisine(Action):
        def name(self):
                return 'action_get_cuisine'

        def run(self,dispatcher,tracker,domain):
                val=tracker.get_slot('cuisine')
                print(val)
                print(type(val))
                cuisines = ['chinese','mexican','italian','american','south indian','north indian']
                _val = True
                if not val or val.lower() not in cuisines:
                       dispatcher.utter_message("Entered cuisine is wrong. Please try again.")
                       _val = False
                       return[Restarted()]

                return [SlotSet('cuisine',val), SlotSet('cuisine_type',_val)]

# Action to search for restaurants and filter for price range
class ActionHotel(Action):

    def name(self):
        return 'action_restaurant'

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message("looking for Resturants")
        loc = tracker.get_slot("location")
        food = tracker.get_slot("cuisine")
        paise = tracker.get_slot("price")
        htm = ""
        no_result = False
        print(paise)
        print(type(paise))
        if str(paise) == 'cheap':
            paise_id = 0
        elif str(paise) == 'moderate':
            paise_id = 1
        elif str(paise) == 'expensive':
            paise_id = 2
        elif str(paise).isnumeric():
            if len(str(paise))==1:
                if str(paise)=="1":
                    paise_id = 0
                if str(paise)=="2":
                    paise_id = 1
                if str(paise)=="3":
                    paise_id = 2
            else:
                paise_id = int(str(paise))
                r1 = paise_id-150
                r2 = paise_id+150
                if r1<1:
                    r1=1
                dispatcher.utter_message("Price Range - Rs."+str(r1)+" to Rs."+str(r2))
        else:
            paise_id = 3
            dispatcher.utter_message("No budget chosen!")
        try:
            final_data = get_top_50(loc,food,paise_id)
            top_restau = filter_n_on_rating(final_data, 10)
            tex, htm = bot_template(top_restau)
            no_result = False
            if not tex:
               dispatcher.utter_message("Sorry, we cannot find restaurant that meet your requirement")
               no_result = True
            else:
               dispatcher.utter_message(str(tex))
        except Exception as e:
            print(e)
            dispatcher.utter_message('Sorry for inconvenience')
        return [SlotSet("matches",htm), SlotSet("noresults",no_result)]


class ActionReset(Action):
        def name(self):
                return 'action_reset'

        def run(self, dispatcher, tracker, domain):
                return [AllSlotsReset()]

class ActionRestarted(Action):
    def name(self):
        return 'action_restarted'

    def run(self, dispatcher, tracker, domain):
        return[Restarted()]

