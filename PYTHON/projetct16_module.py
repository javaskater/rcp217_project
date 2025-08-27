import torch.nn as nn
import torch.nn.functional as TF
import torch

from resnet1d_module import ResNet1D
from averaging_module import AVERAGING

class Project16(nn.Module):

    def __init__(self, debug=False):

        super(Project16,self).__init__()

        self.debug = debug

        # commonly used relu
        self.relu = nn.ReLU()

        # from 1 time serie to 300 series of length 100 each 
        self.conv1_init = nn.Conv1d(in_channels=1, out_channels=300, kernel_size=10, stride=10, padding=0, bias=False)

        # 4 RESNET 1D with kernel of 10
        self.resnet10_1 = ResNet1D(300, 300, 10, 1, debug=debug)
        self.resnet10_2 = ResNet1D(300, 300, 10, 1, debug=debug)
        self.resnet10_3 = ResNet1D(300, 300, 10, 1, debug=debug)
        self.resnet10_4 = ResNet1D(300, 300, 10, 1, debug=debug)

        # 6 RESNET 1D with kernel of 1
        self.resnet1_1 = ResNet1D(300, 300, 1, 1, debug=debug)
        self.resnet1_2 = ResNet1D(300, 300, 1, 1, debug=debug)
        self.resnet1_3 = ResNet1D(300, 300, 1, 1, debug=debug)
        self.resnet1_4 = ResNet1D(300, 300, 1, 1, debug=debug)
        self.resnet1_5 = ResNet1D(300, 300, 1, 1, debug=debug)
        self.resnet1_6 = ResNet1D(300, 300, 1, 1, debug=debug)

        # The last averaging module
        self.averaging = AVERAGING(debug=self.debug)

    def forward(self,x):

        # conv1x1->BN->relu
        x = self.conv1_init(x)
        # first relu
        x = self.relu(x)
        if self.debug:
            print(f"[Project16/forward] after first convolution and relu shape of x {x.shape}")
        
        # 4 RESNET 1D with kernel of 10
        x = self.resnet10_1(x)
        x = self.resnet10_2(x)
        x = self.resnet10_3(x)
        x = self.resnet10_4(x)
        if self.debug:
            print(f"[Project16/forward] after 4 RESNET1D Blocks of kernel 10 shape of x {x.shape}")
        
        # 6 RESNET 1D with kernel of 1
        x = self.resnet1_1(x)
        x = self.resnet1_2(x)
        x = self.resnet1_3(x)
        x = self.resnet1_4(x)
        x = self.resnet1_5(x)
        x = self.resnet1_6(x)
        if self.debug:
            print(f"[Project16/forward] after 6 RESNET1D Blocks of kernel 1 shape of x {x.shape}")

        # from 300 to 10 feature maps and Averaging each map and outputting 10 softmax values
        x = self.averaging(x)
        x = TF.softmax(x,dim=1)
        if self.debug:
            print(f"[Project16/forward] after Averaging and softmax Blocks shape of x {x.shape}")
        
        return x



def test_Project16():
    x = torch.randn(1,1,1000) # simulate 1 input channels (second dimention) of size 1000 (third dimension) (First dimension 1 for batch?) the time serie we input
    model = Project16(debug=True)
    print(model(x).shape)
    del model

if __name__ == '__main__':
    print(f"[main] Calling Project16")
    test_Project16()