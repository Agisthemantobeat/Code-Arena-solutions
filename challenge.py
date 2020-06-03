# Jon Snow visits Dragonstone to meet Daenerys Targaryen. He asks for aid in defeating the White Walkers and Army of Dead. But Daenerys refuses to believe that white walkers are real. She puts a condition before Jon that if he solves the challenge given by her then she will send her army to fight White Walkers. She gives certain inputs and outputs , Jon needs to find the logic and predict the output for the corresponding inputs. Jon Snow is struggling with the challenge as he knows nothing!! Help Jon to find the logic and win this challenge.
#
# INPUT : Input contains integers separated by a newline
'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Jon Snow visits Dragonstone to meet Daenerys Targaryen. He asks for aid in defeating the White Walkers and Army of Dead. But Daenerys refuses to believe that white walkers are real. She puts a condition before Jon that if he solves the challenge given by her then she will send her army to fight White Walkers. She gives certain inputs and outputs , Jon needs to find the logic and predict the output for the corresponding inputs. Jon Snow is struggling with the challenge as he knows nothing!! Help Jon to find the logic and win this challenge.
#
# INPUT : Input contains integers separated by a newline
'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''


# Write your code here
def moveZeros(arr):
    # first expression returns a list of
    # all non zero elements in arr in the
    # same order they were inserted into arr
    # second expression returns a list of
    # zeros present in arr
    return [nonZero for nonZero in arr if nonZero != 0] + \
           [Zero for Zero in arr if Zero == 0]


# Driver function
h = []
i = 0
while h[i] != ' ' and i < len(h) - 2 and h[i + 1] != ' ':
    L = []
    a = input()
    h.append(a)
    i = i + 1
    if (i == len(h) - 2):
        break
    for var in h:
        while (var > 0):
            L.append('var%2')
            var = var / 2
        X = moveZeros(L)
        print(X)
        continue
