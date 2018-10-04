from xmlrpc.client import boolean


class Player:
    name : ""
    pattern : ""
    state : boolean
    turn : boolean

    def __init__(self, name="Player A",pattern="O"):
        self.name = name
        self.pattern = pattern
        self.state = False
        self.order = 1

    def set_name(self,name):
        self.name = name

    def set_pattern(self,pattern):
        self.pattern = pattern

    def set_state(self,state):
        self.state = state

    def set_turn(self,turn):
        self.turn = turn

    def get_name(self):
        return self.name

    def get_pattern(self):
        return self.pattern

    def get_turn(self):
        return self.turn