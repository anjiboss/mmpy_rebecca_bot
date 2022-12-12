from mmpy_bot import Plugin, listen_to
from mmpy_bot import Message
import rebecca_plugin.utils as utils
import time
from random import randint

class Rebecca(Plugin):
    @listen_to("wake up", needs_mention=True)
    async def wake_up(self, message: Message):
        self.driver.reply_to(message, "I'm awake!")

    @listen_to('timer', needs_mention=True)
    def timer(self, message: Message):
        id = randint(1, 20)
        secs = utils.get_sec(message.text, 'timer')
        print(id, secs)
        self.driver.reply_to(message, "Got it sir\n"+ "id: " + str(id))
        time.sleep(secs)
        self.driver.reply_to(message, "Time up, sir. "+ "\nid: " + str(id))