# Day 3 - zip, built in fuctions, filtering

account_ids = ['ACC-001','ACC-02','ACC-03','ACC-04','ACC-05']
balances = [1_200_000,45_000_000,890_000,12_300_000,560_000]

for account_id,balance in zip(account_ids,balances):
    print(f' {account_id} |  {balance} USD')

total = sum(balances)
average = sum(balances)/ len(balances)
maximum = max(balances)
minimum = min(balances)

print(f' Total - {total}')
print(f' Average - {average} ')
print(f'  Maximum -{maximum}')
print(f'  Minimum - {minimum}')

above_threshold = [b for b in balances if b > 1_000_000]
print(above_threshold)
print ("Count:" ,len(above_threshold))