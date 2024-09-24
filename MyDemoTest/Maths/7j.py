import numpy as np
import matplotlib.pyplot as plt

# Hàm số f(x, y)
def f(x, y):
    return np.sqrt(y - x**2) / (1 - x**2)

# Tạo các giá trị x và y trong miền xác định
x = np.linspace(-2, 2, 400)
y = np.linspace(0, 4, 400)
x, y = np.meshgrid(x, y)

# Xác định miền xác định của f(x, y)
domain_mask = (1 - x**2 != 0) & (y - x**2 >= 0)

# Áp dụng giới hạn cho x và y
x = np.ma.masked_where(~domain_mask, x).filled(np.nan)
y = np.ma.masked_where(~domain_mask, y).filled(np.nan)

# Loại bỏ các giá trị không hợp lệ
x = np.nan_to_num(x)
y = np.nan_to_num(y)

# Vẽ miền xác định
plt.figure(figsize=(8, 6))
plt.title("Miền xác định của $f(x, y) = \\frac{\\sqrt{y - x^{2}}}{1 - x^{2}}$")
plt.xlabel("$x$")
plt.ylabel("$y$")
plt.pcolormesh(x, y, f(x, y), cmap='viridis', shading='auto')
plt.colorbar(label="$f(x, y)$")
plt.show()