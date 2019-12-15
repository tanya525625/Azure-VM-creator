import json
import random
from tools.AzureQueue import QueueWorker


def make_prediction(user_data):
    days_to_success = int(random.uniform(0, 1000))
    forecast = f'{user_data["name"]}, '
    if days_to_success == 0:
        forecast += "you are an extremely successful person. Congratulations!"
    else:
        forecast += f'stars predict you success in {days_to_success} days'

    return forecast


if __name__ == "__main__":
    client_queue_name = 'client_queue'
    client_queue = QueueWorker(client_queue_name)
    messages = client_queue.receive_message()

    user_data_dict = json.loads(messages)
    prediction = make_prediction(user_data_dict)

    server_queue_name = 'server_queue'
    server_queue = QueueWorker(server_queue_name)
    server_queue.create_queue()
    server_queue.send_message(prediction)
