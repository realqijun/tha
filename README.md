# hello/

Run `python hello.py`.
Program should output `Hello, World!` to the terminal.

# s_even/

Add code to the bottom of the file `is_even.py` such as `print(is_even(12))`. Save and run `python is_even.py`. Output should show `True`.

Rationale: use modulus operator to check the remainder of the number after dividing by 2, if the remainder is 0, then the number is even

# greaterOfTwo/

Add code to the bottom of the file `greater_of_two.py` such as `print(greater_of_two(12, 123))`. Save and run `python greater_of_two.py`. Output should be 123 in this case.
Rationale: use formula

# count_digit/

Add code to the bottom of the file `count_digit.py` such as `print(count_digit(1234333))`. Save and run `python count_digit.py`. Should output `4`.

Rationale: floor divide the number by 10 until it reaches 0. At every iteration, check the ones digit of the number to see if it's 3.

# string_rev/

Add code to the bottom of the file `string_rev.py` such as `print(string_rev('hello'))`. Save and run `python string_rev.py`. Output would be `olleh`

Rationale: iterate on the input string from the back, then append the charcters to the return string.

# getSecondLargest/

Add code to the bottom of the file `getSecondLargest.py` such as `print(getSecondLargest([2, 3, 4, 2, 3]))`. Save and run `python getSecondLargest.py`

Rationale: find the largest element first, then find another largest element that is not the largest element. To differentitate if the 2nd largest and the largest if they are equal, check their indexes in the array.

# fizzbuzz/

Run `python fizzbuzz.py`

Rationale: the number being divisble by both 3 and 5 is the more specific case, so it is captured the earliest in the if statement. Then check if they are divisible by 3 only or divisible by 5 only, if so then print `Fizz` or `Buzz` respectively. Else print the number.

# div_mod/

Add code to the bottom of the file `divmod.py` such as `print(divmod(10, 3))`. Save and run `python divmod.py`. Output is in the form of a tuple `(a, b)` where `a` is the result of `x // y` and `b` is the result of `x % y`.

Rationale: use a helper function to count the `n` in `x - n * y`, when `x - n * y` is negative, then `n - 1` is the result of `x // y` and `x - (n - 1) * y` is the value of `x % y`.

# firstUniqChar/

Add code to the bottom of the file `first_uniq_char.py` such as `print(first_uniq_char('hello'))`. Save and run `python first_uniq_char.py`. Output would be `h`.

Rationale: store the count of each character in the string in a dictionary. Then iterate over the string to find the first character that has a count of 1.

# simple_stack/

Add code to the bottom of the file `simple_stack.py` such as `simple_stack('PUSH', 12)`. Save and run `python simple_stack.py`.

Rationale: store a global array as the stack. Then, use indexing to manipulate it like a stack.