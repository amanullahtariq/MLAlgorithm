from datetime import timedelta
from datetime import datetime

# Meeting room class contains all the details of the
# meeting room
class MeetingRoom:
    def __init__(self,empid, start_time, end_time,req_date,req_time):
        self.start_time = start_time
        self.end_time = end_time
        self.empid = empid
        self.req_date = req_date
        self.req_time = req_time

# Booking detail class
class BookingDetail:
    def __init__(self):
        self.booking_date = None
        self.room_detail = []

    def book(self,booking_date, room_detail):
        '''
         save booking detail
        :param booking_date:
        :param room_detail:
        :return:
        '''
        self.booking_date= booking_date
        self.room_detail.append(room_detail)

# Office class contains all the detail of the offie,
# currently office start and end time is present
class Office:
    def __init__(self, start_time, end_time):
        self.start_time = start_time
        self.end_time = end_time


## Contains all the methods for data saving, validation and to print the output
class DataProcessing:

    def insert(self,meeting_room, meeting_detail, meeting_detail_list):
        is_present = False
        for detail in meeting_detail_list:
            if detail.booking_date == meeting_detail.booking_date:
                is_present = True
                break
        if is_present:
            is_replace = False

            for room in detail.room_detail:
                if room.start_time == meeting_room.start_time:
                    if room.req_time > meeting_room.req_time:
                        is_replace = True
                        break
            if is_replace:
                room.req_time = meeting_room.req_time
                room.req_date = meeting_room.req_date
                room.empid = meeting_room.empid
            else:
                detail.room_detail.append(meeting_room)
        else:
            meeting_detail_list.append(meeting_detail)

        return meeting_detail_list

    def read_input(self):
        # todo: exception handling
        file = open('input2.txt', 'r')
        input = file.read()
        file.close()
        return input

    def print_output(self,meeting_detail_list):
        meeting_detail_list.sort(key=lambda x:x.booking_date)

        number = 1
        for meeting in meeting_detail_list:
            print("Meeting {}".format(number))
            print(meeting.booking_date)
            for detail in meeting.room_detail:
                print("{} {} {}".format(detail.start_time.strftime('%X'), detail.end_time.strftime('%X'), detail.empid))

            print("===========================")
            number += 1

    def validate_time(self,office_detail, booking_date,start_time, end_time):
        '''
        :param office_detail:
        :param booking_date:
        :param start_time:
        :param end_time:
        :return: if start time and end time falls between the office timing
        '''

        result = False
        dt_format = "%Y-%m-%d %H%M"

        opening_time = datetime.strptime(booking_date + " " + office_detail.start_time, dt_format)
        closing_time = datetime.strptime(booking_date + " " + office_detail.end_time, dt_format)

        if start_time >= opening_time and end_time <= closing_time:
            result = True

        return result

def run():
    data_util = DataProcessing()
    input = data_util.read_input()
    lines = input.split("\n")
    opening_time, closing_time = lines[0].split()
    office = Office(opening_time,closing_time)
    dt_format = "%Y-%m-%d %H:%M:%S"

    meeting_detail_list = []

    for i in range(1, len(lines)):
        if i % 2 != 0:
            request_date, request_time, empid = lines[i].split()
            request_time = datetime.strptime(request_date + " " +request_time,dt_format)

        else:
            booking_date, start_time, duration = lines[i].split()
            start_time = datetime.strptime(booking_date + " " +start_time,dt_format)
            end_time = start_time + timedelta(hours=int(duration))

            if data_util.validate_time(office,booking_date, start_time, end_time):
                meeting_detail = BookingDetail()
                meeting_room = MeetingRoom(empid, start_time, end_time, request_date,request_time)
                meeting_detail.book(booking_date, meeting_room)

                meeting_detail_list = data_util.insert(meeting_room, meeting_detail, meeting_detail_list)
            else:
                #todo:display a error message, cannot save
                #print("Meeting time not correct")
                continue

    ## Print the detail of the meetings
    data_util.print_output(meeting_detail_list)


if __name__ == '__main__':
    run()
