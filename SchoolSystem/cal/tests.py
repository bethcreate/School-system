from django.test import TestCase

# Create your tests here.
class CalenderModelTestCase(TestCase):
    def setUp(self):
        self.calender=Event(Event_Name="Midterm",
        Event_participants="Lisalab",
        Event_planner="Samantha",
        Events_approved_by="Marie",
        Events_id="1212889137"
     )
    def test_calender_Event_participants(self):
        self.assertIn(self.calender.Event_participants())
    def test_calender_Event_planner(self):
        self.assertIn(self.calender.Event_planner())
    def test_calender_Events_id(self):
        self.assertIn(self.calender.Event_Name())