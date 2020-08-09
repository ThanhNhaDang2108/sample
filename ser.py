import socket, threading, time
class ClientThread(threading.Thread):
    def __init__(self,clientAddress,clientsocket):
        self.clientAddress = clientAddress
        threading.Thread.__init__(self)
        self.csocket = clientsocket
        print ("New connection added: ", self.clientAddress)
    def write_data(x_temperature, y_humidity, z_time)
        data = {
            'Time': z_time,
            "Temperature": x_temperature,
            'Humidity': y_humidity
        }
        with open('data.txt', 'a', encoding='utf-8') as outfile:  # modify Chos Nhax path file here.
            json.dump(data, outfile)
    def run(self):
        print ("Connection from : ", self.clientAddress)
        #self.csocket.send(bytes("Hi, This is from Server..",'utf-8'))
        msg = ''
        # while True:
        data = self.socket.recv(2048)
        msg = data.decode()
        # if msg=='bye':
        #     break
        # Need parse data function from here
        write_data(msg, 'msg1', 'msg2')
        print ("from client", msg)
        self.csocket.send(bytes(msg,'UTF-8'))
        print ("Client at ", self.clientAddress , " disconnected...")


class socket_cl_ser():
    def __init__(self):
        pass
    def run_server(self):
        LOCALHOST = ""
        PORT = 12345
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server.bind((LOCALHOST, PORT))
        print("Server started")
        print("Waiting for client request..")
        
        server.listen(1)
        clientsock, clientAddress = server.accept()
        newthread = ClientThread(clientAddress, clientsock)
        newthread.start()
        
    def client_send_data(self, message):
        print ("client_send_data")
        # message = "Send from server to client"
        host = '192.168.1.22'

        # Define the port on which you want to connect 
        port = 1234

        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM) 
        s.connect((host,port))
        s.send(str(message).encode('ascii'))
        s.close()
    def start_server(self):
        r = threading.Thread(target=self.run_server, name="run_server")
        r.setDaemon(True)
        r.start()
    def start_client(self, msg):
        l = threading.Thread(target=self.client_send_data, name="client_send_data", args=(msg, ))
        l.setDaemon(True)
        l.start()
so = socket_cl_ser()
while True:
    so.start_server()
    # so.start_client("+++++++++++++++++++hello++++++++++++")

