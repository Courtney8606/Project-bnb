from lib.booking import Booking
from lib.space import Space


class BookingRepository():
    def __init__(self, connection):
        self._connection = connection
        self._bookingstoreview = []
    
    def all(self):
        rows = self._connection.execute('SELECT * from bookings')
        bookings = []
        for row in rows:
            row = Booking(row["id"], row["space_id"], row["date_booked"], row["userid_booker"], row["userid_approver"], row["approved"])
            bookings.append(row)
        return bookings
    
    def all_by_space_id(self, space_id):
        rows = self._connection.execute('SELECT * from bookings WHERE space_id = %s', [space_id])
        bookings = []
        for row in rows:
            row = Booking(row["id"], row["space_id"], row["date_booked"], row["userid_booker"], row["userid_approver"], row["approved"])
            bookings.append(row)
        return bookings

    def create(self, booking):
        self._connection.execute('INSERT INTO bookings (space_id, date_booked, userid_booker, userid_approver, approved) VALUES (%s, %s, %s, %s, %s)', [booking.space_id, booking.date_booked, booking.userid_booker, booking.userid_approver, booking.approved])
        return None

    def delete(self, booking_id):
        self._connection.execute('DELETE FROM bookings WHERE id = %s', [booking_id])
        return None

    def unapproved_bookings(self, user_id, space_id):
        rows = self._connection.execute('SELECT * from bookings WHERE approved = False AND userid_approver = %s AND space_id = %s', [user_id, space_id])
        bookings = []
        for row in rows:
            row = Booking(row["id"], row["space_id"], row["date_booked"], row["userid_booker"], row["userid_approver"], row["approved"])
            bookings.append(row)
        return bookings

    def approved_bookings(self, user_id, space_id):
        rows = self._connection.execute('SELECT * from bookings WHERE approved = True AND userid_approver = %s AND space_id = %s', [user_id, space_id])
        bookings = []
        for row in rows:
            row = Booking(row["id"], row["space_id"], row["date_booked"], row["userid_booker"], row["userid_approver"], row["approved"])
            bookings.append(row)
        return bookings
    
    def approved_bookings_string(self, user_id):
        rows = self._connection.execute('SELECT * from bookings WHERE approved = True AND userid_approver = %s', [user_id])
        bookings = []
        for row in rows:
            date_booked = str(row["date_booked"])
            bookings.append(date_booked)
        return bookings
    
    def unapproved_bookings_by_user_id(self, user_id):
        rows = self._connection.execute('SELECT * from bookings WHERE approved = False AND userid_approver = %s', [user_id])
        bookings = []
        for row in rows:
            row = Booking(row["id"], row["space_id"], row["date_booked"], row["userid_booker"], row["userid_approver"], row["approved"])
            bookings.append(row)
        return bookings

    def approved_bookings_by_user_id(self, user_id):
        rows = self._connection.execute('SELECT * from bookings WHERE approved = True AND userid_approver = %s', [user_id])
        bookings = []
        for row in rows:
            row = Booking(row["id"], row["space_id"], row["date_booked"], row["userid_booker"], row["userid_approver"], row["approved"])
            bookings.append(row)
        return bookings

    def update_approval(self, booking_id):
        self._connection.execute('UPDATE bookings SET approved = True WHERE id = %s', [booking_id])
