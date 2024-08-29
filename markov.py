import random

class Markov():
    def __init__(self, prefix: int):
        self.items = {}
        lst_state = []
        for _i in range(prefix):
            lst_state.append(None)
        self.state = tuple(lst_state)
        
    def add(self, new_item):
        if self.state in self.items:
            self.items[self.state].append(new_item)
        else:
            self.items[self.state] = [new_item]
        self._transition(new_item)

    def _transition(self, next):
        lst_state = list(self.state)
        state = lst_state[1:] + [next]
        self.state = tuple(state)
        
    def reset(self):
        lst_state = []
        for _i in range(len(self.state)):
            lst_state.append(None)
        self.state = tuple(lst_state)

    def randomNext(self):
        lst = self.items.get(self.state) # lst is a list
        choice = random.choice(lst)
        self._transition(choice)
        return choice