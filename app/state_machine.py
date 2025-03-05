class FiniteStateMachine:
    def __init__(self, initial_state):
        self.current_state = initial_state
        self.transitions = {}  # {(from_state, trigger): to_state}
        self.callbacks = []    # functions to call on state change

    def add_transition(self, from_state, trigger, to_state):
        self.transitions[(from_state, trigger)] = to_state

    def add_callback(self, callback):
        self.callbacks.append(callback)

    def trigger(self, trigger):
        key = (self.current_state, trigger)
        if key not in self.transitions:
            raise Exception(f"No transition from {self.current_state} on trigger '{trigger}'")
        prev_state = self.current_state
        self.current_state = self.transitions[key]
        for callback in self.callbacks:
            callback(prev_state, self.current_state, trigger)
        return self.current_state

    def reset(self, state):
        self.current_state = state
