import os

folder = 'YOUR_FILE_PATH/' # ENTER YOYR FILE PATH HERE
items  = list(files for files in os.listdir(folder))
#print(items)   
def main():
    for i in range(len(items)):
        folder = 'YOUR_FILE_PATH/' + items[i]
        for count, filename in enumerate(os.listdir(folder)):
            dst = f"{items[i]}{str(count)}.jpg"
            src =f"{folder}/{filename}"
            dst =f"{folder}/{dst}"
            #print(f"Renaming {filename} >>> {items[i]}{str(count)}.jpg") # UNCOMMENT TO VISUALIZE THE PROCESS
            #print("count :", count)
            os.rename(src, dst) 

if __name__ == '__main__':
    main()


