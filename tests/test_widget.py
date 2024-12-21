from src.widget import mask_account_card

print(mask_account_card('Счет 73654108430135874305'))  # Ожидается: "Счет **4305"
print(mask_account_card('Visa Platinum 7000792289606361'))  # Ожидается: "Visa Platinum 7000 79** **** 6361"
print(mask_account_card('Maestro 7000792289606361'))  # Ожидается: "Maestro 7000 79** **** 6361"