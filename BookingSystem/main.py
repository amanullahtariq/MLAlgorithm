from datetime import timedelta
from datetime import datetime

class MeetingRoom:
    def __init__(self,empid, start_time, end_time, date):
        self.start_time = start_time
        self.end_time = end_time
        self.date = date
        self.empid = empid


class MeetingDetail:
    def __init__(self):
        self._req_date = None
        self._req_time = None
        self._room_detail = []

    def booking(self, date, time, meeting_detail):
        self._req_date = date
        self._req_time = time
        self._room_detail = meeting_detail

class Office:
    def __init__(self, start_time, end_time):
        self.start_time = start_time
        self.end_time = end_time


def read_input():
    file = open('input.txt', 'r')
    input = file.read()
    file.close()
    return input


input = read_input()
lines = input.split("\n")
opening_time, closing_time = lines[0].split()
office = Office(opening_time,closing_time)

meeting_detail_list = []
meeting_detail = MeetingDetail()

for i in range(1, len(lines)):
    if i % 2 != 0:
        request_date, request_time, empid = lines[i].split()

    else:
        date, start_time, duration = lines[i].split()
        #end_time = start_time + timedelta(hours=duration)
        start_time = datetime.strptime(date + " " +start_time,"%Y-%m-%d %H:%M")
        end_time = start_time + timedelta(hours=int(duration))
        print (end_time)

        #meeting_room = MeetingRoom(empid,start_time, end_time, date )

        #meeting_detail.booking(request_date, request_date)