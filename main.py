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
def main():
    text = input()
    if 'I' in text:
        text = input()
    elif 'F' in text:
        file = "./test/5"
        with open(file) as f:
            text = f.read()
    mismatch = find_mismatch(text)
    # Printing answer, write your code here
    if not mismatch :
        print("Success")
    else:
        print(mismatch)
if __name__ == "__main__":
    main()
