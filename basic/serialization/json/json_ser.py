import json
from datetime import datetime

# Basic json serialization and deserialization
event = {
    'name': 'Homer Simpson',
    'item': 'Duff',
    'amout': 4,
    'item price': 4.75
}


def basic_serialization():
    data = json.dumps(event, indent=4)
    print(data)
    return data


def basic_deserialization():
    event_srt = json.loads(basic_serialization())
    print(event_srt)


def basic_serialization_to_file():
    with open('event.json', 'w') as out:
        json.dump(event, out, indent=4)


def basic_deserialization_from_file():
    with open('event.json', 'r') as fp:
        event_str = json.load(fp)
    print(event_str)


# Custom types serialization and deserialization. Json doesn't have datetime object
custom_event = {
    'time': datetime(2021, 8, 13, 12, 26, 0),
    'name': 'Homer Simpson',
    'item': 'Duff',
    'amout': 4,
    'item price': 4.75
}


def default(obj):
    """
    Encode datetime to string in YYYY-MM-DD HH:MM:SS.mmmmmm format
    :param obj: json field
    :return: datetime if obj isinstance
    """
    if isinstance(obj, datetime):
        return obj.isoformat()
    return obj


def pairs_hook(pairs):
    """
    Convert the "time" key to datetime
    :param pairs: key value pair
    :return: map of key value pair
    """
    obj = {}
    for key, value in pairs:
        value = datetime.fromisoformat(value) if key == "time" else value
        obj[key] = value
    return obj


print(custom_event)
ser_data = json.dumps(custom_event, indent=4, default=default)
print(ser_data)

des_data = json.loads(ser_data, object_pairs_hook=pairs_hook)
print(des_data)

# Steaming json

from io import BytesIO

groups = [
    {'animal': 'bee', 'group': 'swarm'},
    {'animal': 'fox', 'group': 'charm'},
    {'animal': 'whale', 'group': 'pod'}
]

# Sending side
network = BytesIO()
for message in groups:
    data = json.dumps(message)
    network.write(data.encode('UTF-8'))  # Sockets work in byte level
    network.write(b'\n')

# Receiving side
network.seek(0)  # Go back to start of data for reading side

while True:
    line = network.readline()
    if not line:
        break

    message = json.loads(line)
    print('got', message)
