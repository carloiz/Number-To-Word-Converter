ONES = ["","One","Two","Three","Four","Five","Six","Seven","Eight","Nine"]
TEENS = ["Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
TENS = ["","", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]

while True:
    try:
        Number = input("\nEnter Number: ")

        Number = int(Number)

        if Number<10:
            if str(ONES[Number]) == "":
                print("Zero")
            else:
                print(ONES[Number])
        elif Number<20:
            print(TEENS[Number - 10])
        elif Number<=99:
            Number = str(Number)
            print(TENS[int(Number[-2])] + " " + ONES[int(Number[-1])])
        elif Number<=999:
            Number = str(Number)
            if Number[-2] == "1":
                print(ONES[int(Number[-3])] + " Hundred " + TEENS[int(Number) - int(str(Number[-3]) + "10")])
            elif Number[-2] == "0":
                print(ONES[int(Number[-3])] + " Hundred " + ONES[int(Number) - int(str(Number[-3]) + "00")])
            else:
                print(ONES[int(Number[-3])] + " Hundred " + TENS[int(Number[-2])] + " " + ONES[int(Number[-1])])
        elif Number<=9999:
            Number = str(Number)

            if int(Number)%1000==0:
                print(ONES[int(Number[-4])] + " Thousand")
            elif int(Number)%100==0:
                print(ONES[int(Number[-4])] + " Thousand " + ONES[int(Number[-3])] + " Hundred")
            else:
                if Number[-2] == "1":
                    print(ONES[int(Number[-4])] + " Thousand " + ONES[int(Number[-3])] + " Hundred " + TEENS[int(Number) - int(str(Number[-4]) + str(Number[-3]) + "10")]) if int(Number[-3]) != 0 else print(ONES[int(Number[-4])] + " Thousand " + TEENS[int(Number) - int(str(Number[-4]) + "010")]) 
                elif Number[-2] == "0":
                    print(ONES[int(Number[-4])] + " Thousand " + ONES[int(Number[-3])] + " Hundred " + ONES[int(Number) - int(str(Number[-4]) + str(Number[-3]) + "00")]) if int(Number[-3]) != 0 else print(ONES[int(Number[-4])] + " Thousand " + ONES[int(Number) - int(str(Number[-4]) + "000")]) 
                else:
                    print(ONES[int(Number[-4])] + " Thousand " + ONES[int(Number[-3])] + " Hundred " + TENS[int(Number[-2])] + " " + ONES[int(Number[-1])]) if int(Number[-3]) != 0 else print(ONES[int(Number[-4])] + " Thousand " + TENS[int(Number[-2])] + " " + ONES[int(Number[-1])])
        else:
            print("The maximum number Right now is \'9999\'")
    except ValueError as e:
        break

    
