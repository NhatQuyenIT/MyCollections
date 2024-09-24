import numpy as np
import matplotlib.pyplot as plt

# Tạo dải giá trị x từ -1 đến 1
x = np.linspace(-1, 1, 1000)

# Tính các giá trị y tương ứng theo hàm số y = x^2
y_quadratic = x**2

# Tính các giá trị y tương ứng theo hàm số y = sqrt(1 - x^2) để vẽ đường tròn
y_circle = np.sqrt(1 - x**2)

# Vẽ đồ thị của hàm số y = x^2
plt.plot(x, y_quadratic, label=r'$y = x^2$')

# Vẽ đồ thị của đường tròn x^2 + y^2 = 1
plt.plot(x, y_circle, label=r'$x^2 + y^2 \leq 1$')

# Đặt tiêu đề và chú thích
plt.title('Đồ thị của $x^2 + y^2 \leq 1$ và $y = x^2$')
plt.xlabel('x')
plt.ylabel('y')
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.fill_between(x, y_quadratic, where=(y_circle >= y_quadratic), interpolate=True, color='gray', alpha=0.3)
plt.grid(color='gray', linestyle='--', linewidth=0.5)
plt.legend()

# Hiển thị đồ thị
plt.show()