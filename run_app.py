from rasa_core.channels import HttpInputChannel
from rasa_core.agent import Agent
from rasa_core.interpreter import RasaNLUInterpreter
from rasa_slack_connector import SlackInput


nlu_interpreter = RasaNLUInterpreter('./models/nlu/default/restaurantnlu')
agent = Agent.load('./models/dialogue', interpreter = nlu_interpreter)

input_channel = SlackInput('xoxp-803639576294-788648454834-801460644853-5f12eabc9d0c05e8687f8a2d776a6c97', #app oauth access token
                            'xoxb-803639576294-789982095315-qyMJNoSIdMTI53ZG2P6ddm64', # bot verification token
                            '4yodb6XKz72ihVBqVAFVRk8s',
                             True)

#s = agent.handle_channels([input_channel], 5004, serve_forever=True)
s = agent.handle_channel(HttpInputChannel(5004, '/', input_channel))
print(s)

