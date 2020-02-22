if __name__ == '__main__':
    import time
    import systemd.daemon
    import pika

def rabbit_callback(ch, method, properties, body):
    print(" [x] Received %r" % body.decode())

    print('Starting up ...')
    time.sleep(1)
    print('Startup complete')
    # Tell systemd that our service is ready
    systemd.daemon.notify(systemd.daemon.Notification.READY)

    while True:
        print('Hello from the Python rabbit pull Service')
        connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
        channel = connection.channel()
        channel.queue_declare(queue='hello')

        channel.basic_consume(queue='hello',
                            auto_ack=True,
                            on_message_callback=rabbit_callback)
