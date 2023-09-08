s = "MasterCard 3152479541115065"
name_point = s[:s.rfind(" ")]
point = s[s.rfind(" ")+1:]
f_point = point[:4] + ' ' + point[4:6] + '** **** ' + point[-4:]
print(f_point)