class MLP:
    def __init__(self,n):
        self.fc1 = nn.Linear(784, 512)
        self.fc2 = nn.Linear(512, 256)
        self.fc3 = nn.Linear(256, 128)
        self.fc4 = nn.Linear(128, 10)
    def forward(self, x):
        x = Relu(self.fc1(x))
        x = Relu(self.fc2(x))
        x = Relu(self.fc3(x))
        x = self.fc4(x)
        return x