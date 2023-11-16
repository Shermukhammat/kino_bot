import asyncio
import logging

from aiohttp import web
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils.executor import start_webhook

API_TOKEN = '6646323098:AAHcLovTWt83NWns67zaKST1yOC4IDFI18Y'

bot = Bot(API_TOKEN)
Bot.set_current(bot)

dp = Dispatcher(bot)
app = web.Application()

webhook_path = f"/{API_TOKEN}"

