import paddle
from paddle import nn

class MyLoss(nn.Layer):
    def __init(self, **kwargs):
        super(MyLoss, self).__init__()
        # you init code
        pass

    def __call__(self, predicts, batch):
        label = batch[1]
        # your loss code
        loss = self.loss(input=predicts, label=label)
        return {'loss': loss}
