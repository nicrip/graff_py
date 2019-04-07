

def MultiplyDistributions(endpoint, distributions):
    msg = {}
    msg['request'] = 'MultiplyDistributions'
    msg['payload'] = []

    for i in range(0,len(distributions)):
          msg['payload'].append(distributions[i].dict())

    endpoint.SendRequest(msg)


