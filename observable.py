class Observable(object):
    """
    copied from example on powerpoint
    except for house update, made so house can both observer update
    and observable update
    """
    def __init__(self):                    
        self.observers = []
        
    def add_observer(self, observer):                
            if not observer in self.observers:                        
                self.observers.append(observer)
		       
    def remove_observe(self, observer):
        if observer in self.observers:
            self.observers.remove(observer)

        
    def remove_all_observers(self):                
        self.observers = []
		
    def update(self):
        for observer in self.observers:
            observer.update(self)
            
    # added so there wouldn't be a name conflict when house calls update
    # since house extends both observer and observable
    def house_update(self):
        for observer in self.observers:
            observer.update(self)
				