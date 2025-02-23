def oxford_comma(items):
    if len(items)==2:
        items[-1]= "and " + items[-1]
        return " ".join(items)
    if len(items)==1:
        return items[0]
    if len(items)>1:
        last_element = items[-1]
        if last_element:
            items[-1] = "and " + items[-1]
        else:
            print("dafuq")
    else:
        print("nothin")    
    print(", ".join(items))
    return ", ".join(items)
