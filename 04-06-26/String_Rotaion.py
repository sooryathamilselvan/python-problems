s1="abcd"
s2="dabc"
if len(s1)==len(s2) and s2 in (s1+s2):
    print("rotaion")
else:
    print("Not a rotaion")
