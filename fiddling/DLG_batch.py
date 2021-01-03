import torch
import torch.utils.data as Data
from torch import nn
BATCH_SIZE = 2  # 批大小为2
sample_num = 4  # 样本数为4
in_features = 8  # 特征数为8

# 定义模型
model = nn.Sequential(
    nn.Linear(in_features=in_features, out_features=64, bias=False),  # (8,64)
    nn.LeakyReLU(),
    nn.Linear(in_features=64, out_features=128),  # (64,128)
    nn.LeakyReLU(),
    nn.Linear(in_features=128, out_features=64),  # (128,64)
    nn.LeakyReLU(),
    nn.Linear(in_features=64, out_features=1))  # (64,1)

loss_fun = torch.nn.MSELoss()  # 损失函数最小化均方误差

model.zero_grad()
x_true = torch.randn((sample_num, in_features))  # (4,8)
y_true = torch.randn((sample_num, 1))  # (4,1)
torch_dataset = Data.TensorDataset(x_true, y_true)
loader = Data.DataLoader(dataset=torch_dataset,
                         batch_size=BATCH_SIZE,
                         shuffle=False)

# 训练网络 多次
for e in range(1000):
    for i, data in enumerate(loader):
        x_true_tmp, y_true_tmp = data
        y_pred = model.forward(x_true_tmp)
        loss_true = loss_fun(y_true_tmp, y_pred)
        loss_true.backward()  # 将所有影响loss的Variable都求了一次梯度
        # print(x_true_tmp, y_true_tmp)
# 网络梯度
gradient_true = [
    p.grad.clone().requires_grad_(False) for p in model.parameters()
]

# print(gradient_true)
# print(loader)
# 定义预估的参数
x_hat = torch.randn((sample_num, in_features), requires_grad=True)
y_hat = torch.randn((sample_num, 1), requires_grad=True)
torch_dataset_est = Data.TensorDataset(x_hat, y_hat)
loader_est = Data.DataLoader(dataset=torch_dataset_est,
                             batch_size=BATCH_SIZE,
                             shuffle=False)

optimizer = torch.optim.Adam([x_hat, y_hat], lr=0.01)

for i, data in enumerate(loader):
    print(data)
print("############")
for i, data in enumerate(loader_est):
    print(data)

for _ in range(200000):
    # 梯度清零
    model.zero_grad()
    optimizer.zero_grad()

    for i, data in enumerate(loader_est):
        x_hat, y_hat = data

        # 前向传播
        y_hat_pred = model.forward(x_hat)
        # 梯度回传
        loss_hat = loss_fun(y_hat_pred, y_hat)
        loss_hat.backward(retain_graph=True, create_graph=True)

    optimizer.zero_grad()
    gradient_hat = [
        p.grad.clone().requires_grad_(True) for p in model.parameters()
    ]

    # 对梯度中的每一项计算MSE
    gradient_delta_loss = sum(
        map(lambda x: loss_fun(x[0], x[1]), zip(gradient_true, gradient_hat)))
    # print(gradient_delta_loss)

    gradient_delta_loss.backward(retain_graph=True, create_graph=True)
    print(f"gradient_delta_loss:{gradient_delta_loss}")
    # print(f"x_hat.grad:{x_hat.grad}")
    # print(f"y_hat.grad:{y_hat.grad}")
    optimizer.step()

for i, data in enumerate(loader):
    print(data)
print("############")
for i, data in enumerate(loader_est):
    print(data)