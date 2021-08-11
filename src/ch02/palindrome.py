def main():
  print(is_palindrome("A man, a plan, a canal. Panama!"))

def is_palindrome(w):
  w = ''.join(e for e in w if e.isalnum()).lower()
  if len(w) % 2 == 0:
    middle = int(len(w)/2-1)
    return w[:middle:-1] == w[0:middle+1]
  else:
    middle = int(len(w)/2 - .5)
    return w[:middle:-1] == w[0:middle]



main()