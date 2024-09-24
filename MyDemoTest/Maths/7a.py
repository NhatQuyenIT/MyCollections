import numpy as np
import matplotlib.pyplot as plt

# Tạo dải giá trị x và y
x = np.linspace(-5, 5, 400)
y = np.linspace(-5, 5, 400)

# Tạo lưới từ các giá trị x và y
x, y = np.meshgrid(x, y)

# Tìm miền xác định của hàm số
domain_mask = (x - y) != 0

# Tô màu miền xác định trên đồ thị
plt.imshow(domain_mask, extent=(-5, 5, -5, 5), origin='lower', cmap='gray', alpha=0.3)

# Đặt tiêu đề và chú thích
plt.title('Miền xác định của $f(x, y) = \\frac{x+y}{x-y}$')
plt.xlabel('x')
plt.ylabel('y')
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(color='gray', linestyle='--', linewidth=0.5)

# Hiển thị đồ thị
plt.show()