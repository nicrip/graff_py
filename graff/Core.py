import warnings

def MultiplyDistributions(endpoint, distributions):
    """
    Multiply two or more distributions.
    """
    msg = {}
    msg['request'] = 'multiplyDistributions'
    msg['payload'] = {}
    msg['payload']['weights'] =  []

    for i in range(0,len(distributions)):
        msg['payload']['weights'].append(distributions[i].dict())

    (reply, success) = endpoint.SendRequest(msg)

    if success:
        return reply['payload']
    else:
        return {}


def AddVariable(endpoint, variable ):
    """
    Add a variable.
    """
    msg = {}
    msg['request'] = 'addVariable'
    msg['payload'] = variable.dict()

    return(endpoint.SendRequest(msg))


def AddFactor(endpoint, factor):
    """
    Add a factor.
    """
    msg = {}
    msg['request'] = 'addFactor'
    msg['payload'] = factor.dict()

    return(endpoint.SendRequest(msg))

