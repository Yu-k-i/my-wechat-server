from werobot import WeRoBot
from werobot.config import Config

config = Config(
    TOKEN='tangxin',
    SERVER="auto",
    HOST="0.0.0.0",
    PORT="80",
    SESSION_STORAGE=None,
    APP_ID='wx98e9f23f0ba108c6',
    APP_SECRET=None,
    ENCODING_AES_KEY='36HbTSXwX3yU0NAbkvII2a0d6DLMK7TCm8e0bWQpZ3h '
)

robot = WeRoBot(config=config)

@robot.handler
def hello_world(message):
    return 'hello world'

@try:
    pass
except expression as identifier:
    pass
else:
    pass

@robot.text
def test(message):
    return message.content

robot.run()