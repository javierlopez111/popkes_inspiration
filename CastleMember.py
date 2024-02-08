from __future__ import annotations
from typing import Tuple
class CastleKilmereMember:

    location = "United Kingdom"
    def __init__(self, name: str, birthyear: int, sex: str):
        self.name = name
        self.birthyear = birthyear
        self.sex = sex


    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name = '{self.name}', birthyear = '{self.birthyear}', sex='{self.sex}')"
    def says(self, words) -> str:
        return f"{self.name} says {words}"

    @classmethod
    def school_headmistress(cls) -> CastleKilmereMember:
        return cls('Miranda Mirren', 1962, 'female')


class Pupil(CastleKilmereMember):
    def __init__(self, name: str, birthyear: int, sex: str, start_year: int, pet: Tuple[str, str] =None):
        super().__init__(name, birthyear, sex)
        self.start_year = start_year

        if pet is not None:
            self.pet_name, self.pet_type = pet

        self._elms = {
            'Critical Thinking': False,
            'Self-Defense Against Fresh Fruit': False,
            'Broomstick Flying': False,
            'Magical Theory': False,
            'Foreign Magical Systems': False,
            'Charms': False,
            'Defence Against Dark Magic': False,
            'History of Magic': False,
            'Potions': False,
            'Transfiguration': False}



    @staticmethod
    def passed(grade):
        """ Given a grade, determine if an exam was passed.  """
        grades = {
		'E': True,
		'Excellent': True,
                'O': True,
                'Ordinary': True,
                'A': True,
                'Acceptable': True,
                'P': False,
                'Poor': False,
                'H': False,
                'Horrible': False,
                }

        return grades[grade]


    @classmethod
    def luke(cls):
        return cls('Luke Bery', 2008, 'male', 2020, ('Cotton', 'owl'))

    @classmethod
    def lissy(cls):
        return cls('Lissy Spinster', 2008, 'female', 2020, ('Ramses', 'cat'))

    @classmethod
    def adrien(cls):
        return cls('Adrien Fulford', 2008, 'male', 2020, ('Unnamed', 'owl') )


class Professor(CastleKilmereMember):

    def __init__(self, name: str, birthyear: int, sex: str, subject: str):
        super().__init__(name, birthyear, sex)
        self.subject = subject

    @classmethod
    def blade(cls):
        return cls('Blade Bardock', 1988, 'male', 'Potions', 'Science')

    @classmethod
    def briddle(cls):
        return cls('Birdie Briddle', 1931, 'female', 'Foreign Magical Systems', 'Law')

    @classmethod
    def radford(cls):
        return cls('Rupert Radford', 1958, 'male', 'Illusions 101', 'Creativity and Arts')

    @classmethod
    def giddings(cls):
        return cls('Gabriel Giddings', 1974, 'male', 'Broomstick Making', 'Engineering')

class Ghost(CastleKilmereMember):
    def __init__(self, name, birthyear, sex, year_of_death):
        super().__init__(name, birthyear, sex)
        self.year_of_death = year_of_death

if __name__ == '__main__':
    blade = Professor.blade()
    lissy = Pupil.lissy()

    bromley = CastleKilmereMember(name='Bromley Huckabee', birthyear=1959, sex='male')
    print(bromley)