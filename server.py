import cherrypy

from root import Root

def redirect_if_authentication_is_required_and_session_is_not_authenticated(*args, **kwargs):

    conditions = cherrypy.request.config.get('auth.require', None)
    if conditions is not None:
        username = cherrypy.session.get('_cp_username')
        if not username:
            from_url = cherrypy.request.request_line.split()[1]

            raise cherrypy.HTTPRedirect("/loginlogout/login?from_page=%22"+from_url.replace('&&','%01').replace('%22','%00')+"%22")

cherrypy.tools.auth = cherrypy.Tool('before_handler', redirect_if_authentication_is_required_and_session_is_not_authenticated)

if __name__ == '__main__':
    cherrypy.config.update({'server.socket_port': 443}) #port 443 for https or port 80 for http
#    cherrypy.config.update({'server.socket_port': 80})
    cherrypy.config.update({'server.socket_host': 'ec2-35-163-111-83.us-west-2.compute.amazonaws.com'})
    

    #cherrypy.tree.mount(Root())
    cherrypy.tree.mount(Root(),'/',

{ 

'/favicon.ico': { 'tools.staticfile.on': True, 'tools.staticfile.filename': '/home/ec2-user/server/favicon.ico' }, 

'/google30be966b06bbaa70.html': { 'tools.staticfile.on': True, 'tools.staticfile.filename': '/home/ec2-user/server/google30be966b06bbaa70.html'  }, 

'/robots.txt': { 'tools.staticfile.on': True, 'tools.staticfile.filename': '/home/ec2-user/server/robots.txt'  }, 

'/ChatBrowserPhoneImage.png' : { 'tools.staticfile.on': True, 'tools.staticfile.filename': '/home/ec2-user/server/ChatBrowserPhoneImage.png'  },

'/EmailBrowserPhoneImage.png' : { 'tools.staticfile.on': True, 'tools.staticfile.filename': '/home/ec2-user/server/EmailBrowserPhoneImage.png'  }

}

 )

    cherrypy.server.ssl_module = 'builtin'
    cherrypy.server.ssl_certificate = "/etc/letsencrypt/live/ecommunicate.ch/fullchain.pem"
    cherrypy.server.ssl_private_key = "/etc/letsencrypt/live/ecommunicate.ch/privkey.pem"
    cherrypy.server.ssl_certificate_chain = "/etc/letsencrypt/live/ecommunicate.ch/fullchain.pem"
    cherrypy.server.thread_pool = 50


    cherrypy.engine.start()
    cherrypy.engine.block()

