import numpy as np
import matplotlib.pyplot as plt

# Đặt các giá trị
theta = np.linspace(0, 2*np.pi, 100)
r = 1  # bán kính của hình tròn

# Tính toán các tọa độ x, y của điểm trên hình tròn
x = r * np.cos(theta)
y = r * np.sin(theta)

# Vẽ hình tròn
plt.figure(figsize=(8, 8))
plt.plot(x, y, label=r'$1 - \frac{x^2}{9} - y^2 > 0$')

# Đặt các thông số đồ thị
plt.title('Miền xác định của $f(x, y) = \ln(9 - x^2 - 9y^2)$')
plt.xlabel('x')
plt.ylabel('y')
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.grid(color = 'gray', linestyle = '--', linewidth = 0.5)
plt.legend()
plt.axis('equal')

# Hiển thị đồ thị
plt.show()