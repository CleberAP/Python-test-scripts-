import os

class GetPath:
    
    def __init__(self):
        self.path_this_app = os.getcwd ()
        self.app = ''
        self.path_app = ''
        
    def get_path(self):
        return self.path_this_app

    def get_path_app(self, app):
        self.app = app.lower()
        if app.lower() == 'whatsapp':
            return self.get_whastapp_path ()
        else:
            return None
    
    def get_docs_path(self):
        if self.app == 'whatsapp':
            return self.get_doc_whatsapp()
        else:
            return None
            
    def get_whastapp_path(self):
        path_aux = self.path_this_app.split('/')[:-1]
        
        path_main = ''
        
        for elem in path_aux:
            path_main += elem + '/'

        self.path_app = path_main + 'WhatsApp'
        
        return self.path_app
        
    # docs WhatsApp
    def get_doc_whatsapp(self):
        return self.path_app +'/Media/WhatsApp Documents'



