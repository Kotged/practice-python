import re
pose_estimation=input('Enter data: ')
pattern1=re.compile(r'\d\.\d+,\s\d\.\d+')
print('points=',pattern1.findall(pose_estimation))
pattern2=re.compile(r'\d\.\d+\s')
print('scoresss=',pattern2.findall(pose_estimation))