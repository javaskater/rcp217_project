# Créer un réseau neuronal
* cf [Chapter 8 of my book Deep Learning with Pytorch 2nd Edition at Manning](https://www.manning.com/books/deep-learning-with-pytorch-second-edition)
  * Le [code correspondant est sur GitHub](https://github.com/deep-learning-with-pytorch/dlwpt-code/blob/master/p1ch8/1_convolution.ipynb)
    * training [30] et [31]
    * calcul [32]
* Chapter 8.2
  * nn.Conv1d for Time series (What we are looking for)
  * nn.Conv2d for Images
  * nn.Conv3d vor videos
# 250
* Plus il y a de output channels
  * the more of the ouput channels the more of the features detected
# 251
* output=16 means 16 3x3 coefficients for each of the input channel: total tensor 16 x 3 x (3x3)
* we only have 16 biases (one for each output channel, no input channel's bias)
* we cn heve the weights'shape
```python
# In[8]:
conv.weight.shape, conv.bias.shape
# Out[8]:
(torch.Size([16, 3, 3, 3]), torch.Size([16]))
```
# 252 unsqueeze(img, 0)
* or adding an input dimension to an image (order in the batch for each batch's image)
# 253
* 8.2.1 the size at the bottom are without padding
* padding is 3//2 = 1 in the case of our 3 x 3 kernel
* we pad with zeros
# 254 
* we see the output shape and the output image of a simple convolution
  * so we can test step by step
# 255:
* palying with kernels, for example an edge detection kernel
# 256
* Fugure 8.7
> With deep learning, we let kernels be estimated from data in whatever way the
> discrimination is most effective
# 257
* each output channel stands for a different discriminating filter
# 258
* max pooling or strides greater than one are means of downsampling
# 259
* There is a size to maxpooling
```python
# In[21]:
pool = nn.MaxPool2d(2) # we make Squares of 2 x 2 in the orginal image to calulate the max of
output = pool(img.unsqueeze(0)) # each layer receives a tensor with the order of the imaege in the batch as the first dimension
```
# 260
* At the end of the page we turn the 8ch x (8x8) to a 1D  vector
# 262
* view to pass from 8ch x (8x8) convolution output to a 512 Linear vector ... 
## Subclassing nn.Module
* could replace nn.Sequencial but also things like n entire network which then become just one step of an embedding network (Recusive property of nn.Module)...
# 263
* *self.fc1*: fc stands for fully connected
* only the forward method is mandatory
* one entry of the linear will have 8x8x8 parameters, -1 to tell we don't kno how many of such entries there will be in the batch
  * so we don't know the size of the first dimension of the resulting matrix
# 265
> Recall that the goal of classification networks typically is to compress information in the
> sense that we start with an image with a sizable number of pixels and compress it into (a
> vector of probabilities of) classes
# 268
* many good scientist detremine the size of the first Linear layer using try and error
# 269
* optimizer.step() updates the model using the gradients we just computed
# 270 
* exactly what I need to do on my work. How the different elements work together
# 271
* Code exactly what we need :
* Only question in outputs, what is the first dimension ?
  * predicted is an Tensor (length = batch's size)
```python
for imgs, labels in loader:
outputs = model(imgs)
_, predicted = torch.max(outputs, dim=1) # What is the 0 ouput ?
correct += int((predicted == labels).sum()) # predicted is a tensor just like labels the == returs a Tensor of 1  = True and 0 == False
```
# 273
* very important to save the weights of a model (and to reload them when needed)
# 275
* we move the Tensors (imgs and labels) and the model to the device (torch.device)
# 276
* we go to more complex problems of no use for my project ...
# 7.1.2 The Dataset class
# 216 implementing a proper DataSet
* From images and labels
# 232
```python
# view(-1) transforms the 32x32x3 to a linear vector of size 3072
img_tensor = img.view(-1).unsqueeze(0) 
```
# 236
* another full FCC network (training part)
* labels are the label indices ...
# 237
* ful FCC network, validation part
# 239
* intersting calculation to get the number of elements
# Calculating the Error
## 269 of the latest book edition (MEAP: evolving)
* source code blocks 30 and 31 of [Chapter 8 Jupyter Notebook](https://github.com/deep-learning-with-pytorch/dlwpt-code/blob/master/p1ch8/1_convolution.ipynb)
* bloc code 5 for creating the data for labelling (0, or 1)  [Chapter 8 Jupyter Notebook](https://github.com/deep-learning-with-pytorch/dlwpt-code/blob/master/p1ch8/1_convolution.ipynb)