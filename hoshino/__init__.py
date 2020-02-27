from os import path 
import logging

import nonebot

from .log import logger, error_handler


def init(config) -> nonebot.NoneBot:

    nonebot.init(config)
    bot = nonebot.get_bot()

    logger.setLevel(logging.DEBUG if bot.config.DEBUG else logging.INFO)
    nonebot.logger.addHandler(error_handler)

    for module_name in config.MODULES_ON:
        nonebot.load_plugins(
            path.join(path.dirname(__file__), 'modules', module_name),
            f'hoshino.modules.{module_name}'
        )

    return bot


def get_bot() -> nonebot.NoneBot:
    return nonebot.get_bot()