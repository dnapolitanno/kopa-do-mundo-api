from exceptions import NegativeTitlesError
from exceptions import InvalidYearCupError
from exceptions import ImpossibleTitlesError
import datetime


def data_processing(dic):
    titles = int(dic.get("titles"))
    first_cup_date = dic.get("first_cup")
    first_cup = datetime.datetime.strptime(first_cup_date, "%Y-%m-%d").year

    if titles < 0:
        raise NegativeTitlesError("titles cannot be negative")

    current_year = datetime.datetime.now().year
    if first_cup < 1930 or (first_cup - 1930) % 4 != 0 or first_cup > current_year:
        raise InvalidYearCupError("there was no world cup this year")

    cups_played = (current_year - first_cup) // 4 + 1
    if titles > cups_played:
        raise ImpossibleTitlesError("impossible to have more titles than disputed cups")
