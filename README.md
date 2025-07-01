# Building-Chatbots-With-Rasa
Building Chatbots With Rasa (PGD Project)

An Indian startup named 'Foodie' wants to build a conversational bot (chatbot) which can help users discover restaurants across several Indian cities. You have been hired as the lead data scientist for creating this product.

 

The main purpose of the bot is to help users discover restaurants quickly and efficiently and to provide a good restaurant discovery experience. The project brief provided to you is as follows.

 

The bot takes the following inputs from the user:

    City: Take the input from the customer as a text field. For example:

    Bot: In which city are you looking for restaurants?

    User: anywhere in Delhi

     

 

 

Important Notes: 

    Assume that Foodie works only in Tier-1 and Tier-2 cities. You can use the current HRA classification of the cities from here. Under the section 'current classification' on this page, the table categorizes cities as X, Y and Z. Consider 'X ' cities as tier-1 and 'Y' as tier-2. 
    The bot should be able to identify common synonyms of city names, such as Bangalore/Bengaluru, Mumbai/Bombay etc.

 

Your chatbot should provide results for tier-1 and tier-2 cities only, while for tier-3 cities, it should reply back with something like "We do not operate in that area yet".

 

    Cuisine Preference: Take the cuisine preference from the customer. The bot should list out the following six cuisine categories (Chinese, Mexican, Italian, American, South Indian & North Indian) and the customer can select any one out of that. Following is an example for the same:

    Bot: What kind of cuisine would you prefer?
        Chinese
        Mexican
        Italian
        American
        South Indian
        North Indian

    User: I’ll prefer Italian!

 

 

 

 

 

 

 

 

 

 

 

 

    Average budget for two people: Segment the price range (average budget for two people) into three price categories: lesser than 300, 300 to 700 and more than 700. The bot should ask the user to select one of the three price categories. For example:

    Bot: What price range are you looking at?

        Lesser than Rs. 300
        Rs. 300 to 700
        More than 700

    User: in range of 300 to 700

     

 

 

 

 

 

 

 

While showing the results to the user, the bot should display the top 5 restaurants in a sorted order (descending) of the average Zomato user rating (on a scale of 1-5, 5 being the highest). The format should be: {restaurant_name} in {restaurant_address} has been rated {rating}.


Finally, the bot should ask the user whether he/she wants the details of the top 10 restaurants on email. If the user replies 'yes', the bot should ask for user’s email id and then send it over email. Else, just reply with a 'goodbye' message. The mail should have the following details for each restaurant:

    Restaurant Name
    Restaurant locality address
    Average budget for two people
    Zomato user rating

You can refer to the following links on how to send emails through Python:

    Python Email Package
    Python Flask Mail

(A heads up: You'll have to enable secure access on Gmail to allow Python to send emails).

 

You have been given some sample conversational stories in the ‘test’ file. Look at the stories and try to observe entities, intents, dialogue-flow which may be useful to train the NLU and also the dialogue flow.
Sample conversational stories
Download

 
Goals of this Project

In this project, you will build a chatbot for ‘Foodie’ and then deploy it on Slack. The folder with starter codes has already been shared with you in session-1. You need to accomplish the following in the project:

    NLU training: You can use rasa-nlu-trainer to create more training examples for entities and intents. Try using regex features and synonyms for extracting entities.

    Build actions for the bot. Read through the Zomato API documentation to extract the features such as the average price for two people and restaurant’s user rating. You also need to build an ‘action’ for sending emails from Python.

    Creating more stories: Use train_online.py file to create more stories. Refer to the sample conversational stories provided above.  Your bot will be evaluated on something similar to the test stories shared.

# Foodie(FoodBot)
This platform helps user to get information about the restaurants .They can even customize their restaurant search basis on location and cuisine

# Features!
  - can understand intention of end user.
  - provides list of restaurant on the basis of your query.
  - can send email containing your query result.
  - can detect city names, or work for indian pincodes

### Technicalitis ( RUN AS ADMINISTRATOR )
The FoodBot consists of the following files:
- data/stories.md contains training stories for the Core model
- data/data.json contains training data for NLU model
- actions.py contains some custom actions
- config_spacy.json contains the model configuration
- restaurant_domain.yml contains the domain of the bot
- foodie.py script works as a bridge between zomato API and our FoodBot
- sendmail.py script used to send email to user if user wants to get top restaurants list on mail address
- soundex.py is used to detect mis-spelled city names ,if any.
- sound_ex_data.py is to generate SoundEx code for cites stored in settings.py
- rasa_slack_connector.py contains blueprint for slack connection with bot.
- run_app.py contains authentication credentials for slack.

### Installation And Usage

For easy usage and understanding we have created an virtual envoirnment that has all required libraries and functions.
1. Install virtual envoirnment if you dont have using:
  ```sh
$ sudo easy_install pip
$ sudo pip install virtualenv
$ virtualenv venv -p python3.6
$ source venv/bin/activate
$ pip install -r requirements.txt
```

### Training of the model
2. To Train core model , use
  ```sh
$ python dialogue_management_model.py
```
3. To train nlu model , run
  ```sh
$ python nlu_model.py

### How to run bot on Command prompt
To run FoodBot on CLI,
  ```sh
$ python run_console.py

```


### how to run bot on slack
For slack connection, have to write slack authentication credentials and rasa(Core+NLU) in
  ```sh
$ run_app.py
```

After connection established, use ngrok for temporary public URL.
  ```sh
$ ngrok http < same port number used in run_app.py>
```




