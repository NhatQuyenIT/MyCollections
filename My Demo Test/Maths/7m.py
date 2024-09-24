import numpy as np
import matplotlib.pyplot as plt

# Tính giá trị của f(x, y)
def f(x, y):
    return np.log((16 - x**2 - y**2) * (x**2 + y**2 - 4))

# Tạo lưới điểm
x = np.linspace(-5, 5, 400)
y = np.linspace(-5, 5, 400)
x, y = np.meshgrid(x, y)

# Áp dụng điều kiện giới hạn (16 - x^2 - y^2) * (x^2 + y^2 - 4) > 0
condition = (16 - x**2 - y**2) * (x**2 + y**2 - 4) > 0
x = np.ma.masked_where(~condition, x)
y = np.ma.masked_where(~condition, y)

# Vẽ miền xác định của hàm số
plt.figure(figsize=(8, 8))
plt.contourf(x, y, f(x, y), levels=50, cmap='viridis')
plt.colorbar(label='f(x, y)')
plt.title('Miền xác định của f(x, y)')
plt.xlabel('x')
plt.ylabel('y')
plt.show()