class ServingCell:
    """ a common environment to serve a single model """

    def __init__(self):

        self.cell_snapshot = {}; #here we will store inputs and outputs with trace ids;
        return True;

    def prepareInput(self, Input):

        return True;

    def scoreTheModel(self):

        return True;

    def preparePrediction(self):

        return True;

    def liveSign(self):

        return True;