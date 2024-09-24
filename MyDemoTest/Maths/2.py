import numpy as np
import matplotlib.pyplot as plt

# Định nghĩa hàm để vẽ parabol y = x^2
def parabol(x):
    return x**2

# Tạo dải giá trị x
x_values = np.linspace(-2, 2, 400)

# Vẽ đồ thị của parabol
plt.plot(x_values, parabol(x_values), label='y = x^2')

# Vẽ dải giữa y = 1 và y = 2
plt.fill_between(x_values, 1, 2, color='gray', alpha=0.5, label='1 <= y <= 2')

# Đặt tiêu đề và chú thích
plt.title('Đồ thị của phần chung')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()

# Hiển thị đồ thị
plt.show()