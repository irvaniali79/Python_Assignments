boys=['ali','reza','yasin','benyamin','mehrdad','sajjad','aidin','shahin']
girls=['sara','zari','neda','homa','eli','goli','mary','mina']
girls=set(girls)
print([(boys[i],girls.pop()) for i in range(len(boys))])