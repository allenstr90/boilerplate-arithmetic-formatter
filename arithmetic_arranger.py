import re


def arithmetic_arranger(problems, display_result=False):
    if len(problems) > 5:
        return 'Error: Too many problems.'
    line1 = line2 = line3 = line4 = ''
    length = len(problems)
    for operation in problems:
        splits = operation.split()
        num1 = splits[0]
        arith_op = splits[1]
        num2 = splits[2]
        if arith_op != '+' and arith_op != '-':
            return 'Error: Operator must be \'+\' or \'-\'.'
        if re.match('^\\d+$', num1) is None or re.match('^\\d+$', num2) is None:
            return 'Error: Numbers must only contain digits.'
        if len(num1) > 4 or len(num2) > 4:
            return 'Error: Numbers cannot be more than four digits.'
        length = length - 1
        spaces = max(len(num1), len(num2)) + 2
        separator = ('    ' if length > 0 else '')
        line1 += num1.rjust(spaces) + separator
        line2 += arith_op + ' ' + num2.rjust(spaces - 2) + separator
        line3 += ''.rjust(spaces, '-') + separator
        if display_result:
            operand1 = int(num1)
            operand2 = int(num2)
            result = operand1 + operand2 if arith_op == '+' else operand1 - operand2
            line4 += str(result).rjust(spaces) + separator
    return line1 + '\n' + line2 + '\n' + line3 + ('\n' + line4 if display_result else '')
