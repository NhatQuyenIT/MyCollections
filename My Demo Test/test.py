import numpy as np
import matplotlib.pyplot as plt

# Hàm số cần tối ưu
def f(x, y):
    return x**2 + y**2

# Miền ràng buộc
def g(x, y):
    return (x - np.sqrt(2))**2 + (y - np.sqrt(2))**2 - 9

# Tạo lưới điểm trên miền ràng buộc
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(x, y)

# Tính giá trị của hàm số trên miền ràng buộc
Z = f(X, Y)

# Tìm giá trị nhỏ nhất và lớn nhất
min_val = np.min(Z[g(X, Y) <= 0])
max_val = np.max(Z[g(X, Y) <= 0])

print("Giá trị nhỏ nhất của hàm số:", min_val)
print("Giá trị lớn nhất của hàm số:", max_val)

# Vẽ miền ràng buộc
plt.figure(figsize=(8, 8))
plt.contour(X, Y, g(X, Y), [0], colors='r')
plt.scatter(np.sqrt(2), np.sqrt(2), color='r', s=50)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Miền ràng buộc')
plt.show()