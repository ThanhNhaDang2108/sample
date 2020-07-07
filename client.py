import asyncio

async def check_request_from_server(message, loop):
    while True:
        reader, writer = await asyncio.open_connection('127.0.0.1', 5687,
                                                         loop=loop)
        writer.write(message.encode())

        data = await reader.read(100)

        data_dec = data.decode()
        if data_dec == '1':
            print('Send data immediately')
            print('Received: %r' % data.decode())
        await asyncio.sleep(3) # Will remove this

async def send_data_each_five_mins(message, loop):
    while True:
        reader_, writer_ = await asyncio.open_connection('127.0.0.1', 5687,
                                                         loop=loop)
        print('Send: %r' % message)
        writer_.write(message.encode())

        print('Close the socket')
        writer_.close()
        await asyncio.sleep(3)

message = 'Hello Cho Nha!'
loop = asyncio.get_event_loop()

try:
    loop.run_until_complete(asyncio.gather(check_request_from_server(message, loop),
                                           send_data_each_five_mins(message, loop)))
except KeyboardInterrupt:
    pass

loop.close()
