from exceptions import NegativeTitlesError
from exceptions import InvalidYearCupError
from exceptions import ImpossibleTitlesError
import datetime


def data_processing(dic):
    titles = dic.get("titles")
    first_cup = dic.get("first_cup")

    if titles < 0:
        raise NegativeTitlesError

    current_year = datetime.datetime.now().year
    if first_cup < 1930 or (first_cup - 1930) % 4 != 0 or first_cup > current_year:
        raise InvalidYearCupError

    cups_played = (current_year - first_cup) // 4 + 1
    if titles > cups_played:
        raise ImpossibleTitlesError
