from loader import dp
from . import  midle_checksub.Br
from midle_checksub import Bro

if __name__ == 'middlewares':
    dp.middleware.setup(Bro)