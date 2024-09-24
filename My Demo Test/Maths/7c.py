import numpy as np
import matplotlib.pyplot as plt

# Tạo các giá trị theta từ 0 đến 2*pi
theta = np.linspace(0, 2*np.pi, 100)

# Xác định trục dài và trục ngắn của ellipse
a = 3/2  # trục dài
b = 2    # trục ngắn

# Tính các điểm trên ellipse
x = a * np.cos(theta)
y = b * np.sin(theta)

# Vẽ ellipse
plt.plot(x, y, label=r'$\frac{x^2}{(\frac{3}{2})^2} + \frac{y^2}{2^2} \leq 1$')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Domain of $f(x, y) = \sqrt{4x^2 + 9y^2 - 36}$')
plt.legend()
plt.grid(True)
plt.show()