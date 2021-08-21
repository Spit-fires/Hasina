import os
import shutil
userQ = input("apnar jonno ami ki korte pari? : ")
nameq = "apnar nan ki"
deleteQ = "delete koro"
if (userQ == nameq):
  print("Amar nam Hasina!")
if (userQ == deleteQ):
  print("Accha delete kortesi")
  shutil.rmtree(os.getcwd)
