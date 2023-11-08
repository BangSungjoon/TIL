class Calculator:
    def __init__(self, val):
        self.val = val

    def add(self, val):
        self.val += val
        return self
    
    def subtract(self, val):
        self.val -= val
        return self
    
    def multiply(self, val):
        self.val *= val
        return self
    
    def divide(self, val):
        self.val /= val
        return self
    
    def end(self):
        return self.val