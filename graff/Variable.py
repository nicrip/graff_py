class Variable(object):
    def __init__(self, label, varType, N=50, userLabels=['']):
        """
        Variable object
        label - the variable name (e.g x0)
        varType - the type of variable (e.g. Pose3)
        N - the number of particles to use (e.g. 50)
        userLabels - user-specified labels to describe the variable
        """
        self.label = label
        self.varType = varType
        self.N = N
        self.userLabels = userLabels

    def dict(self):
        d = {}
        d['label'] = self.label
        d['varType'] = self.varType
        d['N'] = self.N
        d['userLabels'] = self.userLabels

        return(d)
