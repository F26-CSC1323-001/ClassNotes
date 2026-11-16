import abc


class Fruit(metaclass = abc.ABCMeta):
    def __init__(self):
        pass        
    
    
class SaleItem(metaclass = abc.ABCMeta):
    def __init__(self):
            pass
    
class Banana(Fruit, SaleItem):
    def __init__(self):
        super().__init__() # does not require passing self, references fruit
        SaleItem.__init__(self) # requires self, references SaleItem 