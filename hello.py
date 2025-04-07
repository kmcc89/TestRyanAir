import os 

#Test program to print OS and working directory
print("Hello World")

print("Running python script in docker container")

print("OS name: " + os.name)

print("Current directory: " + os.getcwd())

if(os.name == 'nt'):
    driver_path = 'Windows driver path'
else:
    driver_path = 'Other OS driver path'

print(driver_path)