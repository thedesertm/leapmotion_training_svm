# LeapMotion 
## installation 

> To get started...
   ### Step 1
       - install leap motion sdk that suits your os 
       - put the sdk files "Leap.py","LeapPython.so/dll" and "libLeap.so/dll" inside lib folder
       - install python > 2.6
   ### Step2
       -- ssh to the pi through putty and begot the instalation process 
       -- download dependencies      
      ```shell
      $ python -m pip install PyQt4
      $ python -m pip install numpy
      $ python -m pip install pandas
      $ python -m pip install sklearn
      $ python -m pip install vlc
      ```
> To collect dataset...
 ```shell
     $ python collect_data.py
 ```
> To train the model...
 ```shell
     $ python trainer.py
 ```  
> To evaluate the model...
 ```shell
     $ python prediction.py
 ```

     

