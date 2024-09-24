import numpy as np
import matplotlib.pyplot as plt

# Tạo dải giá trị theta từ 0 đến pi (nửa đường tròn)
theta = np.linspace(0, np.pi, 1000)

# Tính các tọa độ x, y của điểm trên nửa đường tròn
x = np.cos(theta)
y = np.sin(theta)

# Vẽ đồ thị của nửa đường tròn
plt.plot(x, y, label=r'$x^2 + y^2 = 1, x \geq 0$')

# Đặt tiêu đề và chú thích
plt.title('Đồ thị của nửa đường tròn')
plt.xlabel('x')
plt.ylabel('y')
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.grid(color = 'gray', linestyle = '--', linewidth = 0.5)
plt.legend()

# Hiển thị đồ thị
plt.show()