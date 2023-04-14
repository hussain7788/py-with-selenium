class AuthMethod:    
    def __init__(self, fn):
        self.fn = fn
        
    def __call__(self):
        self.fn()
        print("Auth:", self.fn.__name__)
@AuthMethod
def process_document():
    print("called process document")
# process_document()

# ###########################
# class sample():
#     def __init__(self) -> None:
#         pass
#     def __call__(self):
#         print("call method invoked")

# s = sample()
# ## when we call s() like a function the internally __call__ method invoked .
# s()
#########################
def f():
    print("f starts")

    def g():
        print("g starts")
        print("g ends")
        return 2+3
    return g()

print(f())

