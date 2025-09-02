class reverseInt:
     def reverse(self, x: int) -> int:
          sign = -1 if x < 0 else 1
          x = abs(x)
          rev = int(str(x)[::-1])
          return sign*rev if rev < 2**31 else 0
     
     def secMethod(self,x):
          rev = 0
          while x != 0:
               rem = x % 10
               rev = rev * 10 + rem
               x = x // 10
          return rev

          
        
       

    
rev = reverseInt()
print(rev.reverse(45436))
