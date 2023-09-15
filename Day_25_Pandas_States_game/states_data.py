import pandas as pd


class Data_states():
    def __init__(self, path):
        self.path = path
        self.raw_data = pd.read_csv(self.path)
        self.dict_of_states = self.raw_data.set_index(
            "state").to_dict(orient="index")

    def check_state(self, state):
        if state in self.dict_of_states:
            return True
        else:
            return False

    def return_x_y(self, state):
        x = self.dict_of_states[state]["x"]
        y = self.dict_of_states[state]["y"]
        return x, y

    def return_list_of_states(self):
        return self.raw_data["state"].to_list()
