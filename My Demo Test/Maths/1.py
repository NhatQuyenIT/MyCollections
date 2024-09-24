import matplotlib.pyplot as plt
import numpy as np

# Bước 1: Tạo mảng giá trị x từ -4 đến 4
x = np.linspace(-4, 4, 100)

# Bước 2: Tính giá trị y cho hàm y = x^2 và y = -x^2
y_positive = x**2
y_negative = -x**2

# Bước 3: Vẽ đồ thị
plt.plot(x, y_positive, label='y = x^2')
plt.plot(x, y_negative, label='y = -x^2')
plt.fill_between(x, y_positive, y_negative, where=(y_positive > y_negative), color='gray', alpha=0.3)

# Bước 4: Đặt các thông số và hiển thị đồ thị
plt.xlabel('x')
plt.ylabel('y')
plt.title('Graph of y = x^2 and y = -x^2')
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.grid(color = 'gray', linestyle = '--', linewidth = 0.5)
plt.legend()
plt.show()