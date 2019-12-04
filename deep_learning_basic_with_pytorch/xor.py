import torch

# https://stackoverflow.com/questions/48152674/how-to-check-if-pytorch-is-using-the-gpu
# torch.cuda.is_available() returns boolean value
# torch.cuda.current_device(); 0
# torch.cuda.device_count(); 1
# torch.cuda.get_device_name(0)
device = 'cuda' if torch.cuda.is_available() else 'cpu'

# for reproducibility
torch.manual_seed(777)
if device == 'cuda':
    torch.cuda.manual_seed_all(777)

# https://stackoverflow.com/questions/53331247/pytorch-0-4-0-there-are-three-ways-to-create-tensors-on-cuda-device-is-there-s
X = torch.FloatTensor([[0, 0], [0, 1], [1, 0], [1, 1]]).to(device)
Y = torch.FloatTensor([[0], [1], [1], [0]]).to(device)

# nn layers
# https://pytorch.org/docs/stable/_modules/torch/nn/modules/linear.html
# Applies a linear transformation to the incoming data: y = xA^T + b
# single layer for xor operation (perceptron)
# https://nl.wikipedia.org/wiki/Perceptron#/media/Bestand:Rosenblattperceptron.png
linear = torch.nn.Linear(2, 1, bias=True)# in_features, out_features
sigmoid = torch.nn.Sigmoid()

# model
model = torch.nn.Sequential(linear, sigmoid).to(device)

# cost & optimizer
criterion = torch.nn.BCELoss().to(device)
optimizer = torch.optim.SGD(model.parameters(), lr=1)

for step in range(10001):
    optimizer.zero_grad()
    hypothesis = model(X)

    cost = criterion(hypothesis, Y)
    cost.backward()
    optimizer.step()

    if step % 100 == 0:
        print(step, cost.item())

# Accuracy
# True if hypothesis > 0.5 else False
with torch.no_grad():
    hypothesis = model(X)
    predicted = (hypothesis > 0.5).float()
    accuracy = (predicted == Y).float().mean()
    print('\nHypothesis: ', hypothesis.detach().cpu().numpy(), '\nCorrect: ', predicted.detach().cpu().numpy(),
          '\nAccuracy: ', accuracy.item())
