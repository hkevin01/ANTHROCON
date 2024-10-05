from flask import Blueprint, jsonify
from ..models.event import Event

event_bp = Blueprint('event', __name__)

@event_bp.route('/events', methods=['GET'])
def get_events():
    events = Event.query.all()
    return jsonify([{"id": event.id, "name": event.name, "time": event.time, "description": event.description} for event in events]), 200