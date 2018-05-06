def is_num(x) :
    """ Returns True if x is an int, float, or complex. """
    return isinstance(x, (int, float, complex))

class DualNumber :
    """ Implements dual numbers of int, float, or complex. """
    def __init__(self, real = 0, dual = 0) :
        assert is_num(real) and is_num(dual)
        self._real = real
        self._dual = dual

    @property
    def real(self) :
        return self._real

    @property
    def dual(self) :
        return self._dual

    def __eq__(self, other) :
        if is_num(other) :
            return self.real == other.real and \
                   self.dual == 0
        if isinstance(other, DualNumber) :
            return self.real == other.real and \
                   self.dual == other.dual
        return NotImplemented

    def __str__(self) :
        sgn = '-' if self.dual < 0 else '+' 
        if isinstance(self.dual, complex) :
            dual = self.dual
        else :
            dual = abs(self.dual)
        return '{} {} {} eps'.format(self.real, sgn, dual)

    def __repr__(self) :
        return 'DualNumber({},{})'.format(self.real, self.dual)

    def __add__(self, other) :
        if is_num(other) :
            return DualNumber(self.real + other, self.dual)
        if isinstance(other, DualNumber) :
            return DualNumber(self.real + other.real,
                              self.dual + other.dual)
        return NotImplemented

    def __sub__(self, other) :
        if is_num(other) :
            return DualNumber(self.real - other, self.dual)
        if isinstance(other, DualNumber) :
            return DualNumber(self.real - other.real,
                              self.dual - other.dual)
        return NotImplemented

    def __mul__(self, other) :
        if is_num(other) :
            return DualNumber(self.real * other, self.dual * other)
        if isinstance(other, DualNumber) :
            return DualNumber(self.real * other.real,
                              self.real * other.dual +
                              self.dual * other.real )
        return NotImplemented

    def __pow__(self, power, *modulo) :
        """ Computes self ** power. If modulo is given or
        power is not an int, returns NotImplemented. """
        if modulo or not isinstance(power, int) :
            return NotImplemented
        result = DualNumber(1,0)
        double = self
        recip = False
        if power < 0 :
            recip = True
            power = -power
        # standard power accumulation algo
        while power > 0 :
            if power % 2 != 0 :
                result = result * double
            double = double * double
            power //=2

        if recip :
            return 1 / result
        return result
   
    def __truediv__(self, other) :
        if is_num(other) and other != 0 :
            return DualNumber(self.real / other, self.dual / other)
        if isinstance(other, DualNumber) and other.real != 0 :
            new_real = self.real / other.real
            new_dual = (self.dual * other.real - 
                        self.real * other.dual) / other.real**2
            return DualNumber(new_real, new_dual)
        return NotImplemented

    def __neg__(self) :
        return DualNumber(-self.real, -self.dual)

    def __radd__(self, other) :
        return self + other

    def __rsub__(self, other) :
        return -self + other

    def __rmul__(self, other) :
        return self * other

    def __rtruediv__(self, other) :
        if is_num(other) :
            return DualNumber(other) / self
        return NotImplemented
    
def derivative(f,a) :
    """ Given a function f defined using +,-,*,/, and integer pow,
    returns the numeric value f'(a). Computed using dual numbers. """
    return f(DualNumber(a,1)).dual
