class Factor(object):
    def __init__(self, factorType, variables, measurement):
        """
        Initialize the factor object

        factorType - the factor type (e.g. Pose3Pose3)
        variables - a list of the variables affected by the factor
        measurement - the distribution describing the measurement
        """
        self.factorType = factorType
        self.variables = variables
        self.measurement = measurement

    def dict(self):
        d = {}
        d['factorType'] = self.factorType
        d['variables'] = self.variables
        d['factor'] = {}
        d['factor']['measurement'] = {}
        # for i in range(0, len(self.measurement)):
        #     d['factor']['measurement'] = self.measurement[i].dict()
        d['factor']['measurement'] = self.measurement.dict()

        return(d)


