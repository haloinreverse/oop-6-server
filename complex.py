class TComplex:
    def __init__(self, *args):
        if len(args) == 1:
            if isinstance(args[0], str):
                nums = args[0].replace(' ', '').split('+')
                if len(nums) == 1:
                    self.real_part = float(nums[0])
                    self.im_part = 0
                else:
                    self.real_part = float(nums[0])
                    self.im_part = float(nums[1][:-1])
            else:
                self.real_part = int(args[0])
                self.im_part = 0
        else:
            self.real_part = args[0]
            self.im_part = args[1]

    def __str__(self):
        if self.real_part == 0 and self.im_part == 0:
            return '0'
        elif self.real_part == 0:
            return f'{self.im_part}i'
        elif self.im_part == 0:
            return f'{self.real_part}'
        elif self.im_part < 0:
            return f'{self.real_part}-{- self.im_part}i'
        else:
            return f'{self.real_part}+{self.im_part}i'

    def __abs__(self):
        return ((self.real_part) ** 2 + (self.im_part) ** 2) ** 0.5

    def __eq__(self, other):
        if self.real_part == other.real_part and self.im_part == other.im_part:
            return True
        else:
            return False

    def __add__(self, other):
        return TComplex(self.real_part + other.real_part, self.im_part + other.im_part)

    def __mul__(self, other):
        return TComplex(self.real_part * other.real_part - self.im_part * other.im_part, self.real_part * other.real_part + self.im_part * other.im_part)

    def __sub__(self, other):
        return TComplex(self.real_part - other.real_part, self.im_part - other.im_part)

    def __ne__(self, other):
        return not self == other

    def __truediv__(self, other):
        return TComplex((self.real_part * other.real_part + self.im_part * other.im_part) / (other.real_part ** 2 + other.im_part),
                        (self.im_part * other.real_part + self.real_part / other.im_part) / (other.real_part ** 2 + other.im_part))

    def __gt__(self, other):
        return abs(self) > abs(other)

    def __neg__(self):
        return TComplex(-self.real_part, -self.im_part)