from typing import Dict


class Check:
    errors: Dict

    @classmethod
    def validate(cls, **kwargs) -> bool:
        cls.errors = {}
        for key, func_list in kwargs.items():
            for func in func_list:
                result = func()
                if result and key not in cls.errors:
                    cls.errors[key] = result

        if cls.errors:
            return False

        return True
