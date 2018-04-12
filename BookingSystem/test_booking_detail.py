import unittest
import booking_system
from datetime import datetime
from datetime import timedelta

# Todo: Unit test for test cases:
#  1) When no input file is provided
#  2) When input format is incorrect
#  3) Test for more number of data
#  4) Load Testing
#  5) Test all other classes

# Unit test class for booking system
class TestBookingSystem(unittest.TestCase):
    def test_run_should_not_return_empty(self):
        """
        Test if booking system is not returning None values
        :return:
        """
        file = 'input.txt'
        result = booking_system.run(file)
        self.assertIsNotNone(result, "Booking system return cannot be null.")
        self.assertEquals(type(result), list, "Return type should be list.")
        self.assertEquals(len(result), 2, "Return type should be list.")

    def test_run_should_return_meetings_requested_first(self):
        """
        If two or more meetings are on the same-time then the
         room is allocated to the employee who have requested it first
        :return:
        """
        file = 'input.txt'
        result = booking_system.run(file)
        dt_allow = "2015-08-17 10:17:06"
        empid_allow = "EMP001"

        self.assertIsNotNone(result, "Booking system return cannot be null.")
        self.assertEquals(type(result), list, "Return type should be list.")
        self.assertEquals(len(result), 2, "Return type should be list.")

        self.assertNotEqual(result[0].booking_date, dt_allow, "This date is not allow.")

        self.assertIsNotNone(result[0].room_detail, "Room detail should not be empty.")

        for meeting_detail in result[0].room_detail:
            self.assertNotEqual(meeting_detail.empid, empid_allow, "This employee should not be in the list.")

    def test_run_should_return_in_chronological_order(self):
        """
        Test if system returns the result in the chronological order
        :return:
        """
        file = 'input1.txt'
        result = booking_system.run(file)
        self.assertIsNotNone(result, "Booking system return cannot be null.")
        self.assertEquals(type(result), list, "Return type should be list.")
        self.assertEquals(len(result), 2, "Return type should be list.")

        self.assertIsNotNone(result[0].booking_date, "Booking date cannot be none.")
        self.assertIsNotNone(result[1].booking_date, "Booking date cannot be none.")

        self.assertLess(result[0].booking_date, result[1].booking_date)

    def test_run_should_return(self):
        """
        Test if system returns the result in the chronological order
        :return:
        """
        file = 'input2.txt'
        result = booking_system.run(file)
        self.assertIsNotNone(result, "Booking system return cannot be null.")
        self.assertEquals(type(result), list, "Return type should be list.")
        self.assertEquals(len(result), 3, "Return type should be list.")



    def test_run_should_return_booking_detail_within_office_timing(self):
        """
        Test if system returns the result in the chronological order
        :return:
        """
        file = 'input3.txt'
        result = booking_system.run(file)

        start_time = "09:00"
        end_time = "17:30"
        dt_format = "%Y-%m-%d %H:%M"

        self.assertIsNotNone(result, "Booking system return cannot be null.")
        self.assertEquals(type(result), list, "Return type should be list.")
        self.assertEquals(len(result), 2, "Return type should be list.")


        #for result
        is_correct_time = True
        for detail in result:
            opening_time = datetime.strptime(detail.booking_date + " " + start_time, dt_format)
            closing_time = datetime.strptime(detail.booking_date + " " + end_time, dt_format)
            for meeting_detail in detail.room_detail:

                self.assertGreaterEqual(meeting_detail.start_time, opening_time,  "Meeting should be within opening time of the office.")
                self.assertLessEqual(meeting_detail.end_time, closing_time,
                                        "Meeting should be within opening time of the office.")



