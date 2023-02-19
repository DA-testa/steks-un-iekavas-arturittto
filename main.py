#Artūrs Čubukovs 16.grupa 221RDB127 1.m.d.Datu struktūras
def is_matching_bracket(opening, closing):
    if opening == '[' and closing == ']':
        return True
    elif opening == '{' and closing == '}':
        return True
    elif opening == '(' and closing == ')':
        return True
    else:
        return False

def find_unmatched_bracket(s):
    stack = []
    for i in range(len(s)):
        if s[i] in ['[','{','(']:
            stack.append((s[i], i))
        elif s[i] in [']','}',')']:
            if not stack:
                return i + 1
            opening, index = stack.pop()
            if not is_matching_bracket(opening, s[i]):
                return i + 1
    if stack:
        opening, index = stack.pop()
        return index + 1
    return "Success"

if __name__=='__main__':
    #option = input("Enter 'F' to use test files or 'I' to input the brackets:")
    if option == 'F':
        with open('test_cases.txt', 'r') as f:
            test_cases = f.readlines()
        for test_case in test_cases:
            input_str = test_case.strip()
            print(find_unmatched_bracket(input_str))
    elif option=='I':
        input_str = input("Enter the string to check: ")
        print(find_unmatched_bracket(input_str))
    else:
        print("Invalid option")
