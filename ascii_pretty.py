#!/usr/bin/python
print ("    |"),
for i in range(0, 0x10):
    print("+%x" % i,)
print ("\n----+-" + ("-" * 0x10 * 3))

for j in range(0, 0x80, 0x10):
    print (" %.2x |" % j,)
    for i in range (0, 0x10):
        ch = j + i
    if ch >= 0x20 and ch < 0x7f:
        print (" %c" %ch,)
    elif ch == ord ("\n"):
        print ("\\n",)
    elif ch == ord ("\t"):
        print ("\\t",)
    elif ch == ord("\r"):
        print ("\\r",)
    else:
        print (" ",)
    
print
