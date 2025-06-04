import json

def save_state(data, filename="task_state.json"):
    with open(filename, "w") as f:
        json.dump(data, f)

def load_state(filename="task_state.json"):
    with open(filename) as f:
        return json.load(f)
