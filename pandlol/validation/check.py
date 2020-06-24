from typing import Dict


class Check:
    def __init__(self):
        self.errors = {}

    def validate(self, **kwargs) -> bool:
        self.errors = {}
        for key, func_list in kwargs.items():
            for func in func_list:
                if key not in self.errors:
                    result = func()
                    if result:
                        self.errors[key] = result

        if self.errors:
            return False

        return True
