# NOT A NECESSARY FILE
from requireit import *
print("libraries installed:")
# same as pip freeze
print(pipit("freeze"))
print("making sure asyncio is installed")
# same is checking if asyncio is in the output of pip freeze, and if it isn't, running pip install asyncio
# note the quotes!
makeSure("asyncio")
print("importing asyncio")
# note the quotes again!
importIt("asyncio")
print("making sure asyncio is installed, and then importing it")
# it says it all
makeSureAndImport("asyncio")
print("making sure aiohttp and asyncio is installed")
# it says it all, but the second parameter is verbose or not
requireExists(["aiohttp", "asyncio"], True)
print("making sure aiohttp and asyncio is imported")
# the signature move! (the second parameter is verbose or not)
requireit(["aiohttp", "asyncio"], True)
