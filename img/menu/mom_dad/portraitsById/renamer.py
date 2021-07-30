import os

path = "./"
directories = os.listdir(path)

numberOfMale = 0
for file in directories: 
    if file.startswith("male"):
        print(file)
        os.rename(path+file,path+file.replace('male_',''))
        numberOfMale += 1

numberOfFemale = 0
for file in directories:
    if file.startswith("female"):
        id = int(file.replace('female_','').replace('.png', ''))+numberOfMale
        os.rename(path+file,path+str(id)+'.png')
        numberOfFemale+=1

numberOfSpecialMale = 0
for file in directories:
    if file.startswith("special_male"):
        id = int(file.replace('special_male_','').replace('.png', ''))+numberOfMale+numberOfFemale
        os.rename(path+file,path+str(id)+'.png')
        numberOfFemale+=1

numberOfSpecialFemale = 0
for file in directories:
    if file.startswith("special_female"):
        id = int(file.replace('special_female_','').replace('.png', ''))+numberOfMale+numberOfFemale+numberOfSpecialMale
        os.rename(path+file,path+str(id)+'.png')
        numberOfSpecialFemale += 1

print("Finished to rename, there is (",numberOfMale, "male) (",numberOfFemale,"female) (",numberOfSpecialMale," specialMale) (",numberOfSpecialFemale," specialFemale)")