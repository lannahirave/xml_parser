import os

def main():
    arr = os.listdir()
    uies = []
    qrcs = []
    for i in arr:
        if i.endswith(".ui"):
            uies.append(i)
        if i.endswith('.qrc'):
            qrcs.append(i)
    name = ''
    print(uies)
    while name not in uies:
        name = input("Enter name of needed ui: ")
        if name.isdigit():
	        if 0 <= int(name) < len(uies):
		        name = uies[int(name)]
        if name == "":
            break
    try:
        os.system(f"pyuic5 {name} > {name[:-2]}py")
        print("Success")
    except Exception as e:
        print(e)
        
    print(qrcs)
    while name not in qrcs:
        name = input("Enter name of needed qrc: ")
        if name == "":
            return
    try:
        #pyrcc5 resource.qrc -o resource_rc.py
        os.system(f"pyrcc5 {name} -o {name[:-4]}_rc.py")
        print("Success")
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()