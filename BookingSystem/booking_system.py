from datetime import timedelta
from datetime import datetime
import argparse
import doctest

parser = argparse.ArgumentParser()
parser.add_argument('--input_file_path', type=str, default='input.txt',
                    help='File path to the input file')



# Meeting room class contains all the details of the
# meeting room
class MeetingRoom:
    def __init__(self,empid, start_time, end_time,req_date,req_time):
        """

        :param empid:
        :param start_time:
        :param end_time:
        :param req_date:
        :param req_time:

        """
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

    def update_existing_record(self, detail, meeting_room):
        """
        Check if the booking of meeting room is already present
        for the time, if yes then request which was done first
        is added to the list and other is ignore
        :param detail:
        :param meeting_room:
        :return:
        """

        is_replace = False
        for room in detail.room_detail:
            if room.start_time == meeting_room.start_time:
                if room.req_time > meeting_room.req_time:
                    is_replace = True
                    break
        return is_replace, room

    def check_date_entry_exist(self, meeting_detail_list, booking_detail):
        """
        Check if the entry against the booking date is already present
        :param meeting_detail_list:
        :param booking_detail:
        :return: True if date entry already exist in the list
        """
        is_present = False
        # Check if the entry against the booking date is already present
        exist_detail = None
        for detail in meeting_detail_list:
           #print(detail)
            if detail.booking_date == booking_detail.booking_date:
                is_present = True
                exist_detail = detail
                break
        return is_present, exist_detail

    def insert(self,meeting_room, booking_detail, meeting_detail_list):
        """
        Insert the new date data or update the existed data
        :param meeting_room: room detail
        :param booking_detail: booking detail
        :param meeting_detail_list: list of meeting details
        :return: List of all the meeting details
        """

        is_present, exist_detail = self.check_date_entry_exist(meeting_detail_list, booking_detail)

        if is_present:
            is_replaceable, room = self.update_existing_record( exist_detail, meeting_room)
            if is_replaceable:
                room.req_time = meeting_room.req_time
                room.req_date = meeting_room.req_date
                room.empid = meeting_room.empid
            else:
                exist_detail.room_detail.append(meeting_room)
        else:
            meeting_detail_list.append(booking_detail)

        return meeting_detail_list

    def read_input(self,input_file_path):
        """
        Read the input file
        :return: the list of inputs
        """
        # todo: exception handling
        file_mode = 'r'
        file = open(input_file_path, file_mode)
        input = file.read()
        file.close()
        return input



    def validate_office_time(self,office_detail, booking_date,start_time, end_time):
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

    def validate_booking_request_time(self, request_time, start_time):
        """
        Validate if the meeting room requested time is correct
        :param request_time:
        :param start_time:
        :return: True if request time is before the start time of the meeting
        """
        result = False

        if start_time >= request_time:
            result = True

        return result

def process_booking_detail(lines,data_util):

    opening_time, closing_time = lines[0].split()
    office = Office(opening_time, closing_time)

    meeting_detail_list = []

    # Extracting input data and saving it
    for i in range(1, len(lines)):
        if i % 2 != 0:
            request_date, request_time, empid = lines[i].split()
            request_time = datetime.strptime(request_date + " " + request_time, "%Y-%m-%d %H:%M:%S")

        else:
            booking_date, start_time, duration = lines[i].split()
            start_time = datetime.strptime(booking_date + " " + start_time, "%Y-%m-%d %H:%M")
            end_time = start_time + timedelta(hours=int(duration))

            if data_util.validate_office_time(office, booking_date, start_time,
                                              end_time) and data_util.validate_booking_request_time(request_time,
                                                                                                    start_time):
                meeting_detail = BookingDetail()
                meeting_room = MeetingRoom(empid, start_time, end_time, request_date, request_time)
                meeting_detail.book(booking_date, meeting_room)

                meeting_detail_list = data_util.insert(meeting_room, meeting_detail, meeting_detail_list)
            else:
                # todo:display a error message for not saving the meeting data
                continue
    return meeting_detail_list

def print_output(meeting_detail_list):
    """
    Print the list of meeting detail in the chronological order
    :param meeting_detail_list:
    :return:
    """

    number = 1
    for meeting in meeting_detail_list:
        print("Meeting {}".format(number))
        print(meeting.booking_date)
        for detail in meeting.room_detail:
            print("{} {} {}".format(detail.start_time.strftime('%X'), detail.end_time.strftime('%X'), detail.empid))

        print("===========================")
        number += 1

def run(input_file_path):
    """
    Extract the input from the file, book all the meeting and
    output the meeting detail
    :param input_file_path:
    :return: The list of meetings detail
    """
    # Initialization
    data_util = DataProcessing()

    # Read input from the file
    input = data_util.read_input(input_file_path)
    lines = input.split("\n")

    #
    meeting_detail_list = process_booking_detail(lines, data_util)

    meeting_detail_list.sort(key=lambda x: x.booking_date)

    return meeting_detail_list


if __name__ == '__main__':
    args = parser.parse_args()
    input_file_path = args.input_file_path
    meeting_detail_list = run(input_file_path)
    ## Print the detail of the meetings
    print_output(meeting_detail_list)
