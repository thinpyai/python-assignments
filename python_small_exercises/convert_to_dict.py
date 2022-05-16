import json

class Pet:
    def __init__(self, type: str) -> None:
        self.type = type

class Child:
    def __init__(self, name, pet: Pet) -> None:
        self.child_name = name
        self.pet = pet

class Task:
    def __init__(self, job: str) -> None:
        self.job = job

class Parent:
    def __init__(self, name: str, child: Child, task: Task) -> None:
        self.parent_name = name 
        self.child = child 
        self.job = task


def convert_to_dict(obj, types) -> dict:
    obj_dict = obj.__dict__
    for key, value in obj_dict.items():
        if isinstance(value, types):
            obj_dict[key] = convert_to_dict(value, types)
    return obj_dict

if __name__ == "__main__":
    pet = Pet('dog')
    child = Child('baby', pet)
    job = Task('engineer')
    parent = Parent('mama', child, job)
    parent_dict = convert_to_dict(parent, tuple([Child, Task, Pet]))
    print(parent_dict)

