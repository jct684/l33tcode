class Solution:
    def reverse(self, x: int) -> int:
        #x may be positive or negative integer
        #output a reversed integere unless it is outside the 32-bit range
        #if outside the 32-bit range then return 0
        if x >= 0:
            sign = 1
        else:
            sign = -1
        x_copy = abs(x)
        new_x = 0
        while x_copy > 0:
            digit = x_copy % 10
            x_copy = x_copy // 10
            new_x = new_x * 10
            new_x += digit
            if new_x > 2**31:
                return 0
        return new_x * sign