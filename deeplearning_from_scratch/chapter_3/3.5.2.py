import numpy as np

a = np.array([1010, 1000, 990])
print(np.exp(a) / np.sum(np.exp(a))) # 소프트맥스 함수의 계산 -> array([ nan, nan, nan])

c = np.max(a) # c = 1010 (최댓값)
a - c

print(np.exp(a - c) / np.sum(np.exp(a - c))) # [9.99954600e-01 4.53978686e-05 2.06106005e-09]


def softmax(a):
    c = np.max(a)
    exp_a = np.exp(a - c)
    sum_exp_a = np.sum(exp_a)
    y = exp_a / sum_exp_a
    return y