import unittest
import booking_system


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
        self.assertIsNotNone(result, "Booking system return cannot be null.")
        self.assertEquals(type(result), list, "Return type should be list.")
        self.assertEquals(len(result), 2, "Return type should be list.")


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

        self.assertIsNone(result[0].booking_date, "Booking date cannot be none.")
        self.assertIsNone(result[1].booking_date, "Booking date cannot be none.")

        self.assertLess(result[0].booking_date, result[1].booking_date)

    def test_run_should_return_(self):
        """
        Test if system returns the result in the chronological order
        :return:
        """
        file = 'input2.txt'
        result = booking_system.run(file)
        self.assertIsNotNone(result, "Booking system return cannot be null.")
        self.assertEquals(type(result), list, "Return type should be list.")
        self.assertEquals(len(result), 2, "Return type should be list.")

        self.assertIsNone(result[0].booking_date, "Booking date cannot be none.")
        self.assertIsNone(result[1].booking_date, "Booking date cannot be none.")

        self.assertLess(result[0].booking_date, result[1].booking_date)

    def test_run_should_return_booking_detail_within_office_timing(self):
        """
        Test if system returns the result in the chronological order
        :return:
        """
        file = 'input3.txt'
        result = booking_system.run(file)
        self.assertIsNotNone(result, "Booking system return cannot be null.")
        self.assertEquals(type(result), list, "Return type should be list.")
        self.assertEquals(len(result), 2, "Return type should be list.")

        self.assertIsNone(result[0].booking_date, "Booking date cannot be none.")
        self.assertIsNone(result[1].booking_date, "Booking date cannot be none.")

        self.assertLess(result[0].booking_date, result[1].booking_date)

