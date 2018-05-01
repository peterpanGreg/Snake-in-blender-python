from bge import logic
from bge import events


class Direct:
    def __init__(self,direct='E'):
        self.direct=direct

    def __repr__(self):
        return repr(self.direct)

    def change(self):
        clavier=logic.keyboard

        UP_key= logic.KX_INPUT_ACTIVE==clavier.events[events.UPARROWKEY]
        DOWN_key= logic.KX_INPUT_ACTIVE==clavier.events[events.DOWNARROWKEY]
        RIGHT_key= logic.KX_INPUT_ACTIVE==clavier.events[events.RIGHTARROWKEY]
        LEFT_key= logic.KX_INPUT_ACTIVE==clavier.events[events.LEFTARROWKEY]

        if UP_key and self.direct!='S':
            self.direct="N"

        elif DOWN_key and self.direct!='N':
            self.direct="S"

        elif RIGHT_key and self.direct!='W':
            self.direct="E"

        elif LEFT_key and self.direct!='E':
            self.direct="W"

        
        UP_key=False
        DOWN_key=False
        RIGHT_key=False
        LEFT_key=False

    
