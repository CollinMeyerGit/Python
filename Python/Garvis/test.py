ordinal = lambda n: "%d%s" % (n,"tsnrhtdd"[(n//10%10!=1)*(n%10<4)*n%10::4])
dates = [ordinal(n) for n in range(1,32)]
print(dates)