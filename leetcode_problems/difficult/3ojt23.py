class suppress:
    def __init__(self, error):
        self.error = error
        
    def __enter__(self):
        return self
        

    def __exit__(self, exc_type, exc_val, tb):
        # print(exc_type,exc_val,tb)
        if exc_type == self.error:
            return True
        

with suppress(NameError):
    print("Hi!") 
    print("It's nice to meet you,", name) 
    print("Goodbye!") 
    
with suppress(TypeError):
    print("Hi!") 
    print("It's nice to meet you,", name) 
    print("Goodbye!")