Create a Django project. Use React for frontend.
With models:

Flat
 - name

Booking
  -flat(FK)
  -checkin(date)
  -checkout(date)


Add the django view with the table of Bookings with "previous booking ID".
A previous booking is a booking that is before by date the current one for the same flat.


Example:
Bookings for
Flat-1
(1, 2022-01-01, 2022-01-13)
(2, 2022-01-20, 2022-02-10)
(3, 2022-02-20, 2022-03-10)

Flat-2
(4, 2022-01-02, 2022-01-20)
(5, 2022-01-20, 2022-02-11)

Result table:

|Flat name  |ID|Checkin    |Checkout  |Previous booking  ID    |
|flat-1     |1 | 2022-01-01|2022-01-13| -                      |
|flat-1     |2 | 2022-01-20|2022-02-10| 1                      |
|flat-1     |3 | 2022-02-20|2022-03-10| 2                      |
|flat-2     |4 | 2022-01-02|2022-01-20| -                      |
|flat-2     |5 | 2022-01-20|2022-01-11| 4                      |

Default order is (flat ID, booking checkin). Add ability to have a sorting by booking#checkin.
Keep in mind the performance.

Create it into GitHub repo and provide a link to it.
Tech note: please install shell-plus and djanog-debug-toolbar to the app.
