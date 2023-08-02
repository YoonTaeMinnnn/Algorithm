def sample():

  stack = []
  s = " 7 5 - "
  s = s.split(" ")
  s = s[1:len(s)-1]
  
  for i in s:
    if i.isdecimal():
      if 0 <= int(i) <= 2**20 - 1:
        stack.append(int(i))
    elif i == "POP":
      if stack:
        stack.pop()
      else:
        return -1
    elif i == "DUP":
      if stack:
        stack.append(stack[-1])
      else:
        return -1
    elif i == "+":
      if stack:
        a = stack.pop()
        if stack:
          b = stack.pop()
          if a+b > 2**20-1:
            return -1
          stack.append(a+b)
        else:
          return -1
      else:
        return -1
    elif i == "-":
      if stack:
        a = stack.pop()
        if stack:
          b = stack.pop()
          if a-b < 0:
            return -1
          else:
            stack.append(a-b)
        else: 
          return -1
      else:
        return -1
        
  if not stack:
    return -1
  return stack.pop()


print(sample())
