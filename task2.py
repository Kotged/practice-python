objects_list=list( input('Enter the names of the objects: ').split())

if len(objects_list)==1:
    print(objects_list[0])
elif len(objects_list)==2:
    print(objects_list[0]+ ' and '+ objects_list[1])

else:
    edited_list=''
    for i in range(len(objects_list)):
        
        if i==len(objects_list)-1:
            edited_list= edited_list + ', and '+ objects_list[-1]
        elif i==0:
            edited_list=objects_list[0]
       
        else:
            edited_list= edited_list +', '+objects_list[i]
    print(edited_list)
  
 
