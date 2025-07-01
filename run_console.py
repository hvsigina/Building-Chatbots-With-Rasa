from rasa_core.interpreter import RasaNLUInterpreter
import rasa_core
from rasa_core.utils import EndpointConfig
import actions
from rasa_core.agent import Agent
from rasa_core.channels.console import ConsoleInputChannel

import logging

logging.basicConfig(level=logging.DEBUG)

nlu_interpreter = RasaNLUInterpreter('./models/nlu/default/restaurantnlu')
agent = Agent.load('./models/dialogue', interpreter = nlu_interpreter)

agent.handle_channel(ConsoleInputChannel())

