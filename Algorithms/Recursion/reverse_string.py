def reverse_string(s: str) -> str:
   if len(s) <= 1:
       return s
   return s[-1] + reverse_string(s[:-1])
