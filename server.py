import os
import cherrypy
import json

PATH = os.path.abspath(os.path.dirname(__file__))
class Root(object):
    
    class api(object):
        pass


class RestObject(object):
    exposed = True
    
    def __init__(self,data):
        self.data = data
            
    def GET(self,*args,**kwargs):
        cherrypy.response.headers['Content-Type']= 'application/json'
        return json.dumps(self.data,indent=4)

mydata = [
          {'name':'User1','age':'21'},
          {'name':'User2','age':'25'},
          {'name':'User3','age':'26'},
          {'name':'User4','age':'27'},
          ]

Root.api.users = RestObject(mydata)        

cherrypy.tree.mount(Root(), '/', config={
        '/': {
                'tools.staticdir.on': True,
                'tools.staticdir.dir': PATH,
                'tools.staticdir.index': 'index.html',
                'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
            },
        
    })

cherrypy.engine.start()
cherrypy.engine.block()
