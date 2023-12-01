"""
Credit card veryfier (using Luhn's algorithm, and card len check).
M_Sosnowski
"""

while True:
    card_number = str(input("Gimme ur card number: "))
    
    if len(card_number) != 16:
        print(f"U sure? Better try again!")
        break
    else:    
        odd_sum = 0
        even_sum = 0
        double_even = []
        number = list(card_number)
        
        for (idx, val) in enumerate(number):
            if idx % 2 != 0:
                odd_sum += int(val)
            else:
                double_even.append(int(val)*2)
        
        double_even_sum = []
        
        for x in double_even:
            if x < 10:
                double_even_sum.append(x)
            else:
                double_even_sum.append((int(str(x)[0]) + int(str(x)[1])))
        
        for x in double_even_sum:
            even_sum += x
        
        
        suum = odd_sum + even_sum
        
        # Lhun_algorithm_veryfier
        
        if suum % 10 == 0:
            print(f"Yay! that's a valid card number!")
        else:
            print(f"Oh bollocks, that ain't a valid card number, try again!")
