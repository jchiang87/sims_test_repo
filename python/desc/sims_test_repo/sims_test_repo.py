class sims_test_repo(object):
    '''
    Example class for sims_test_repo package.
    '''
    def __init__(self, message):
        self.message = message

    def run(self, raise_error=False):
        if raise_error:
            raise RuntimeError()
        return self.message
