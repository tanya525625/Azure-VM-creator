import json
from tools.AzureQueue import QueueWorker


if __name__ == "__main__":
    client_queue_name = 'client_queue'
    client_queue = QueueWorker(client_queue_name)
    messages = client_queue.receive_message()

    user_data_dict = json.loads(messages)

    server_queue_name = 'server_queue'
    server_queue = QueueWorker(server_queue_name)
    server_queue.create_queue()
    prediction = server_queue.send_message(user_data_dict['name'])
