import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Định nghĩa hàm f(x, y)
def f(x, y):
    return -(np.arcsin(1 - y) / x)

# Tạo dữ liệu cho trục x và y
x = np.linspace(0.001, 2, 100)  # Tránh chia cho 0
y = np.linspace(0, 2, 100)
x, y = np.meshgrid(x, y)

# Tính giá trị của hàm f(x, y)
z = f(x, y)

# Vẽ đồ thị 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(x, y, z, cmap='viridis')

# Đặt tên cho các trục
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('f(x, y)')

# Hiển thị đồ thị
plt.show()