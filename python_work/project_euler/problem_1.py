# Multiples of 3 and 5
def problem_1(input):
    result = sum([i for i in range(1,input) if i % 3 == 0 or i % 5 == 0 ])
    return result


# Even Fibonacci numbers
def problem_2(input):
    fibonacci_list = [1, 2]
    while True:
        start = fibonacci_list[-1]
        end = fibonacci_list[-2]
        fibonacci_list.append(start + end)
        if fibonacci_list[-1] + fibonacci_list[-2] > input:
            break
    result = sum([i for i in fibonacci_list if i % 2 == 0])

    return result


def is_prime(input_int):
    if input_int < 2:
        return False
    if input_int ==2:
        return True
    if n



        elif
if __name__ == "__main__":
    print("Answer of the first question is:", problem_1(1000))
    print("Answer of the 2ed question is:"problem_2(4000000))
    %time
