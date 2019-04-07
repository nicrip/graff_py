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
        self.socket = self.context.socket(zmq.ROUTER)

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
        print(request)
        self.socket.send_json(request)# , flags=zmq.NOBLOCK)

        # wait for the reply
        # TODO: check for what flags we need?
        reply = self.socket.recv_json()

        # TODO: check for payload==OK.


    def Status(self):
        """
        Request endpoint status.
        """

        msg = {}
        msg['request'] = 'status'
        msg['payload'] = ''

        reply = self.SendRequest(msg)

        return(reply)



