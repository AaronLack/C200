import astronomy as astr 

def F(m):
    def lbToKg(pnds):        # 1kg = 2.2lbs; 1lb =.453592kg
        pounds = .453592 #kg
        return pnds * pounds
    myWeight = lbToKg(m)
    return (astr.gravitationalConstant * myWeight * astr.earthMass) / ((astr.earthDiameter/2) ** 2)

print("{0:.2f} Newtons.".format(F(143.3)))
