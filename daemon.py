if __name__ == '__main__':
    import time
    import systemd.daemon

    print('Starting up ...')
    time.sleep(5)
    print('Startup complete')
    # Tell systemd that our service is ready
    systemd.daemon.notify('READY=1')

    while True:
        print('Hello from the Python Demo Service')
        time.sleep(5)
