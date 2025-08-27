import torch.nn as nn
import torch

class ResNet1D(nn.Module):

    def __init__(self,in_channels,out_channels,kernel_size,stride, debug=False):

        super(ResNet1D,self).__init__()

        self.in_channels = in_channels
        self.out_channels = out_channels
        self.debug = debug
    

        # commonly used relu
        self.relu = nn.ReLU()

        # 1x1
        self.conv1_1x1 = nn.Conv1d(in_channels=self.in_channels, out_channels=self.out_channels, kernel_size=kernel_size, stride=stride, padding=0, bias=False )
        self.batchnorm1 = nn.BatchNorm1d(self.out_channels)

    def forward(self,x):
        # input stored to be added before the final relu
        in_x = x

        # conv1x1->BN->relu
        x = self.conv1_1x1(x)
        if self.debug:
            print(f"[ResNet1D/forward] after CONV shape of x {x.shape}")
        
        x = self.batchnorm1(x)
        if self.debug:
            print(f"[ResNet1D/forward] after BatcNorm shape of x {x.shape}")
        
        x = self.relu(x)
        if self.debug:
            print(f"[ResNet1D/forward] after RELU shape of x {x.shape}")


        # identity with trucation
        in_x_truncated = in_x[...,:x.shape[2]]
        x += in_x_truncated

        # final relu
        x = self.relu(x)
        
        return x



def test_ResNet1D_kernel10():
    x = torch.randn(1,300,100) # simuler 300 input channels (second dimention) of size 100 (third dimension) (First dimension 1 for batch?)
    model = ResNet1D(in_channels=300,out_channels=300,kernel_size=10,stride=1,debug=True)
    print(model(x).shape)
    del model

def test_ResNet1D_kernel1():
    x = torch.randn(1,300,100) # simuler 300 input channels (second dimention) of size 100 (third dimension) (First dimension 1 for batch?)
    model = ResNet1D(in_channels=300,out_channels=300,kernel_size=1,stride=1,debug=True)
    print(model(x).shape)
    del model

if __name__ == '__main__':
    print(f"[main] Calling RESNET1D with kernel 10")
    test_ResNet1D_kernel10()
    print(f"[main] Calling RESNET1D with kernel 1")
    test_ResNet1D_kernel1()