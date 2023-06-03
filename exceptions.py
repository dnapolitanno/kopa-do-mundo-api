# class NegativeTitlesError(Exception):
#     def __init__(self, message):
#         self.message = message


# def validate_title():
#     NegativeTitlesError("titles cannot be negative")


# class InvalidYearCupError(Exception):
#     def __init__(self, message):
#         self.message = message


# def validate_year():
#     InvalidYearCupError("there was no world cup this year")


# class ImpossibleTitlesError(Exception):
#     def __init__(self, message):
#         self.message = message


# def validate_imptitle():
#     ImpossibleTitlesError("impossible to have more titles than disputed cups")

class NegativeTitlesError(Exception):
    def __init__(self):
        super().__init__("titles cannot be negative")


class InvalidYearCupError(Exception):
    def __init__(self):
        super().__init__("there was no world cup this year")


class ImpossibleTitlesError(Exception):
    def __init__(self):
        super().__init__("impossible to have more titles than disputed cups")