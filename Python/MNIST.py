import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
import torchvision
from torchvision import datasets, transforms


class Net():
    def __init__(self):
        self.l1 = nn.Linear(784, 256)
        self.l2 = nn.Linear(256, 128)
        self.l3 = nn.Linear(128, 10)
        self.sm = nn.LogSoftmax(dim = 1)
    def forward(self, x):
        x = self.sm(self.l3(self.l2(F.relu(self.l1(x)))))
        return x

def main():
    train = datasets.MNIST('', train=True, download=True, transform=transforms.Compose([transforms.ToTensor()]))
    test = datasets.MNIST('', train=False, download=True, transform=transforms.Compose([transforms.ToTensor()]))
    trainset = torch.utils.data.DataLoader(train, batch_size=10, shuffle=True)
    testset = torch.utils.data.DataLoader(test, batch_size=10, shuffle=False)
    if torch.cuda.is_available():
        device = torch.device("cuda:0")
        print("Running on the GPU")
    else:
        device = torch.device("cpu")
        print("Running on the CPU")
    net = Net()
    loss_function = nn.NLLLoss(reduction='none')
    optim = torch.optim.SGD(net.parameters(), lr=0.001, momentum=0)
    BS = 128
    losses, accuracies = [], []
    for i in (t := trange(1000)):
        samp = np.random.randint(0, X_train.shape[0], size=(BS))
        X = torch.tensor(X_train[samp].reshape((-1, 28*28))).float()
        Y = torch.tensor(Y_train[samp]).long()
        model.zero_grad()
        out = model(X)
        cat = torch.argmax(out, dim=1)
        accuracy = (cat == Y).float().mean()
        loss = loss_function(out, Y)
        loss = loss.mean()
        loss.backward()
        optim.step()
        loss, accuracy = loss.item(), accuracy.item()
        losses.append(loss)
        accuracies.append(accuracy)
        t.set_description("loss %.2f accuracy %.2f" % (loss, accuracy))
if __name__ == "__main__":
    main()