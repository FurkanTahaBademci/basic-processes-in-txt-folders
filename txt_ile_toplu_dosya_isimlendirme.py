import os
import glob""

folder = "C:\\Users\\90551\\Desktop\\plaka_veri\\plaka\\"
for count, filename in enumerate(os.listdir(folder)):
    oldname = folder + filename   
    newname = folder + "dosya" + str(count + 1) + ".jpg"
    os.rename(oldname, newname)

# printing the changed names
print(glob.glob(folder + "."))