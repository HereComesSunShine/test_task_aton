import sqlite3
from mimesis import Person
from mimesis.locales import Locale
from mimesis.builtins import RussiaSpecProvider
from mimesis.enums import Gender

person = Person(Locale.RU)
ru = RussiaSpecProvider()


conn = sqlite3.connect("database.db")
c = conn.cursor()
for i in range(10):
    c.execute(
        "INSERT INTO users (Name, login, password) VALUES (?, ?, ?)",
        (
            person.surname(gender=Gender.MALE)
            + " "
            + person.name(gender=Gender.MALE)
            + " "
            + ru.patronymic(gender=Gender.MALE),
            f"login{i}",
            f"password{i}",
        ),
    )


conn.commit()
conn.close()
