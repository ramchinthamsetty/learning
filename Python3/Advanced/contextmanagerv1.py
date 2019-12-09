class PrintingContextManager:
    
    def __init__(self, name):
        self.name = name
    
    def __enter__(self):
        print('{} entered'.format(self.name))
        return self.name
        
    def __exit__(self, *args):
        print('{} exited'.format(self.name))
        
        
pcm1 = PrintingContextManager('context manager 1')
pcm2 = PrintingContextManager('context manager 2')
with pcm1 as name:
    print('in with block for {}'.format(name))
try:
    with pcm2 as name:
        raise Exception
        print('in with block for {}'.format(name))
except:
    print('Error occurred.')