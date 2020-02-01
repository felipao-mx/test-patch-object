from foo.b import B

class A():
    def __init__(self):
        self.b = B('el', 'korean')
        print(type(self.b))
