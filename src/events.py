from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/events', methods=['GET'])
def get_events():
    events = [
        {
            'event_id': '1',
            'name': 'Opening Ceremony',
            'description': 'Kick-off event for the convention.',
            'schedule': '09:00 AM',
            'location': 'Main Hall',
            'wait_times': '5 mins'
        },
        {
            'event_id': '2',
            'name': 'Tech Talk: AI Innovations',
            'description': 'Discussion on the latest in AI technology.',
            'schedule': '11:00 AM',
            'location': 'Conference Room A',
            'wait_times': '10 mins'
        },
        # Add more events
    ]
    return jsonify(events), 200

if __name__ == '__main__':
    app.run(debug=True)