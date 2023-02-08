# -*- coding: utf-8 -*-
"""
@Author     : NIGangJun
@Date       : 2023/1/18 11:40
@File       : msmq_learn.py
@Desc       : MSMQ Consumer Producer
"""

import os
import random
import socket
import time
from concurrent.futures import ThreadPoolExecutor

import win32com.client


def receive_messages(queue_name: str):
    queue_info.FormatName = f'direct=TCP:192.168.0.55\\private$\\{queue_name}'
    queue = None

    try:
        queue = queue_info.Open(1, 0)

        while True:
            msg = queue.Receive()
            print(f'Got Message from {queue_name}: {msg.Label} - {msg.Body}')

    except Exception as e:
        print(f'Error! {e}')

    finally:
        queue.Close()


# MSMQ特性：程序一定要部署在服务所在机器才能进行接收
def receive_main():
    with ThreadPoolExecutor(max_workers=2) as executor:
        for queue in queues:
            executor.submit(receive_messages, queue)


def send_message(queue_name: str, label: str, message: str):
    queue_info.FormatName = f'direct=TCP:192.168.0.55\\PRIVATE$\\{queue_name}'
    queue = None

    try:
        queue = queue_info.Open(2, 0)
        msg = win32com.client.Dispatch("MSMQ.MSMQMessage")
        msg.Label = label
        msg.Body = message
        msg.Send(queue)

    except Exception as e:
        print(f'Error! {e}')

    finally:
        queue.Close()


def send_main():
    i = 0
    while True:
        i += 1
        send_message(random.choice(queues), 'test label', f'{i}: this is a test message')
        print(f'{i}: Message sent!')
        time.sleep(10)


if __name__ == '__main__':
    Compute_name = socket.getfqdn(socket.gethostname())  # get name
    print(Compute_name)
    queue_info = win32com.client.Dispatch("MSMQ.MSMQQueueInfo")
    computer_name = os.getenv('COMPUTERNAME')
    queues = ['MQ-TEST-SEND']
    send_main()
    print("running")
