from paddle import optimizer as optim

class MyOptim(object):
    def __init__(self, learning_rate=0.001, *args, **kwargs):
        self.learning_rate = learning_rate

    def __call_(self, parameters):
        # It is recommended to wrap the built-in optimizer of paddle
        opt = optim.XXX(
            learning_rate=self.learning_rate,
            parameters=parameters
        )
        return opt
