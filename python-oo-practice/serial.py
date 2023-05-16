"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """
    def __init__(self,start=0):
        '''Create a new serial with a default starting point of 0'''
        self.start = self.next = start

    def __repr__(self):
        return f'<Serial start={self.start} next={self.next}>'
    
    def generate(self):
        '''Take the existing serial and output the next number in sequence'''
        self.next += 1
        return self.next -1
    
    def reset(self):
        '''Reset the serial back to the original starting number'''
        self.next = self.start