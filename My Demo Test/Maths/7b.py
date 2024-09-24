import numpy as np
import matplotlib.pyplot as plt

# Tạo các giá trị x, y trong miền cho trục x và y
x_values = np.linspace(-5, 5, 100)
y_values = np.linspace(-5, 5, 100)

# Tạo lưới các điểm (x, y)
x, y = np.meshgrid(x_values, y_values)

# Tính giá trị của hàm số f(x, y)
f_values = x / (x**2 + y**2)

# Vẽ đồ thị 3D của hàm số
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(x, y, f_values, cmap='viridis')

# Đặt tên cho các trục
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('f(x, y)')

# Hiển thị đồ thị
plt.show()