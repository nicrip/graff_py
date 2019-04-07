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
        reply = self.socket.recv_json() 

        success = False
        if reply['status'] == 'OK':
            success = True
        else:
            reply = {}

        return (reply, success )


    def Status(self):
        """
        Request endpoint status.
        """

        msg = {}
        msg['request'] = 'status'
        msg['payload'] = ''

        (r,s) = self.SendRequest(msg)

        if s:
            return(r)
        else:
            return {}

    def RequestSolve(self):
        """
        Request full batch solve.
        """
        msg = {}
        msg['request'] = 'batchSolve'
        msg['payload'] = ''

        (r,s) = self.SendRequest(msg)

        if s:
            return(r)
        else:
            return {}


    def GetVarMAP(self, variable, estimate ):
        """
        Get the maximum-based MAP estimate for the given variable

        variable - the variable label
        estimate - type of estimate: 'max' or 'mean' (default)
        """

        msg = {}
        if 'max' == estimate:
            msg['request'] = 'getVarMAPMax'
        else:
            msg['request'] = 'getVarMAPMean'
        msg['payload'] = variable
        (r,s) = self.SendRequest(msg)

        if s:
            return(r)
        else:
            return {}


    def Evaluate(self, variables,locations):
        """
        request evaluation of one or more variables at a set of locations
        """
        msg = {}
        msg['request'] = 'evaluate'
        msg['payload'] = {}
        msg['payload']['variables'] = variables
        msg['payload']['locations'] = locations

        (r,s) = self.SendRequest(msg)

        if s:
            return(r)
        else:
            return {}






