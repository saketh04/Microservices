from time import sleep
from nameko.rpc import rpc

class IntroService:
    name = "intro_service"
    branch="intro_service"

    @rpc
    def biodata(self,name,branch):
        sleep(10)
        return "Hello, I am {}! At present I am pursuing B.Tech 4th year at B.V Raju Institute Of Technology in {} branch.".format(name,branch)