from src.widget import mask_account_card, get_date


print(mask_account_card('Счет 12345678901234567890')) # должны увидеть: Счет **7890
print(mask_account_card('Visa Super Puper 1234567890123456')) # Visa Super Puper 1234 56** **** 3456
print(get_date('2024-12-18T01:28:30.012345')) # 18.12.2024