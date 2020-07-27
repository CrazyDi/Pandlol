class Check:
    """
    Класс для общей валидации
    """
    def __init__(self):
        self.errors = {}

    def validate(self, **kwargs) -> bool:
        """
        Функция собирает все ошибки возникшие при валидации указанных параметров и возвращает их в объекте JSON
        :param kwargs: параметр проверки=[список функций валидации]
        :return:
        """
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
