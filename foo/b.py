class B():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        import pdb
        pdb.set_trace()
        print(f'B constructor {x} and {y}')