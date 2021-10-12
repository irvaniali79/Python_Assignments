second=int(input())

hours=int(second/3600)

tmpsecond=int(second%3600)
minutes=int(tmpsecond/60)
sec=int(tmpsecond%60)

print(hours,':',minutes,':',sec)
