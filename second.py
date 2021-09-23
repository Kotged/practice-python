magnitude=float(input('Magnitude of the earthquake: ')) #input of information
if magnitude<2:
    descriptor='micro'
elif magnitude>=2 and magnitude<3:
    descriptor='very minor'
elif magnitude>=3 and magnitude<4:
    descriptor='minor'
elif magnitude>=4 and magnitude<5:
    descriptor='light'
elif magnitude>=5 and magnitude<6:
    descriptor='moderate'
elif magnitude>=6 and magnitude<7:
    descriptor='strong'
elif magnitude>=7 and magnitude<8:
    descriptor='major'
elif magnitude>=8 and magnitude<10:
    descriptor='great'
elif magnitude>=10:
    descriptor='meteoric'
print('The earthquake of magnitude ' + str(magnitude) + ' is ' + str(descriptor)) #output information
