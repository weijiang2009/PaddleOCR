class MyMetric(object):
    def __init__(self, main_indicator='acc', **kwargs):
        # main_indicator is used for select best model
        self.main_indicator = main_indicator
        self.reset()

    def __call__(self, preds, batch, *args, **kwargs):
        # preds is out of postprocess
        # batch is out of dataloader
        labels = batch[1]
        cur_correct_num = 0
        # you metric code
        self.correct_num += cur_correct_num
        self.all_num += cur_all_num
        return {'acc': cur_correct_num / cur_all_num, }

    def get_metric(self):
        """
        return metrics {
            'acc': 0,
            'norm_edit_dis': 0,
        }
        """
        acc = self.correct_num / self.all_num
        self.reset()
        return {'acc': acc}

    def reset(self):
        # reset metric
        self.correct_num = 0
        self.all_num = 0
