import vnstock3 as vnstock
import vnstock as vs
import pandas as pd
import matplotlib.pyplot as plt

stock_code = 'VNM'

start_date = '2024-09-01'
end_date = '2024-09-20'

data = vs.stock_historical_data(stock_code, start_date, end_date)

df = pd.DataFrame(data)

df['time'] = pd.to_datetime(df['time'])

plt.figure(figsize=(10, 6))
plt.plot(df['time'], df['close'], marker='o', color='b', linestyle='-', label='Giá đóng cửa')


plt.title(f'Giá đóng cửa cổ phiếu {stock_code} theo thời gian')
plt.xlabel('Ngày')
plt.ylabel('Giá đóng cửa (VND)')

# Thêm chú thích
plt.legend()

# Hiển thị biểu đồ
plt.grid(True)
plt.xticks(rotation=45)  # Xoay nhãn trục x để dễ nhìn hơn
plt.tight_layout()       # Đảm bảo bố cục gọn gàng
plt.show()


#df.to_csv('stock_price_data.csv', index=False, encoding='utf-8')

