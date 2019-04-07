"""

"""

import zmq

class Endpoint(object):
    """
    A Caesar endpoint object.
    """
    def __init__(self):
        """
        Initialize endpoint object.
        """
        self.context = zmq.Context.instance()
        self.socket = self.context.socket(zmq.REQ)


    def Connect(self, address):
        """
        Connect to endpoint
        """
        self.address = address
        self.socket.connect(self.address)


    def Disconnect(self):
        """
        Disconnect from endpoint
        """
        self.socket.disconnect(self.address)


    def SendRequest(self, request):
        """
        Send request to endpoint.

        This method handles the conversion from native python dictionaries to json.
        """
        # serialize and send message
        # print(request)
        self.socket.send_json(request)# , flags=zmq.NOBLOCK)

        # it is up to the caller to figure out what to do with the reply
        return( self.socket.recv_json() )


    def Status(self):
        """
        Request endpoint status.
        """

        msg = {}
        msg['request'] = 'status'
        msg['payload'] = ''

        reply = self.SendRequest(msg)

        return(reply)



