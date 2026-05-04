def is_above_threshold(balance,threshold):
   """Return True if balance is above threshold, False otherwise"""
   return balance > threshold

THRESHOLD = 50_000_000

#testcases
test_balances =[120_00_000,75_00_00,50_00_0001,658_008_8754_845,123_048_84]

for balance in test_balances:
  result = is_above_threshold(balance,THRESHOLD)
  status = 'ABOVE'if result else 'BELOW'
  print (f" {balance} -- {status} (returned: {result})")

  ##Getting priority
def get_priority(amount):
     
    if amount >= 1_000_000_000:
       return "CRITICAL"
    elif amount >= 100_000_000:
       return "HIGH"
    elif amount >= 10_000_000:
       return "MEDIUM"
    else:
       return "LOW"
    
print()
print("=" * 50)
print("PART 2: Priority Classification")
print("=" * 50) 

test_amounts = [2_450_000_000,340_000_000,45_000_000,890_000]

for amount in test_amounts:
   priority = get_priority(amount)
   print(f' {amount}, {priority}')

##Account summary for 5 accounts
account =[
   {"id":"Acc-01", "Owner":"John Doe", "Balance":1_200_000},
   {"id":"Acc-02", "Owner": "Karan Johar", "Balance":45_000_000},
   {"id": "Acc-03", "Owner": "Priya Dixit", "Balance": 890_000},
   {"id": "Acc-04", "Owner": "Mayuri", "Balance": 123_000_000},
   {"id": "Acc-05", "Owner": "Neha", "Balance": 560_000}
]

for acc in account:
   priority = get_priority(acc["Balance"])
   print( f' ID: {acc["id"]}, {acc["Owner"]}, {acc["Balance"]},{priority}')