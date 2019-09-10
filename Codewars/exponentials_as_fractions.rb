# def expand(x, digit)
#     fraction = [1,1]
#     i = 1
#
#   mult = frac_to_i(x)
#
#     while true
#       fraction[1] *= i
#       fraction[1] *= mult**i
#       fraction[0] = fraction[0] * i * mult**i + x**i * mult**i
#       gcd_frac = gcd(fraction,i)
#       if gcd_frac[0].to_s.length >= digit
#         return gcd_frac
#       end
#       i += 1
#     end
# end
#
# def gcd(fraction,i)
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
# def frac_to_i(x)
#   i = 1
#   while (x * i).to_i != (x * i)
#     i+=1
#   end
#   return i
# end

def expand(x,digits)
  fraction = [1,1]
  i=1
  fact = 1
  while true
    fraction = add_fractions(fraction,[x**i,fact],i)
    if fraction[0].to_s.length >= digits
      return fraction
    end
    i += 1
    fact *= i
  end
end

def add_fractions(a,b,i)
  a = to_fraction(a)
  b = to_fraction(b)
  return reduce_fraction([a[0]*b[1] + a[1]*b[0],a[1]*b[1]],i)
end

def reduce_fraction(fraction,i)
  while i > 0
  if fraction[0] % i == 0 && fraction[1] % i == 0 && i > 1
    fraction = [fraction[0]/i.to_i,fraction[1]/i.to_i]
    i += 1
  end
  i = i-1
  end
  return fraction
end

def to_fraction(fraction)
  i = 1
  x = fraction[0]
  while (x * i).to_i != (x * i)
    i+=1
  end
  return [(fraction[0]*i).to_i,fraction[1]*i]
end
