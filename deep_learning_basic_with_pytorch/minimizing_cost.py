import torch
import torch.optim as optim
import matplotlib.pyplot as plt
import numpy as np

x_train = torch.FloatTensor([[1], [2], [3]])
y_train = torch.FloatTensor([[1], [2], [3]])

# Data
plt.scatter(x_train, y_train)
xs = np.linspace(1, 3, 1000) # return evenly spaced numbers over a specified interval (start, stop, num=50)
plt.plot(xs, xs)
plt.show()

# Cost by W
# Assume H(x) = W * x
# https://medium.com/@lachlanmiller_52885/machine-learning-week-1-cost-function-gradient-descent-and-univariate-linear-regression-8f5fe69815fd
W_l = np.linspace(-5, 7, 1000)
cost_l = []
for W in W_l:
    hypothesis = W * x_train

    cost = torch.mean((hypothesis - y_train) ** 2)
    cost_l.append(cost.item())

plt.plot(W_l, cost_l)
plt.xlabel('$W$')
plt.ylabel('Cost')
plt.show()

# Gradient Descent by Hand
W = 0

gradient = torch.sum((W * x_train - y_train) * x_train)
print(gradient)

# W = W - (learning rate)a(differential)W
# Weight update by gradient descent
lr = 0.1
W -= lr * gradient
print(W)

# Training
# Naive approach
# Gradient descent
x_train = torch.FloatTensor([[1], [2], [3]])
y_train = torch.FloatTensor([[1], [2], [3]])

W = torch.zeros(1)

lr = 0.1

nb_epochs = 10
for epoch in range(nb_epochs+1):
    hypothesis = x_train * W

    cost = torch.mean((hypothesis - y_train) ** 2)
    gradient = torch.sum((W * x_train - y_train) * x_train)

    print('Epoch {:4d}/{} W: {:.3f}, Cost: {:.6f}'.format(
        epoch, nb_epochs, W.item(), cost.item()
    ))

    # Weight update
    W -= lr * gradient

# SGD
# http://shuuki4.github.io/deep%20learning/2016/05/20/Gradient-Descent-Algorithm-Overview.html
# http://aikorea.org/cs231n/optimization-1/
# https://everyday-deeplearning.tistory.com/entry/SGD-Stochastic-Gradient-Descent-%ED%99%95%EB%A5%A0%EC%A0%81-%EA%B2%BD%EC%82%AC%ED%95%98%EA%B0%95%EB%B2%95

# Training with optim
x_train = torch.FloatTensor([[1], [2], [3]])
y_train = torch.FloatTensor([[1], [2], [3]])

W = torch.zeros(1, requires_grad=True)
optimizer = optim.SGD([W], lr=0.15)

nb_epochs = 10
for epoch in range(nb_epochs + 1):
    hypothesis = x_train * W

    cost = torch.mean((hypothesis - y_train) ** 2)

    print('Epoch {:4d}/{} W: {:.3f} Cost: {:.6f}'.format(
        epoch, nb_epochs, W.item(), cost.item()
    ))

    # https://tutorials.pytorch.kr/beginner/pytorch_with_examples.html

    # https://stackoverflow.com/questions/48001598/why-do-we-need-to-call-zero-grad-in-pytorch
    optimizer.zero_grad() # 역전파 단계를 실행하기 전에 변화도를 0으로 만듭니다.

    # 역전파 단계: 모델의 학습 가능한 모든 매개변수에 대해 손실의 변화도를
    # 계산합니다. 내부적으로 각 Module의 매개변수는 requires_grad=True 일 때
    # Tensor 내에 저장되므로, 이 호출은 모든 모델의 모든 학습 가능한 매개변수의
    # 변화도를 계산하게 됩니다.
    # https://discuss.pytorch.org/t/what-does-the-backward-function-do/9944
    cost.backward() # computes dloss/dx for every parameter x which has requires_grad=True. x.grad += dloss/dx
    print(W.grad)
    optimizer.step() # updates the value of x using the gradient x.grad. SGD; x += -lr * x.grad