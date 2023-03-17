def currencycal(AmountINR,curr):
    if(curr=="Euro"):
        print(AmountINR*0.01417)
    elif(curr=="British Pound"):
        print(AmountINR*0.0100)
    elif(curr=="Australian Dollar"):
        print(AmountINR*0.02140)
    elif(curr=="Canadian Dollar"):
        print(AmountINR*0.02027)
    else:
        print(-1)

currencycal(300,"Euro")
currencycal(300,"British Pound")
currencycal(300,"Australian Dollar")
currencycal(300,"Canadian Dollar")
