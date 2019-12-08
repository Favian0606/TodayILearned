# from mnist_softmax
import torch
import torchvision.datasets as datasets
import torchvision.transforms as transformers
import random
import matplotlib.pyplot as plt

device = 'cuda' if torch.cuda.is_available() else 'cpu'

# for reproducibility
random.seed(777)
if device == 'cuda':
    torch.cuda.manual_seed_all(777)

# parameters
learning_rate = 0.001
training_epochs = 15
batch_size = 100
drop_prob = 0.3

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

# neural network layers
linear1 = torch.nn.Linear(784, 256, bias=True)
linear2 = torch.nn.Linear(256, 256, bias=True)
linear3 = torch.nn.Linear(256, 10, bias=True)
relu = torch.nn.ReLU()
bn1 = torch.nn.BatchNorm1d(256)
bn2 = torch.nn.BatchNorm1d(256)
dropout = torch.nn.Dropout(p=drop_prob)

# normal distribution initializtion
torch.nn.init.normal_(linear1.weight)
torch.nn.init.normal_(linear2.weight)
torch.nn.init.normal_(linear3.weight)

# model
# model = torch.nn.Sequential(linear1, relu, linear2, relu, linear3).to(device)
model = torch.nn.Sequential(linear1, bn1, relu,
                            linear2, bn2, relu,
                            linear3).to(device)

# define cost/loss and optimizer
criterion = torch.nn.CrossEntropyLoss().to(device)# Softmax is internally computed
optimizer = torch.optim.Adam(model.parameters(), lr=learning_rate)

train_losses = []
train_accs = []

total_batch = len(data_loader)
for epoch in range(training_epochs):
    avg_cost = 0

    for X, Y in data_loader:
        # reshape input image into [batch_size by 784]
        # label is not one-hot encoded
        X = X.view(-1, 28 * 28).to(device)
        Y = Y.to(device)

        optimizer.zero_grad()
        hypothesis = model(X)
        cost = criterion(hypothesis, Y)
        cost.backward()
        optimizer.step()

        # avg_cost += cost / total_batch
        with torch.no_grad():
            model.eval()  # Set the model to evaluation mode

            # Test the model using train sets
            eval_loss, eval_acc = 0, 0
            for i, (X, Y) in enumerate(data_loader):
                X = X.view(-1, 28 * 28).to(device)
                Y = Y.to(device)

                eval_prediction = model(X)
                eval_correct_prediction = torch.argmax(eval_prediction, dim=1) == Y
                eval_loss += criterion(eval_prediction, Y)
                eval_acc += eval_correct_prediction.float().mean()

            eval_loss, eval_acc = eval_loss / total_batch, eval_acc / total_batch

            train_losses.append([eval_loss])
            train_accs.append([eval_acc])
            # newer than python3.6
            # https://www.python.org/dev/peps/pep-0498/
            print(f'[Epoch {(epoch+1)}-TRAIN] BatchNorm Loss(Acc): eval_loss: {eval_loss}({eval_acc})')
    # print('Epoch:', '%04d' % (epoch + 1), 'cost =', '{:.9f}'.format(avg_cost))

print('Learning finished')

def plotting_metrics(loss_list, ylim=None, title=None):
    losses = [i[0] for i in loss_list]

    plt.figure(figsize=(15, 10))
    plt.plot(losses, label='Eval loss')
    if ylim:
        plt.ylim(ylim)
    if title:
        plt.title(title)
    plt.legend()
    plt.grid('on')
    plt.show()


plotting_metrics(train_losses, title='Training Loss at each epoch')
