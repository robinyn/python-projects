ones=["", "one","two","three","four","five","six","seven","eight","nine"]
teens=["ten", "eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen"]
tens=["","ten","twenty","thirty","forty","fifty","sixty","seventy","eighty","ninety","hundred"]
sum=0

for hundreds_i in range(0,10):
    for tens_i in range(0, 10):
        for ones_i in range(0, 10):
            if hundreds_i>0:
                if ones_i==0 and tens_i==0:
                    sum+=len(ones[hundreds_i]+tens[10])
                    continue
                if tens_i==1:
                    sum+=len(ones[hundreds_i]+tens[10]+"and"+teens[ones_i])
                else:
                    sum+=len(ones[hundreds_i]+tens[10]+"and"+tens[tens_i]+ones[ones_i])
            else:
                if tens_i==1:
                    sum+=len(teens[ones_i])
                else:
                    sum+=len(tens[tens_i]+ones[ones_i])

sum+=len("onethousand")

print(sum)
