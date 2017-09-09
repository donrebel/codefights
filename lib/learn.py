class Stack():
    def __init__(self):
        self.data = []

    def isEmpty(self):
        return self.data == []

    def push(self, item):
        self.data.append(item)

    def pop(self):
        return self.data.pop()

    def peek(self):
        return self.data[len(self.data) + 1]

# =========================================================

def parChecker(s):
    st = Stack()
    i = 0
    balanced = True
    while i < len(s) and balanced:
        if s[i] == '(':
            st.push(s[i])
        else:
            if st.isEmpty() == True:
                balanced = False
            else:
                st.pop()
        i += 1

    if balanced == True and st.isEmpty():
        return True
    else:
        return False

# =========================================================

def parChecker2(s):
    st = Stack()
    i = 0
    balanced = True
    while i < len(s) and balanced:
        if s[i] in '({[':
            st.push(s[i])
        else:
            if st.isEmpty():
                balanced = False
            else:
                top = st.pop()
                if is_matched(top, s[i]) == False:
                    balanced = False
        i += 1
    if st.isEmpty() and balanced is True:
        return True
    else:
        return False

def is_matched(o, c):
    opens = '[{('
    closers = ']})'
    return opens.index(o) == closers.index(c)

# =========================================================

def baseConverter(decNumber, base):
    st = Stack()
    digits = '0123456789ABCDEF'
    while decNumber > 0:
        rem = decNumber % base
        st.push(rem)
        decNumber = decNumber // base

    str = ''
    while st.isEmpty() is False:
        str = str + digits[st.pop()]

    return str

if __name__ == '__main__':

   print(baseConverter(25, 2))
   print(baseConverter(25, 16))




