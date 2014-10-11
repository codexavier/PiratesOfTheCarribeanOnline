from pandac.PandaModules import *

loadPrcFile('config/general.prc')

class game:
    name = 'pirates'
    process = 'server'
__builtins__.game = game

from otp.ai.AIBaseGlobal import *

from pirates.uberdog.PiratesUberRepository import PiratesUberRepository
simbase.air = PiratesUberRepository(400000000, 4002)
simbase.air.connect('127.0.0.1', 7100)

run()