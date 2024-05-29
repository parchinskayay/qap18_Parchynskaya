# Приложение «Касса кинотеатра».
# Спроектировать ПО, предназначенное для автоматизации деятельности кассы
# кинотеатра. Функции, которые должны быть реализованы в приложении:
# добавление, удаление, редактирование и просмотр информации о сеансах,
# наличии билетов и свободных мест.

class Session:
    def __init__(self, film_name, room_number, duration_of_session, count_seats):
        self.film_name = film_name
        self.room_number = room_number
        self.duration_of_session = duration_of_session
        self.count_seats = count_seats
        self.count_of_occupied_seats = 0

    def take_seats(self, count):
        if self.count_of_occupied_seats + count > self.count_seats:
            return (f"Нет {count} свободных мест, осталось только "
                    f"{self.count_seats - self.count_of_occupied_seats}.")
        else:
            self.count_of_occupied_seats += count
            return True

    def info(self):
        return (f"Название фильма: {self.film_name}\n"
                f"Номер зала: {self.room_number}\n"
                f"Продолжительность сеанса: {self.duration_of_session}\n"
                f"Количество мест: {self.count_seats}\n"
                f"Количество свободных: {self.count_of_occupied_seats}\n")

    def get_film_name(self):
        return self.film_name


class Cinema:
    def __init__(self):
        self.sessions = []

    def add_session(self, film_name, room_number, duration_of_session, count_seats):
        session = Session(film_name, room_number, duration_of_session, count_seats)
        self.sessions.append(session)

    def remove_session(self, film_name):
        for session in self.sessions:
            if session.get_film_name() == film_name:
                self.sessions.remove(session)

    def edit_session(self, film_name, count):
        for session in self.sessions:
            if session.get_film_name() == film_name:
                res = session.take_seats(count)
                if res is not True:
                    print(res)
                else:
                    print("Билеты куплены.")

    def info(self, film_name):
        for session in self.sessions:
            if session.get_film_name() == film_name:
                print(session.info())
                return
        print("Такого сеанса не существует.")


cinema = Cinema()
cinema.add_session("Барби", 1, 1.20, 5)
cinema.info("Барби")
cinema.add_session("Титаник", 2, 2.20, 7)
cinema.info("Титаник")
cinema.edit_session("Титаник", 4)
cinema.info("Титаник")
cinema.edit_session("Титаник", 4)
cinema.remove_session("Титаник")
cinema.info("Титаник")
