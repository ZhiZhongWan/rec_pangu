# -*- ecoding: utf-8 -*-
# @ModuleName: lr
# @Author: wk
# @Email: 306178200@qq.com
# @Time: 2022/6/10 7:40 PM
from torch import nn
from ..layers import LR_Layer

class LR(nn.Module):
    def __init__(self,
                 loss_fun='torch.nn.BCELoss()',
                 enc_dict=None):
        super(LR, self).__init__()

        self.loss_fun = eval(loss_fun)
        self.enc_dict = enc_dict
        self.lr_layer = LR_Layer(enc_dict=self.enc_dict)

    def forward(self, data):
        y_pred = self.lr_layer(data)
        y_pred = y_pred.sigmoid()
        # 输出
        loss = self.loss_fun(y_pred.squeeze(-1), data['label'])
        output_dict = {'pred': y_pred, 'loss': loss}
        return output_dict
