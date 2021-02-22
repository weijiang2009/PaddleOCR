import paddle


class MyPostProcess:
    def __init__(self, *args, **kwargs):
        # your init code
        pass

    def __call__(self, preds, label=None, *args, **kwargs):
        if isinstance(preds, paddle.Tensor):
            preds = preds.numpy()
        # you preds decode code
        preds = self.decode_preds(preds)
        if label is None:
            return preds
        # you label decode code
        laebl = self.decode_label(label)
        return preds, label

    def decode_preds(self, preds):
        # you preds decode code
        pass

    def decode_label(self, preds):
        # you label decode code
        pass
