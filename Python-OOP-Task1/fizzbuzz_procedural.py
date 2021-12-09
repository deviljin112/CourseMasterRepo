def main():
    number_list = [i for i in range(101) if i != 0]
    divisible_nums = {}

    print("How many numbers would you like?")
    count = input("=> ")

    if count.isdigit():
        count = int(count)
        i = 0

        while i < count:
            print("Choose a number and word.\nExample: 3 Fizz.")
            try:
                num, word = input("=> ").split(" ")
            except:
                print("Invalid format!\nFormat: NUM WORD.")
            else:
                if num.isdigit():
                    i += 1
                    divisible_nums[int(num)] = word
                else:
                    print("This is not a valid number!\nTry again.")

        output = [str(i) for i in range(101) if i != 0]
        for x in divisible_nums.keys():
            for y in number_list:
                if y % x == 0:
                    if output[y - 1].isdigit():
                        output[y - 1] = divisible_nums[x]
                    else:
                        output[y - 1] += divisible_nums[x]

        print(output)

    else:
        print("That is not a valid integer number")


if __name__ == "__main__":
    print("-=FizzBuzz=-")
    main()