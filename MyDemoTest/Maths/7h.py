import numpy as np
import matplotlib.pyplot as plt

# Tạo dữ liệu cho đường tròn miền xác định
theta = np.linspace(0, 2*np.pi, 100)
r = 2  # Bán kính của đường tròn

# Tính toán tọa độ x, y của các điểm trên đường tròn
x_circle = r * np.cos(theta)
y_circle = r * np.sin(theta)

# Vẽ đường tròn miền xác định
plt.figure(figsize=(8, 8))
plt.plot(x_circle, y_circle, label=r'$x^2 + y^2 \neq 4$')

# Đặt các giá trị
x_values = np.linspace(-3, 3, 400)
y_values = np.linspace(-3, 3, 400)

# Tính toán giá trị của hàm số
X, Y = np.meshgrid(x_values, y_values)
Z = (3*X + 5*Y) / (X**2 + Y**2 - 4)

# Vẽ biểu đồ hàm số
plt.contour(X, Y, Z, levels=[-10, -5, 0, 5, 10], colors='r', linestyles='dashed', linewidths=1)
plt.colorbar(label=r'$f(x, y)$')

# Đặt các thông số đồ thị
plt.title('Miền xác định và Đồ thị của $f(x, y) = \\frac{3x + 5y}{x^2 + y^2 - 4}$')
plt.xlabel('x')
plt.ylabel('y')
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(color='gray', linestyle='--', linewidth=0.5)
plt.legend()
plt.axis('equal')

# Hiển thị đồ thị
plt.show()