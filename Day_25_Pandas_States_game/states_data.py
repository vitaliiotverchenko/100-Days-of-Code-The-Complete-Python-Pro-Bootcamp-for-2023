import pandas as pd


class Data_states():
    def __init__(self, path):
        self.path = path
        self.raw_data = pd.read_csv(self.path)
        self.dict_of_states = self.raw_data.set_index("state").to_dict(orient="index")

    def check_state(self, state):
        if state in self.dict_of_states:
            return True
        else:
            return False
