"""
Defines a one-to-many dependency between objects so that when one object changes state,
all its dependents are notified and updated automatically.
"""


class Publisher:
    def __init__(self):
        self._subscribers = []

    def add_subscriber(self, subscriber):
        self._subscribers.append(subscriber)

    def remove_subscriber(self, subscriber):
        self._subscribers.remove(subscriber)

    def notify_all_subscribers(self, *args, **kwargs):
        for subscriber in self._subscribers:
            subscriber.update(*args, **kwargs)


class Subscriber:
    def update(self, *args):
        pass


class EmailSubscriber(Subscriber):
    def update(self, subjecte):
        print(f"EmailSubscriber: Received notification on '{subjecte}'")


class SMSSubscriber(Subscriber):
    def update(self, subject):
        print(f"SMSSubscriber: Received notification on '{subject}'")


if __name__ == "__main__":
    publisher = Publisher()

    email_subscriber = EmailSubscriber()
    sms_subscriber = SMSSubscriber()

    publisher.add_subscriber(email_subscriber)
    publisher.add_subscriber(sms_subscriber)

    publisher.notify_all_subscribers("New Product Launch")
    # Output:
    # EmailSubscriber: Received notification on 'New Product Launch'
    # SMSSubscriber: Received notification on 'New Product Launch'

    publisher.remove_subscriber(email_subscriber)
    publisher.notify_all_subscribers("Sale Announcement")
    # Output:
    # SMSSubscriber: Received notification on 'Sale Announcement'
