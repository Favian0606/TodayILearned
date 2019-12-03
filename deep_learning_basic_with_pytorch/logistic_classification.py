import torch
import torch.optim as optim
import torch.nn.functional as F

# For reproducibility
torch.manual_seed(1)

# Training data
x_data = [[1, 2], [2, 3], [3, 1], [4, 3], [5, 3], [6, 2]] # 6 x 2
y_data = [[0], [0], [0], [1], [1], [1]] # 6 x 1

# Given the number of hours each student spent watching the lecture and working in the code lab,
# predict whether the student passed or failed a course.

x_train = torch.FloatTensor(x_data)
y_train = torch.FloatTensor(y_data)

print(x_train.shape)
print(y_train.shape)

# Computing the hypothesis
print("e^1 equals: {}".format(torch.exp(torch.FloatTensor([1]))))

W = torch.zeros((2, 1), requires_grad=True)
b = torch.zeros(1, requires_grad=True)

hypothesis = 1 / (1 + torch.exp(-(x_train.matmul(W) + b)))

print(hypothesis)
print(hypothesis.shape)

print("1/(1+e^(-1)) equals: {}".format(torch.sigmoid(torch.FloatTensor([1]))))

hypothesis = torch.sigmoid(x_train.matmul(W) + b)

print(hypothesis)
print(hypothesis.shape)

# Computing the cost function (low-level)
# BCS(Binary Cross-Entropy)
# We want to measure the difference between hypothesis and y_train

# For one element, the loss can be computed as follows
single_loss = -(y_train[0] * torch.log(hypothesis[0])) + (1 - y_train[0]) * torch.log(1-hypothesis[0])
print(single_loss)

losses = -(y_train * torch.log(hypothesis)) + (1 - y_train) * torch.log(1-hypothesis)
print(losses)

cost = losses.mean()
print(cost)

# Computing the cost function with F.binary_cross_entropy
print(F.binary_cross_entropy(hypothesis, y_train))

# Training with low-level binary cross entropy loss
x_data = [[1, 2], [2, 3], [3, 1], [4, 3], [5, 3], [6, 2]]
y_data = [[0], [0], [0], [1], [1], [1]]
x_train = torch.FloatTensor(x_data)
y_train = torch.FloatTensor(y_data)

W = torch.zeros((2, 1), requires_grad=True)
b = torch.zeros(1, requires_grad=True)

optimizer = optim.SGD([W, b], lr=1)

nb_epochs = 1000
for epoch in range(nb_epochs+1):

    # cost
    hypothesis = torch.sigmoid(x_train.matmul(W) + b)
    cost = -(y_train * torch.log(hypothesis) +
            (1 - y_train) * torch.log(1-hypothesis)).mean()

    # fitting model with cost
    optimizer.zero_grad()
    cost.backward()
    optimizer.step()

    if epoch % 100 == 0:
        print('Epoch {:4d}/{} Cost: {:.6f}'.format(
            epoch, nb_epochs, cost.item()))

# Training with F.binary_cross_entropy
W = torch.zeros((2, 1), requires_grad=True)
b = torch.zeros(1, requires_grad=True)

optimizer = optim.SGD([W, b], lr=1)

nb_epochs = 1000
for epoch in range(nb_epochs+1):

    # cost
    hypothesis = torch.sigmoid(x_train.matmul(W) + b)
    # https://curt-park.github.io/2018-09-19/loss-cross-entropy/
    # https://ratsgo.github.io/deep%20learning/2017/09/24/loss/
    # https://wordbe.tistory.com/entry/ML-Cross-entropyCategorical-Binary%EC%9D%98-%EC%9D%B4%ED%95%B4
    # https://kakalabblog.wordpress.com/2017/04/04/cross-entropy-%EC%A0%95%EB%A6%AC/
    # https://taeoh-kim.github.io/blog/cross-entropy%EC%9D%98-%EC%A0%95%ED%99%95%ED%95%9C-%ED%99%95%EB%A5%A0%EC%A0%81-%EC%9D%98%EB%AF%B8/
    cost = F.binary_cross_entropy(hypothesis, y_train)

    # fitting model with cost
    optimizer.zero_grad()
    cost.backward()
    optimizer.step()
    
    if epoch % 100 == 0:
        print('Epoch {:4d}/{} Cost: {:.6f}'.format(
            epoch, nb_epochs, cost.item()))
