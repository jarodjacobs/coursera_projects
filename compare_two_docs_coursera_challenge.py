
def singleline_diff(string1, string2):
    
    string1_open = open(string1, "rt")
    string1 = string1_open.read()
    string1_open.close()

    string2_open = open(string2, "rt")
    string2 = string2_open.read()
    string2_open.close()
    
    if len(string1) <= len(string2):
        shortest_string = string1
    else:
        shortest_string = string2
    if len(string1) >= len(string2):
        longest_string = string1
    else:
        longest_string = string2
    if len(string1) == 0 and len(string2) != 0:
        print("0")
        return
    if len(string1) == 0 and len(string2) == 0:
        print("IDENTICAL")
        return
    if len(string1) == len(string2):
        for i in range(0, len(shortest_string)):
            if string1[i] != string2[i]: 
                print(i)
                return
        print("IDENTICAL")
    else:
        for i in range(0, len(shortest_string)):
            if string1[i] != string2[i]: 
                print(i)
                return
        print(len(shortest_string)+1)
        
            
#singleline_diff("file7.txt", "file10.txt")


