# import json
from tools.AzureQueue import QueueWorker


if __name__ == "__main__":
    client_queue_name = 'client_queue'
    client_queue = QueueWorker(client_queue_name)
    messages = client_queue.receive_message()
    # my_dict = json.loads('{' + messages + '}')
    # my_dict = ast.literal_eval(messages)
    # print(my_dict['name'])

    server_queue_name = 'server_queue'
    server_queue = QueueWorker(server_queue_name)
    server_queue.create_queue()
    prediction = server_queue.send_message('answer')
