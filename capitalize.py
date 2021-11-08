



def capitalize(s):
    #return s.title()
    #l = s.split()
    #for i in range(len(l)):
     #   l.insert(i, l[i].capitalize())
      #  l.remove(l[i+1])
    #return ' '.join(l)
    for x in s[:].split():
        s = s.replace(x, x.capitalize())
    return s



