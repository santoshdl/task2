with open(r"C:\Users\LENOVO\Desktop\puresoft_assignment\draw-YOLO-box-main\draw-YOLO-box-main\labels\0BA2A4B4-4193-4506-8818-31564225EF8B.txt",'r') as fin:
    lines = fin.readlines()

element_names=['btn-inactive', 'btn-active', 'btn-red', 'btn-orange', 'btn-green']

bboxes=[]   
for line in lines:
    string = line.strip()
    bboxes.append(list(string.split(" ")))
    
print(bboxes)

t= sorted(bboxes, key=lambda x: x[2])

#print(t)

rows=[]

ref=float(t[0][2])
grp=[]
for idx, val in enumerate(t):
    print(val)
    if float(val[2])-float(ref) < 0.1:
           grp.append(idx)
    else:
         ref=t[idx][2]
         rows.append(grp)
         grp=[]
         grp.append(idx)

    if idx==len(t)-1:
              rows.append(grp)

element_count=["single", "double", "triple", "quadrapule"]
result=""
for num_row, row in enumerate(rows):
      r=sorted(t[row[0]:row[-1]+1], key=lambda x: x[1])
      str=""
      if num_row==0:
           #print("header")
           row_elements=[]
           for j in r:
               row_elements.append(element_names[int(j[0])]) 

           str="header {\n"+ ','.join(row_elements)+"\n}\n"
           result=result+str
      if num_row>0:
        #print(element_count[len(r)-1])
        str=str+"row {\n"
        for j in r:
             str=str+element_count[len(r)-1]+"{\n small-title, text"+ element_names[int(j[0])]+"\n}\n"
        str=str+"\n}\n"
        result=result+str
print(result)
with open("Output.txt", "w") as text_file:
   text_file.write(result)

