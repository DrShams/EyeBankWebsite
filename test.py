import sys
import os

# ДОБАВЛЯЕМ ПУТЬ К ПАПКЕ, а не к файлу
sys.path.append(r'D:\GitHub\Locust\libs')
sys.path.append('/home/your_username/GitHub/Locust/libs')

# Теперь можно импортировать
from csv_reader import CSVDataReader

# Использование
reader = CSVDataReader('data.csv')
data = reader.load_data()