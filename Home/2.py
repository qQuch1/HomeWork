def user_data(name, surname, birth, sity, email, phone):
    return ", ".join([name, surname, birth, sity, email, phone])
print(user_data(name="Max", surname="Bgdn", birth="2003", sity="Moscow", email="mail@mail", phone="899999999"))
