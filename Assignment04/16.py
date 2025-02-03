def tribonacci_in_range(start, end):
    tribonacci = [1, 1, 2]
    while True:
        next_trib = tribonacci[-1] + tribonacci[-2] + tribonacci[-3]
        if next_trib > end:
            break
        tribonacci.append(next_trib)
    return [num for num in tribonacci if start <= num <= end]

start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))

result = tribonacci_in_range(start, end)
print(f"Tribonacci numbers in the range [{start}, {end}]: {result}")
