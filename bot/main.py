import logging
import asyncio
import os

from bot import bot
from rest import RestBridge
from database import prepare_index

rest = RestBridge(bot)


if __name__ == '__main__':
    loglevel = logging.DEBUG if os.getenv("DEBUG") else logging.INFO
    logging.basicConfig(level=loglevel)

    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(start())
    except KeyboardInterrupt:
        pass
    finally:
        loop.run_until_complete(stop())
