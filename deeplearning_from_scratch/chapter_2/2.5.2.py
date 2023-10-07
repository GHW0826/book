import numpy as np

def NAND(x1, x2):
    x = np.array([x1, x2])      # 입력
    w = np.array([-0.5, -0.5])  # 가중치. AND와는 가중치(w와 b)만 다르다.
    b = 0.7
    tmp = np.sum(w*x) + b
    if tmp <= 0:
	    return 0
    else:
	    return 1

def OR(x1, x2):
    x = np.array([x1, x2])    # 입력
    w = np.array([0.5, 0.5])  # 가중치. AND와는 가중치(w와 b)만 다르다.
    b = -0.2
    tmp = np.sum(w * x) + b
    if tmp <= 0:
        return 0
    else:
        return 1

def AND(x1, x2):
    x = np.array([x1, x2])    # 입력
    w = np.array([0.5, 0.5])  # 가중치. AND와는 가중치(w와 b)만 다르다.
    b = -0.7
    tmp = np.sum(w * x) + b
    if tmp <= 0:
        return 0
    else:
        return 1

def XOR(x1, x2):
	s1 = NAND(x1, x2)
	s2 = OR(x1, x2)
	y = AND(s1, s2)
	return y

print(XOR(0, 0)) # 0을 출력
print(XOR(1, 0)) # 1을 출력
print(XOR(0, 1)) # 1을 출력
print(XOR(1, 1)) # 0을 출력