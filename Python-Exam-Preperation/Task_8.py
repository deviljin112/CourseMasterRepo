# create a dictionary
# shopping items with prices

some_dict = {
    "apple": 1.99,
    "banana": 0.75,
    "eggs": 1.25,
    "bread": 1.0,
}

print(some_dict)

## IN A FOR LOOP

answer = 0
for v in some_dict.values():
    answer += v

print(answer)

## ALTERNATIVE

print(sum(some_dict))

## IN A FUNCTION


def added_dict(arg):
    return sum(arg.values())


print(added_dict(some_dict))

## ADDING NEW VALUE

some_dict["kiwi"] = 2.99

print(some_dict)