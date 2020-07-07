import asyncio

async def tcp_echo_client(message, loop):
    reader, writer = await asyncio.open_connection('127.0.0.1', 5687,
                                                   loop=loop)

    print('Send: %r' % message)
    writer.write(message.encode())

    data = await reader.read(100)
    print('Received: %r' % data.decode())

    print('Close the socket')
    writer.close()

async def print_every_second(message, loop):
    for i in range(5):
        reader, writer = await asyncio.open_connection('127.0.0.1', 5687,
                                                       loop=loop)
        print('Send: %r' % message)
        writer.write(message.encode())

        data = await reader.read(100)
        print('Received: %r' % data.decode())

        print('Close the socket')
        writer.close()
        await asyncio.sleep(3)

message = 'Cho Nha~'
loop = asyncio.get_event_loop()
#loop.run_until_complete(asyncio.gather(tcp_echo_client(message, loop),
#                                       print_every_second())
#)
#loop.run_until_complete(tcp_echo_client(message, loop))
loop.run_until_complete(print_every_second(message, loop))

loop.close()
