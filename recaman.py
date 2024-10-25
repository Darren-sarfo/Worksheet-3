def recaman_sequence(n):
    original_num=[0]

    for i in range(1,n):
        num_next=original_num[i-1 ]- i

        if num_next in original_num or 0>num_next:
            num_next=original_num[i-1]+i

        original_num.append(num_next)

    return original_num

counter=int(input("Please enter how many numbers the sequence will contain: "))
print(recaman_sequence(counter))
