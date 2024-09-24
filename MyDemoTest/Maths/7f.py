import numpy as np
import matplotlib.pyplot as plt

# Tạo dữ liệu
x = np.linspace(-10, 10, 400)
y = np.linspace(-10, 10, 400)

# Tạo lưới giá trị x, y
X, Y = np.meshgrid(x, y)

# Xác định miền xác định
domain_mask = X + Y >= 0

# Vẽ đồ thị
plt.contourf(X, Y, domain_mask, cmap='viridis', levels=[0, 1], alpha=0.5)
plt.title('Miền xác định của $f(x, y) = \sqrt{x+y}$')
plt.xlabel('x')
plt.ylabel('y')
plt.colorbar(label='Miền xác định (1: True, 0: False)')
plt.show()