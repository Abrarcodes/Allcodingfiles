def mask_credit_card(card_number):
    card=str(card_number)
    return "*"*(len(card)-5) +(card[-5:])
print(mask_credit_card(123456789))