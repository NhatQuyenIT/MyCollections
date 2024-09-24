import numpy as np
import matplotlib.pyplot as plt

# Tạo dữ liệu
x = np.linspace(-5, 5, 400)
y = np.linspace(-5, 5, 400)
X, Y = np.meshgrid(x, y)
Z = np.log(X * Y)

# Vẽ đồ thị hàm số
plt.contourf(X, Y, Z, levels=50, cmap='viridis')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Miền xác định của $f(x, y) = \ln(xy)$')
plt.colorbar(label='$\ln(xy)$')

# Hiển thị đồ thị
plt.show()