'''
State machine example.
Modified from https://python-3-patterns-idioms-test.readthedocs.io/en/latest/StateMachine.html#table-driven-state-machine
'''

from enum import Enum

class MouseAction(Enum):
    '''Mouse action enumeration definition.'''
    APPEAR = 0
    RUN_AWAY = 1
    ENTER = 2
    ESCAPE = 3
    TRAPPED = 4
    REMOVED = 5

class State:
    '''State super class.'''

class Waiting(State):
    '''Mouse trap waiting status implementation.'''

    def run(self):
        '''Execute tasks under this state.'''

        print('Waiting: Broadcasting cheese smell')

    def next(self, input_state):
        '''Transit state machine to next state according to the input.'''

        if input_state == MouseAction.APPEAR.value:
            return Luring()

        print('WARNING: UNEXPECTED STATUS!')

        return Waiting()

class Luring(State):
    '''Mouse trap luring status implementation.'''

    def run(self):
        '''Execute tasks under this state.'''

        print('Luring: Presenting Cheese, door open')

    def next(self, input_state):
        '''Transit state machine to next state according to the input.'''

        if input_state == MouseAction.RUN_AWAY.value:
            return Waiting()
        if input_state == MouseAction.ENTER.value:
            return Trapping()

        print('WARNING: UNEXPECTED STATUS!')

        return Luring()

class Trapping(State):
    '''Mouse trap trapping status implementation.'''

    def run(self):
        '''Execute tasks under this state.'''

        print('Trapping: Closing door')

    def next(self, input_state):
        '''Transit state machine to next state according to the input.'''

        if input_state == MouseAction.ESCAPE.value:
            return Waiting()
        if input_state == MouseAction.TRAPPED.value:
            return Holding()

        print('WARNING: UNEXPECTED STATUS!')

        return Trapping()

class Holding(State):
    '''Mouse trap holding status implementation.'''

    def run(self):
        '''Execute tasks under this state.'''

        print('Holding: Mouse caught')

    def next(self, input_state):
        '''Transit state machine to next state according to the input.'''

        if input_state == MouseAction.REMOVED.value:
            return Waiting()

        print('WARNING: UNEXPECTED STATUS!')

        return Holding()

class StateMachine:
    '''State machine super class.'''

    def __init__(self, initialState):
        self.current_state = initialState
        self.current_state.run()

    def run_with_script_file(self, input_file_name):
        '''Execute state machine a script file.'''

        MOUSE_ACTION = 2

        with open(input_file_name, encoding = 'utf-8') as file:
            moves = file.readlines()
            for move in moves:
                input_state = int(str.split(move, ' ')[MOUSE_ACTION])
                print(f'The input state is: {MouseAction(input_state)}')
                self.current_state = self.current_state.next(input_state)
                self.current_state.run()

class MouseTrap(StateMachine):
    '''Mouse trap state machine.'''

    def __init__(self):
        super().__init__(Waiting()) # Initialize state machine with waiting state.

if __name__ == '__main__':
    MouseTrap().run_with_script_file('MouseMoves.txt')
