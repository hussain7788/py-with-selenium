class AuthMethod:    
    def __init__(self, fn):
        self.fn = fn
        
    def __call__(self):
        self.fn()
        print("Auth:", self.fn.__name__)
@AuthMethod
def process_document():
    print("called process document")
process_document()

