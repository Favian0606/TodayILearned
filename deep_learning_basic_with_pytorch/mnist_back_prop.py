import torch
import torchvision.datasets as datasets
import torchvision.transforms as transformers

device = 'cuda' if torch.cuda.is_available() else 'cpu'
torch.manual_seed(777)
if device == 'cuda':
    torch.cuda.manual_seed_all(777)

# parameters
learning_rate = 0.5
batch_size = 10

# MNIST dataset
mnist_train = datasets.MNIST(root='MNIST_data/',
                             train=True,
                             transform=transformers.ToTensor(),
                             download=True)

mnist_test = datasets.MNIST(root='MNIST_data/',
                             train=False,
                             transform=transformers.ToTensor(),
                             download=True)

# dataset loader
data_loader = torch.utils.data.DataLoader(dataset=mnist_train,
                                          batch_size=batch_size,
                                          shuffle=True,
                                          drop_last=True)

# nn layers
# Defines parameters manually for custom initialization
# Using torch.nn.Linear, def __init__(self, in_features, out_features, bias=True):
# self.weight = Parameter(torch.Tensor(out_features, in_features))
# weight parameter is created using torch.nn.Parameter
# and initialized by calling reset_parameters;  init.kaiming_uniform_(self.weight, a=math.sqrt(5))
# https://stackoverflow.com/questions/50935345/understanding-torch-nn-parameter
w1 = torch.nn.Parameter(torch.Tensor(784, 30)).to(device)
b1 = torch.nn.Parameter(torch.Tensor(30)).to(device)
w2 = torch.nn.Parameter(torch.Tensor(30, 10)).to(device)
b2 = torch.nn.Parameter(torch.Tensor(10)).to(device)

# batch normalization using normal distribution for each layer
# internal covariate shift; inconsistency of input distribution of each layer
torch.nn.init.normal_(w1)
torch.nn.init.normal_(b1)
torch.nn.init.normal_(w2)
torch.nn.init.normal_(b2)

def sigmoid(x):
    # sigmoid function
    return 1.0 / (1.0 + torch.exp(-x))

# https://towardsdatascience.com/derivative-of-the-sigmoid-function-536880cf918e
def sigmoid_prime(x):
    # derivative of the sigmoid function
    return sigmoid(x) * (1 - sigmoid(x))

X_test = mnist_test.test_data.view(-1, 28 * 28).float().to(device)[:1000]
Y_test = mnist_test.test_labels.to(device).to(device)[:1000]
i = 0
while not i == 10000:
    for X, Y in data_loader:
        i += 1

        # forward
        X = X.view(-1, 28 * 28).to(device)
        Y = torch.zeros((batch_size, 10)).scatter_(1, Y.unsqueeze(1), 1).to(device) # one-hot
        # model
        l1 = torch.add(torch.matmul(X, w1), b1) # linear transformation
        a1 = torch.sigmoid(l1) # sigmoid activation
        l2 = torch.add(torch.matmul(a1, w2), b2) # linear transformation
        y_pred = torch.sigmoid(l2)

        # naive loss
        diff = y_pred - Y

        # Back prop (chain rule)
        # Layer 2
        d_l2 = diff * sigmoid_prime(l2)
        d_b2 = d_l2
        # transpose(Tensor, dim0, dim1)
        d_w2 = torch.matmul(torch.transpose(a1, 0, 1), d_l2)

        # Layer 1
        d_a1 = torch.matmul(d_l2, torch.transpose(w2, 0, 1))
        d_l1 = d_a1 * sigmoid_prime(l1)
        d_b1 = d_l1
        d_w1 = torch.matmul(torch.transpose(X, 0, 1), d_l1)

        # Weight update
        w1 = w1 - learning_rate * d_w1
        b1 = b1 - learning_rate * torch.mean(d_b1, 0)
        w2 = w2 - learning_rate * d_w2
        b2 = b2 - learning_rate * torch.mean(d_b2, 0)

        if i % 1000 == 0:
            l1 = torch.add(torch.matmul(X_test, w1), b1)
            a1 = sigmoid(l1)
            l2 = torch.add(torch.matmul(a1, w2), b2)
            y_pred = sigmoid(l2)
            acct_mat = torch.argmax(y_pred, 1) == Y_test
            acct_res = acct_mat.sum()
            print(acct_res.item())

        if i == 10000:
            break