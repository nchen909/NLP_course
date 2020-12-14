#encoding=utf-8
import torch
tensor1=torch.FloatTensor([[1,2],[3,4]])
tensor2=torch.FloatTensor([[5,6],[7,8]])

print(tensor1.reshape((4,1)))
print(tensor1*tensor2)#叉积
import tsensor
with tsensor.clarify():
    #print(tensor1@tensor2@torch.FloatTensor([1]))
    print(tensor1 @ tensor2)#叉积

X = tensor1.view(-1).dot(tensor2.view(-1))  # 叉积和
print(X)
#print(torch.dot(tensor1,tensor2))
#dot只能用于向量
print(tensor1.t()@tensor1@tensor2.t()@tensor2-tensor2.t()@tensor1@tensor1.t()@tensor2)#点积

#print(torch.mm(tensor1.t()))