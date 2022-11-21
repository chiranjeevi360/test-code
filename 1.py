def Base3Conversion(targetnumber):	
	if targetnumber >= 3:
		Base3Conversion(targetnumber // 3)
	print(targetnumber % 3, end = '')



targetnumber=int(input())
Base3Conversion(targetnumber)
