# Day 1 - Nostro Account Balance Statement

# Variables
account_id = 'ACC-00492'
balance = 2_450_000.75
currency = 'USD'
is_flagged = False

# Print each variable
print(account_id)
print(balance)
print(currency)
print(is_flagged)

# f-string formatting
print(f'Account {account_id} holds {currency} {balance:,.2f}')

# Arithmetic - nostro balance movement
opening_balance = 5_000_000

credits = 320_000 + 1_200_000
debits = 870_500 + 450_000

closing_balance = opening_balance + credits - debits

print(f'Opening Balance : {currency} {opening_balance:,.2f}')
print(f'Total Credits   : {currency} {credits:,.2f}')
print(f'Total Debits    : {currency} {debits:,.2f}')
print(f'Closing Balance : {currency} {closing_balance:,.2f}')

# Surplus or deficit check
if closing_balance > opening_balance:
    print('Status: Surplus')
else:
    print('Status: Deficit')