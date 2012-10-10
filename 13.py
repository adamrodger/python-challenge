import base64
import urllib
from urllib import unquote, splittype, splithost
import xmlrpclib

class UrllibTransport(xmlrpclib.Transport):
    def set_proxy(self, proxy):
        self.proxyurl = proxy
                
    def request(self, host, handler, request_body, verbose=0):
        type, r_type = splittype(self.proxyurl)
        phost, XXX = splithost(r_type)

        puser_pass = None
        if '@' in phost:
            user_pass, phost = phost.split('@', 1)
            if ':' in user_pass:
                user, password = user_pass.split(':', 1)
                puser_pass = base64.encodestring('%s:%s' % (unquote(user),
                                                unquote(password))).strip()
        
        urlopener = urllib.FancyURLopener({'http':'http://%s'%phost})
        if not puser_pass:
            urlopener.addheaders = [('User-agent', self.user_agent)]
        else:
            urlopener.addheaders = [('User-agent', self.user_agent),
                                    ('Proxy-authorization', 'Basic ' + puser_pass) ]

        host = unquote(host)
        f = urlopener.open("http://%s%s"%(host,handler), request_body)

        self.verbose = verbose 
        return self.parse_response(f)
        
if __name__ == '__main__':
    proxy = "http://adam.rodger:Passw0rd@141.196.16.102:8081"
    
    p = UrllibTransport()
    p.set_proxy(proxy)
    
    server = xmlrpclib.Server("http://www.pythonchallenge.com/pc/phonebook.php", transport=p)
    #print server.system.methodSignature("phone")
    print server.phone("Bert") #italy
