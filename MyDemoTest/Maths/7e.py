import numpy as np
import matplotlib.pyplot as plt

# Định nghĩa hàm số
def f(x, y):
    return np.log(y) / (2 * x**2 - 1)

# Tạo lưới điểm trong miền xác định
x = np.linspace(-2, 2, 400)
y = np.linspace(0.01, 5, 400)
x, y = np.meshgrid(x, y)

# Áp dụng điều kiện miền xác định
valid_points = (2 * x**2 - 1 != 0) & (y > 0)

# Vẽ miền xác định
plt.imshow(valid_points, extent=(-2, 2, 0.01, 5), origin='lower', cmap='viridis', alpha=0.3)
plt.title('Miền xác định của $f(x, y)$')
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.show()