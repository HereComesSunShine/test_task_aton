import sqlite3
from mimesis import Person, Generic, Locale, Finance
from mimesis.builtins import RussiaSpecProvider
from mimesis.enums import Gender

conn = sqlite3.connect("database.db")
c = conn.cursor()

c.execute("SELECT Name FROM users")
users = c.fetchall()


person = Person(Locale.RU)
generic = Generic(Locale.RU)
ru = RussiaSpecProvider()

for index,user in enumerate(users):
    print(user[0])
    acc_number=10000000*index
    for i in range(5):
        c.execute(
            "INSERT INTO clients (acc_number, Surname, Name, F_name, Birth_date, INN, Manager) VALUES ( ?, ?, ?, ?, ?, ?, ?)",
            (
                acc_number,
                person.surname(gender=Gender.MALE),
                person.name(gender=Gender.MALE),
                ru.patronymic(gender=Gender.MALE),
                generic.datetime.date(start=1980,end = 2000),
                ru.inn(),
                user[0],
                
            ),
        )
        acc_number+=1
conn.commit()
conn.close()
