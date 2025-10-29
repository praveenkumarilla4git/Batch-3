#======================
#While loop
#======================

#!/bin/bash
read -p "Enter a number: " n
sum=0
i=1

while [ $i -le $n ]

do
        sum=$((sum + i))
        ((i++))
done

echo "Sum of first $n numbers is: $sum"