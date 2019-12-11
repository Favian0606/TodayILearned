import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim

import torchvision
import torchvision.datasets as datasets
import torchvision.transforms as transforms

device = 'cuda' if torch.cuda.is_available() else 'cpu'

torch.manual_seed(777)
if device == 'cuda':
    torch.cuda.manual_seed_all(777)

# train data
transforms_train = transforms.Compose([
    transforms.ToTensor()
])


train_data = datasets.ImageFolder(root='custom_data/train_data', transform=transforms_train)

data_loader = torch.utils.data.DataLoader(dataset=train_data,
                                          batch_size=8,
                                          shuffle=True,
                                          num_workers=2)

# Model
class CNN(nn.Module):
    def __init__(self):
        super(CNN, self).__init__()
        self.layer1 = nn.Sequential(
            nn.Conv2d(3, 6, 5), # in_channel: 3(RGB), out_channel: 6, kernel_size: 5
            nn.ReLU(),
            nn.MaxPool2d(2)
        )
        self.layer2 = nn.Sequential(
            nn.Conv2d(6, 16, 5),
            nn.ReLU(),
            nn.MaxPool2d(2)
        )
        self.layer3 = nn.Sequential(
            nn.Linear(16*13*29, 120),
            nn.ReLU(),
            nn.Linear(120, 2)
        )

    def forward(self, x):
        out = self.layer1(x)
        # print(out.shape)
        out = self.layer2(out)
        # print(out.shape)
        out = out.view(out.shape[0], -1)
        # print(out.shape)
        out = self.layer3(out)
        return out

# test model
net = CNN().to(device)
test_input = (torch.Tensor(3,3,64,128).to(device))
test_out = net(test_input)

optimizer = optim.Adam(net.parameters(), lr=0.00001)
loss_func = nn.CrossEntropyLoss().to(device)

total_batch = len(data_loader)
training_epochs = 10

for epoch in range(training_epochs):
    avg_cost = 0.0
    for num, data in enumerate(data_loader):
        imgs, labels = data
        imgs = imgs.to(device)
        labels = labels.to(device)

        optimizer.zero_grad()
        out = net(imgs)
        loss = loss_func(out, labels)
        loss.backward()
        optimizer.step()

        avg_cost += loss / total_batch

    print('[Epoch:{}] cost = {}'.format((epoch+1), avg_cost))


print('Learning Finished.')

# save model
torch.save(net.state_dict(), 'model/model.pth')

new_net = CNN().to(device)
new_net.load_state_dict(torch.load('model/model.pth'))

print(net.layer1[0])
print(new_net.layer1[0])

print(net.layer1[0].weight[0][0][0])
print(new_net.layer1[0].weight[0][0][0])

# assert net.layer1[0].weight[0] == new_net.layer1[0].weight[0]

# test data
transforms_test = transforms.Compose([
    transforms.Resize((64,128)),
    transforms.ToTensor()
])

test_data = datasets.ImageFolder(root='custom_data/test_data', transform=transforms_test)
test_data_loader = torch.utils.data.DataLoader(dataset=test_data,
                                               batch_size=len(test_data))

with torch.no_grad():
    for num, data in enumerate(test_data_loader):
        imgs, label = data
        imgs = imgs.to(device)
        label = label.to(device)

        prediction = net(imgs)
        correct_prediction = torch.argmax(prediction, dim=1) == label
        accuracy = correct_prediction.float().mean()

        print('Accuracy: ', accuracy.item())