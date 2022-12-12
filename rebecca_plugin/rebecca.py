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
        secs = utils.get_sec(message.text, 'timer')
        self.driver.reply_with_mention(message, "Got it sir")
        time.sleep(secs)
        self.driver.reply_with_mention(message, "Time up, sir. ")