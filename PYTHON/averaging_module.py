import torch.nn as nn
import torch

class AVERAGING(nn.Module):

    def __init__(self, debug=False):

        super(AVERAGING,self).__init__()
    
        self.debug = debug

        # commonly used relu
        self.relu = nn.ReLU()

        # 1x1
        self.conv1_before_averging = nn.Conv1d(in_channels=300, out_channels=10, kernel_size=10, stride=1, padding=0, bias=False )
        self.batchnorm_before_averging= nn.BatchNorm1d(10)

    def forward(self,x):

        # conv1x1->BN->relu
        x = self.conv1_before_averging(x)
        x = self.batchnorm_before_averging(x)
        x = self.relu(x)
        if self.debug:
            print(f"[AVERAGING/forward] after CONV/NORM/RELU shape of x {x.shape}")
        
        x = torch.mean(x, 2) # calculate the mean on the last dimension (batch size, number of )
        if self.debug:
            print(f"[AVERAGING/forward] after mean operation shape of x {x.shape}")

        return x


def test_Averaging():
    x = torch.randn(1,300,64) # simuler 300 input channels (second dimention) of size 64 (third dimension) (First dimension 1 for batch?)
    model = AVERAGING(debug=True)
    print(model(x).shape)
    del model

if __name__ == '__main__':
    print(f"[main] Calling AVERAING")
    test_Averaging()