"""
in the 'arithmetic_arranger' function, the parameter 'display_answers' is set to 'False' by default for a few reasons:

> default Behaviour :
> when a parameter has a default value, it means that if the user does  not provide a value for that parameter,it will automatically use the default. in this case, the default behavior is to arrange the arithmetic problems without showing the answers

This is useful because sometimes the user might just want to see the problems arranged neatly without the answers.
Optional Display of Answers:

The display_answers parameter is optional. If the user wants to see the answers, they can set display_answers to True when calling the function. This provides flexibility depending on the user's needs.
For example, a teacher might want to present problems to students without showing the answers initially. Later, the same teacher might want to display the problems along with the answers for verification.
"""
def arithmetic_arranger(problems, display_answers = False): 
    if len(problems) > 5:
        return 'Error: Too many problems'
    
    # step 2 : setting up lists for different parts of problems

    first_operands = []
    second_operands = []
    operators = []
    results = []

    # step 3 : splitting and validating each problem

    for problem in problems:
        parts = problem.split()

        if len(parts) != 3:
            return 'Error: Incorrect format.'
        
        """
        Breaking down this code : imagine you are a detective, and you have found a mysterious note with an arithmetic problem written on it '32 + 8'. Your job is to figure out what the first number is, what operation is being done, and what the second number is
        the ine of code 
        'first_operand, operator, second_operand = parts' 
        
        
        is like our detective's tool to crack the code
        
        for example
        
        '32 + 8'
        
        step 1: splitting the Note
        first, we use the 'split()' method to break the note into parts. this is like using scissors to cut the note into smaller pieces:
        
        parts = problem.split()
        
        Result 'parts becomes ['32', '+', '8']
        
        step 2: using our detective tool
        now, we use our special detective tool to take these pieces and put them into three different boxes:
        
        first_operand, operator, second_operand = parts
        """
        
        first_operand, operator, second_operand = parts
        
        if operator not in ['+','-']:
            return "Error: Operator must be '+' or '-'"
        
        if not first_operand.isdigit() or not second_operand.isdigit():
            return "Error: Numbers must only contain digits."
        
        if len(first_operand) > 4 or len(second_operand) > 4:
            return "Error: Numbers cannot be more than four digits."
        
        # summary : we split each problem into three parts: the first number, the operator, and the second number. if there are not exactly three parts, or if the operator isn't + or -, or if the numbers aren't digit, or if the numbers are too long, we get an error
        
        # step 4 : calculating the result
        
        if operator == '+':
            result = str(int(first_operand) + int(second_operand))
        else:
            result = str(int(first_operand) - int(second_operand))
            
        # why leave final results in string?
        """
        when we display problems and their answers, we need everything to be in a nice readable format. strings help us with that!
        when we use strings, we can align the numbers properly, just like arranging books neatly on a shelf
        """
        
        
        # step 5: storing the parts
        
        first_operands.append(first_operand)
        second_operands.append(second_operand)
        operators.append(operator)
        results.append(results)
        
        # step 6 : arranging the problems
        
        arranged_problems = ''
        line1 = ''
        line2 = ''
        line3 = ''
        line4 = ''
        
        # looping through problems
        for i in range(len(problems)):
        # we find the length of the longest  number in the problem and add 2 more spaces. this helps us m ake sure there's enough space for the operator and extra space to make things look nice
            length = max(len(first_operands[i]), len(second_operands[i])) + 2
            # we take the first number and use 'rjust(length)' to make sure it's right-aligned. this means we add spaces to the left if the number is shorter than the length
            # adding the operator and second number
            line2 += operators[i] + second_operands[i].rjust(length - 1)
            
            # adding the dashes
            line3 += '-' * length
            
            # adding the result
            line4 += results[i].rjust(length)
            
            # adding spaces between problems
            if i < len(problems) - 1:
                line1 += ' ' * 4
                line2 += ' ' * 4
                line3 += ' ' * 4
                line4 += ' ' * 4
                
                
            # combining the lines
            
            if display_answers:
                arranged_problems = line1 + '\n' + line2 + '\n' + line3 + '\n' + line4
            else:
                arranged_problems = line1 + '\n' + line2 + '\n' + line3
                
            return arranged_problems
        
#print(arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True))
print(f'\n{arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])}')

        
        