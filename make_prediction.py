from azure.servicebus import Message, ServiceBusService

import json
import random


key_name = 'RootManageSharedAccessKey'
key_value = 'Pyh1POvpagtuCZlth3mFiburtkEYQr9M/hJd5Z+JKSA='
service_namespace = 'appForGrid'


class QueueWorker:
    """ Class for working with queues """

    def __init__(self, queue_name):
        """
        Constructor of the QueueWorker class

        :param queue_name: name of the queue
        """

        self.queue_name = queue_name
        self.sbs = ServiceBusService(service_namespace,
                                     shared_access_key_name=key_name,
                                     shared_access_key_value=key_value)

    def create_queue(self):
        """ Function for queue creation """

        self.sbs.create_queue(self.queue_name)

    def send_message(self, message):
        """ Function for sending messages to the queue """

        # Send a message to the queue
        msg = Message(message)
        self.sbs.send_queue_message(self.queue_name, msg)

    def receive_message(self):
        """ Function for receiving messages from the queue """

        # Receive the message from the queue
        msg = self.sbs.receive_queue_message(self.queue_name, peek_lock=False)
        return msg.body.decode("utf-8").replace("'", '"')


def make_prediction(user_data):
    """
    Function for making the prediction

    :param user_data: user's data
    :return: forecast, prediction for the user
    """

    days_to_success = int(random.uniform(0, 1000))
    forecast = f'{user_data["name"]}, '
    if days_to_success == 0:
        forecast += "you are an extremely successful person. Congratulations!"
    else:
        forecast += f'stars predict you success in {days_to_success} days'

    return forecast


if __name__ == "__main__":
    # receiving data from client
    client_queue_name = 'client_queue'
    client_queue = QueueWorker(client_queue_name)
    messages = client_queue.receive_message()

    # making prediction
    user_data_dict = json.loads(messages)
    prediction = make_prediction(user_data_dict)

    # sending the response to client
    server_queue_name = 'server_queue'
    server_queue = QueueWorker(server_queue_name)
    server_queue.create_queue()
    # adding message to the server_queue
    server_queue.send_message(prediction)
