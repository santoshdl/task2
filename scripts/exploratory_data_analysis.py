import os
import matplotlib.pyplot as plt

def get_label_counts(path, element_names):
    stats={}

    for ele in element_names:
       stats[ele]=0

    annotations=os.listdir(path)
    
    for annotation in annotations:
       with open(os.path.join(path,annotation)) as fin:
         lines = fin.readlines()

       for line in lines:
          line=line.strip()
          line=line.replace(",", " ")
          elements=list(line.split(" "))

          for element in elements:
             if element in element_names:
                stats[element]=stats[element]+1

    return stats


if __name__=="__main__":
    dir_path=r"C:\Users\LENOVO\Desktop\puresoft_assignment\Assignment_Data\Assignment_Data\D3" #r"C:\Users\LENOVO\Desktop\puresoft_assignment\Assignment_Data\Assignment_Data\D2"
    num_images=len(os.listdir(os.path.join(dir_path, "IMAGES")))
    element_names= ['field-inactive','img-btn-card','img-txt-btn-card','btn','entry','field-active','category','img-card','user-img','user-img-user-name','logo-txt']
    #['btn-inactive', 'btn-active', 'btn-red', 'btn-orange', 'btn-green'] #['page-title','ck-box','radio','dropdn','slider','search-bar','btn-active','btn-inactive','btn-green','btn-orange','btn-red','icons','cart-link','burger-link','rating','medium-title']
    stats=get_label_counts(os.path.join(dir_path, "TEXT_LABELS"), element_names)
    print(stats)
    plt.bar(*zip(*stats.items()))
    plt.show()
