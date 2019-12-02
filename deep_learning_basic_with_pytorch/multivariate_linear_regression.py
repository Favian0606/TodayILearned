import torch
import torch.optim as optim
import torch.nn as nn
import torch.nn.functional as F

# For reproducibility
torch.manual_seed(1)

# Data
x1_train = torch.FloatTensor([[73], [93], [89], [96], [73]])
x2_train = torch.FloatTensor([[80], [88], [91], [98], [66]])
x3_train = torch.FloatTensor([[75], [93], [90], [100], [70]])
y_train = torch.FloatTensor([[152], [185], [180], [196], [142]])

# Model initialization
w1 = torch.zeros(1, requires_grad=True)
w2 = torch.zeros(1, requires_grad=True)
w3 = torch.zeros(1, requires_grad=True)
b = torch.zeros(1, requires_grad=True)
# Optimizer
optimizer = optim.SGD([w1, w2, w3, b], lr=1e-5)

nb_epochs = 5000
for epoch in range(nb_epochs+1):

    # H(x)
    hypothesis = x1_train * w1 + x2_train * w2 + x3_train * w3 + b

    # cost
    cost = torch.mean((hypothesis - y_train) ** 2)

    # Fitting model with cost
    optimizer.zero_grad()
    cost.backward() # compute dloss/dx x.grad += dloss/dx
    # print("w1 gradient: {}".format(w1.grad))
    # print("w2 gradient: {}".format(w2.grad))
    # print("w3 gradient: {}".format(w3.grad))
    optimizer.step() # update the value of parameter x using gradient; SGD x += -lr * x.grad

    if epoch % 100 == 0:
        print('Epoch {:4d}/{} w1: {:.3f} w2: {:.3f} w3: {:.3f} b: {:.3f} Cost: {:.6f}'.format(
            epoch, nb_epochs, w1.item(), w3.item(), w3.item(), b.item(), cost.item()
        ))

# Matrix data representation

x_train = torch.FloatTensor([[73, 80, 75],
                             [93, 88, 93],
                             [89, 91, 90],
                             [96, 98, 100],
                             [73, 66, 70]])
y_train = torch.FloatTensor([[152], [185], [180], [196], [142]])

print(x_train.shape) # [5, 3]
print(y_train.shape) # [5, 1]

# Model initialization
W = torch.zeros((3, 1), requires_grad=True)
b = torch.zeros(1, requires_grad=True)

# Optimizer
optimizer = optim.SGD([W, b], lr=1e-5)

nb_epochs = 20
for epoch in range(nb_epochs+1):

    # H(x)
    hypothesis = x_train.matmul(W) + b

    # cost
    cost = torch.mean((hypothesis - y_train) ** 2)

    # Fitting model with cost
    optimizer.zero_grad()
    cost.backward()
    optimizer.step()

    print('Epoch {:4d}/{} hypothesis: {} Cost: {:.6f}'.format(
        epoch, nb_epochs, hypothesis.squeeze().detach(), cost.item()
    ))

class MultivariateLinearRegressionModel(nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = nn.Linear(3, 1)

    def forward(self, x):
        return self.linear(x)

# Data
x_train = torch.FloatTensor([[73, 80, 75],
                             [93, 88, 93],
                             [89, 91, 90],
                             [96, 98, 100],
                             [73, 66, 70]])
y_train = torch.FloatTensor([[152], [185], [180], [196], [142]])

# Model initialization
model = MultivariateLinearRegressionModel()

# Optimizer
optimizer = optim.SGD(model.parameters(), lr=1e-5)

nb_epochs = 20
for epoch in range(nb_epochs+1):

    # H(x)
    prediction = model(x_train)

    # cost
    cost = F.mse_loss(prediction, y_train)

    # Fitting model with cost
    optimizer.zero_grad()
    cost.backward()
    optimizer.step()

    print('Epoch {:4d}/{} Cost: {:.6f}'.format(
        epoch, nb_epochs, cost.item()
    ))