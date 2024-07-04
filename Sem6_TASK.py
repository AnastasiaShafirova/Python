# Напишите функцию, которая принимает одно число и проверяет, является ли оно 
# простым (делится на  1 и на N)
#  5 => yes

def natural(Turn, del1=2):
    if del1*del1>=Turn:
        return True
    elif Turn%del1==0:
        return False
    return natural(Turn, del1+1)

print(natural(10))



# определить полиндром введеных с ло или нет. полиндром это число которое 
# читается слева направо также как ис право на лево
# СРЕЗЫ!!!!

def revs1(n):
    if n[0] != n[-1]:
        return False
    elif len(n) <= 1:
        return True
    return revs1(n[1:-1])
print(revs1("12321"))