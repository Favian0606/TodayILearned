import torch
import torch.optim as optim

# Data
x_train = torch.FloatTensor([[1], [2], [3]])
y_train = torch.FloatTensor([[1], [2], [3]])

print("X_train: {}".format(x_train))
print("X_train shape: {}".format(x_train.shape))

# Weight initialization
W = torch.zeros(1, requires_grad=True)
print(W)
print(W.shape)

b = torch.zeros(1, requires_grad=True) # bias
print(b)
print(b.shape)

# Hypothesis
# H(x) = W * x + b
hypothesis = x_train * W + b
print(hypothesis)

# Cost
print(y_train)
print(hypothesis - y_train) # error
print((hypothesis - y_train) ** 2) # squared error
cost = torch.mean((hypothesis - y_train) ** 2)
print(cost)

# Training
optimizer = optim.SGD([W, b], lr=0.01)
nb_epochs = 2000
for epoch in range(nb_epochs+1):

    # Hypothesis
    # H(x) = W * x + b
    hypothesis = x_train * W + b

    # Cost
    cost = torch.mean((hypothesis - y_train) ** 2)

    optimizer.zero_grad()
    cost.backward()
    optimizer.step()

    if epoch % 100 == 0:
        print('Epoch {:4d}/{} W: {:.3f}, b: {:.3f} Cost: {:.6f}'.format(
            epoch, nb_epochs, W.item(), b.item(), cost.item()
        ))