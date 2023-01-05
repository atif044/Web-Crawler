import time as tm
import os
def spider_shape():
    shape = """
        *           *
        *           *
        *           *
    *    *         *     *
    *     *       *      *
     *     *******      *
      *   *       *    *
       ***          ***
        * ( ⊙ o⊙  )  *
         *          *
        ***        ***
       *   ********   *
      *                *
     *                  *   
     *                  *
     *                  *    

         
    """
    print(shape)
   

def loading():
    i=1
    for _ in range (100):
        if i == 1:
            i=i+1
            print ("(/)")
        elif i == 2:
            i=i+1
            print ("(-)")
        elif i == 3:
            i=i+1
            print("(\)")
        elif i == 4:
            i=1
            print ("(-)")
        tm.sleep(0.1)
        os.system("cls" if os.name == "nt" else "clear")
    #tumahri arhi hai
def loading_line():
    
    #print("*************************************************************************************************")
    for i in range (95):
        if i==0:
             print('*|' ,end='')
        elif i==94:
            print('|*',end='')
        else:
            print('|' ,end='')
        tm.sleep(0.05)
    print("\n*************************************************************************************************")
    
    #os.system("cls" if os.name == "nt" else "clear")
        
# spider_shape()
#loading()

