"""
1169. Invalid Transactions
A transaction is possibly invalid if:

the amount exceeds $1000, or;
if it occurs within (and including) 60 minutes of another transaction with the same name in a different city.
You are given an array of strings transaction where transactions[i]
consists of comma-separated values representing the name, time (in minutes), amount, and city of the transaction.

Return a list of transactions that are possibly invalid. You may return the answer in any order.
"""
from collections import defaultdict


def invalid_transactions(self, transactions):
    invalid = []
    transaction_time = defaultdict(dict)
    for transaction in transactions:
        name, str_time, amount, city = transaction.split(",")
        time = int(str_time)

        if name not in transaction_time[time]:
            transaction_time[time][name] = {city, }
        else:
            transaction_time[time][name].add(city)

    for transaction in transactions:
        name, str_time, amount, city = transaction.split(",")
        time = int(str_time)
        if int(amount) > 1000:
            invalid.append(transaction)
            continue

        for inv_time in range(time - 60, time + 61):
            if inv_time not in transaction_time:
                continue
            if name not in transaction_time[inv_time]:
                continue

            trans_by_name_at_time = transaction_time[inv_time][name]

            if city not in trans_by_name_at_time or len(trans_by_name_at_time) > 1:
                invalid.append(transaction)
                break

    return invalid
