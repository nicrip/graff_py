

def MultiplyDistributions(endpoint, distributions):
    """
    """
    msg = {}
    msg['request'] = 'multiplyDistributions'
    msg['payload'] = {}
    msg['payload']['weights'] =  []

    for i in range(0,len(distributions)):
        msg['payload']['weights'].append(distributions[i].dict())

    return(endpoint.SendRequest(msg))


def AddVariable(endpoint, variable ):
    """
    """
    msg = {}
    msg['request'] = 'addVariable'
    msg['payload'] = variable

    return(endpoint.SendRequest(msg))

def AddFactor(endpoint, factor):
    """
    """
    msg = {}
    msg['request'] = 'addFactor'
    msg['payload'] = factor

    return(endpoint.SendRequest(msg))

