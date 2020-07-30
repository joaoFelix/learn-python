price = 10 ** 6  # 1M
down_payment_percent = 0.2  # defaults to 20%

buyer_has_good_credit = False

if buyer_has_good_credit:
    down_payment_percent = 0.1

print(f'Down payment = {price * down_payment_percent}')

