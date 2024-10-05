import unittest
from app import create_app
from app.utils.database import db
from app.models.event import Event

class EventTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_event_creation(self):
        new_event = Event(name="Test Event", time="10:00 AM", description="This is a test event.")
        db.session.add(new_event)
        db.session.commit()

        event = Event.query.first()
        self.assertEqual(event.name, "Test Event")

if __name__ == '__main__':
    unittest.main()