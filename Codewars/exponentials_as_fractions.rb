# def expand(x,digits)
#   fraction = [1,1]
#   i=1
#   y=x
#   fact = 1
#   while true
#     fraction = add_fractions(fraction,[y,fact],i)
#     if fraction[0].to_s.length >= digits
#       return fraction
#     end
#     i += 1
#     fact *= i
#     y *= x
#   end
# end
#
# def add_fractions(a,b,i)
#   a = to_fraction(a)
#   b = to_fraction(b)
#   return reduce_fraction([a[0]*b[1] + a[1]*b[0],a[1]*b[1]],i)
# end
#
# def reduce_fraction(fraction,i)
#   while i > 0
#   if fraction[0] % i == 0 && fraction[1] % i == 0 && i > 1
#     fraction = [fraction[0]/i.to_i,fraction[1]/i.to_i]
#     i += 1
#   end
#   i = i-1
#   end
#   return fraction
# end
#
# def to_fraction(fraction)
#   i = 1
#   x = fraction[0]
#   while (x * i).to_i != (x * i)
#     i+=1
#   end
#   return [(fraction[0]*i).to_i,fraction[1]*i]
# end

def expand(x,digits)
  #puts("x #{x}, digits #{digits}")
  fraction = "1"
  i=1
  y = Rational(x.to_s)
  fact = 1
  while true
    fraction = Rational(fraction.to_s) + Rational(y.to_s,fact.to_s)

    if fraction.numerator.to_s.length >= digits
      return [fraction.numerator,fraction.denominator]
    end
    i += 1
    fact *= i
    y = Rational(Rational(y.to_s) * Rational(x.to_s))
  end
end

# **** The Rational() function does not work correctly ****
# eg Rational(1.6) = (3602879701896397/2251799813685248)
# not
# (8/5)
