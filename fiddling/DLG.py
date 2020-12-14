import torch
from torch import nn

sample_num = 2
in_features = 8
model = nn.Sequential(
    nn.Linear(in_features=in_features, out_features=64, bias=False),
    nn.LeakyReLU(),
    nn.Linear(in_features=64, out_features=128),
    nn.LeakyReLU(),
    nn.Linear(in_features=128, out_features=64),
    nn.LeakyReLU(),
    nn.Linear(in_features=64, out_features=1)
)

loss_fun = torch.nn.MSELoss()

model.zero_grad()
x_true = torch.randn((sample_num, in_features))
y_true = torch.randn((sample_num, 1))
y_pred = model.forward(x_true)
loss_true = loss_fun(y_true, y_pred)
loss_true.backward()
gradient_true = [p.grad.clone().requires_grad_(False) for p in model.parameters()]

x_hat = torch.randn((sample_num, in_features), requires_grad=True)
y_hat = torch.randn((sample_num, 1), requires_grad=True)

optimizer = torch.optim.Adam([x_hat, y_hat], lr=0.01)

for _ in range(1000):
    model.zero_grad()
    optimizer.zero_grad()
    y_hat_pred = model.forward(x_hat)
    loss_hat = loss_fun(y_hat, y_hat_pred)
    loss_hat.backward(retain_graph=True, create_graph=True)
    optimizer.zero_grad()
    gradient_hat = [p.grad.clone().requires_grad_(True) for p in model.parameters()]

    gradient_delta_loss = sum(map(lambda x: loss_fun(x[0], x[1]), zip(gradient_true, gradient_hat)))
    gradient_delta_loss.backward(retain_graph=True, create_graph=True)
    print(f"gradient_delta_loss:{gradient_delta_loss}")
    # print(f"x_hat.grad:{x_hat.grad}")
    # print(f"y_hat.grad:{y_hat.grad}")
    print(f"loss_fun(x_hat,x_true):{loss_fun(x_hat, x_true)}")
    optimizer.step()

print(x_hat)
print(x_true)
print(y_hat)
print(y_true)
