def group_check(s):
  stack = []
  open = ['[', '{', '(']
  close = {']':'[', '}':'{',')':'('}
  for c in s:
    if c in open:
      stack.append(c)
    else:
      print c
      if close[c] == stack[-1]:
        stack.pop()
      else: return False
  return True if not stack else False

group_check('()')
