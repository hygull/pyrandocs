from datetime import date

class Person(object):
    """
    Person
    ======
        - A class to represent a person class 
    """
    def __init__(self, fullname, username, dob, email, profession, address):
        super(Person, self).__init__()

        self.fullname = fullname
        self.username = username
        self.dob = self.__get_dob(dob)
        self.age = self.__get_age()
        self.email = email
        self.profession = profession
        self.address = address

    def __get_dob(self, dob):
        """
            >>> arr = [1, 3, 4]
            >>> x, y, z = a
            >>> x
            1
            >>> y
            3
            >>> z
            4
            >>> 
            >>> def func(a, b, c):
            ...     print(a, b, c)
            ... 
            >>> func(*[55, 67, 88])
            (55, 67, 88)
            >>>
            >>> func(*[55, 67, 88][::-1])
            (88, 67, 55)
            >>> 
        """ 
        dob = date(*[int(data) for data in dob.split('-')][::-1])
        return dob

    def __get_age(self):
        today = date.today()
        delta = today - self.dob
        years = delta.days / 365.25 
        days = delta.days % 365.25
        message = ''

        if years or days:
            message = '{0:d} years {1:d} days (approx.)'.format(int(years), int(days))
        else:
            message = 'Unborn baby'

        return message
            
    def details(self):
        for atrribute_name, atrribute_value in self.__dict__.items():
            print('{0:15s} - {1}'.format(atrribute_name, atrribute_value))


if __name__ == "__main__":
    person = Person(
                'Rishikesh Agrawani', 'hygull',
                '14-05-1992', 'rishikesh0014051992@gmail.com',
                'Python/Node developer', 'Banaglore, India'
            )

    person.details()
    """
    username        - hygull
    dob             - 1992-05-14
    age             - 26 years 263 days (approx.)
    profession      - Python/Node developer
    address         - Banaglore, India
    fullname        - Rishikesh Agrawani
    email           - rishikesh0014051992@gmail.com
    """

		