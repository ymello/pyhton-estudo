def checkPalindrome(inputString):
  string = inputString
  invertida = string[::-1]

  if string == invertida:
    return True
  else:
    return False


print(checkPalindrome("yuri"))
print(checkPalindrome("aadaa"))