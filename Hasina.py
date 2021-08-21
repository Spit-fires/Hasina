import os
import shutil
import time
while True:
 userQ = input("apnar jonno ami ki korte pari? : ")
 nameq = "apnar nam ki"
 deleteQ = "delete koro"
 path = "os.getcwd"
 if (userQ == nameq):
   print("Amar nam Hasina!")
 if (userQ == deleteQ):
   print("Accha delete kortesi")
   shutil.rmtree(path)
