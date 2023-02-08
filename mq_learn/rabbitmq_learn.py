# -*- coding: utf-8 -*-
"""
@Author     : NIGangJun
@Date       : 2023/2/3 17:37
@File       : rabbitmq_learn.py
@Desc       : RabbitMQ Consumer Producer
"""

import pika

receive_un = 'mq_user'
receive_pw = '123456'
receive_ho = '192.168.0.55'
receive_vh = 'V_HOST'
receive_po = 5672
receive_qu = 'TO_RECEIVE'

send_un = 'mq_user'
send_pw = '123456'
send_ho = '192.168.0.55'
send_vh = 'V_HOST'
send_po = 5672
send_qu = 'TO_SEND'


def send_msg_to_mq(body):
    """
    send
    :param body: string
    :return: close the channel every time the sending is completed. Not return
    """
    # authentication
    au = pika.PlainCredentials(send_un, send_pw)
    # connect
    connection = pika.BlockingConnection(pika.ConnectionParameters(host=send_ho, virtual_host=send_vh, port=send_po, credentials=au))
    # define channel
    channel = connection.channel()
    # define queue
    channel.queue_declare(queue=send_qu, durable=True)
    # publish
    channel.basic_publish(exchange='', routing_key=send_qu, body=body)
    print("RabbitMQ is sending succeeded!")
    connection.close()


def get_msg_from_mq():
    """
    receive
    :return:
    """
    # authentication
    au = pika.PlainCredentials(receive_un, receive_pw)
    # connect
    connection = pika.BlockingConnection(pika.ConnectionParameters(host=receive_ho, virtual_host=receive_vh, port=receive_po, credentials=au))

    # define channel
    channel = connection.channel()
    # define queue
    queue = channel.queue_declare(queue=receive_qu, durable=True)
    # mq count
    message_count = queue.method.message_count
    print(f"Get Msg Count => {message_count}")

    def callback(ch, method, properties, body):
        """
        callback!
        :return:
        """
        try:
            print(f'RabbitMQ Got Message from {receive_qu}: {body.decode("utf-8")}')
        except Exception as err:
            print(f'MSMQ Receive Error! \n {err}')
        finally:
            channel.basic_ack(delivery_tag=method.delivery_tag)

    channel.basic_consume(receive_qu, callback)
    channel.start_consuming()
