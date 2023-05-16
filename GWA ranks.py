def details ():
    Description = "Ranking GWA."
    Date = "05-16-23"
    print ("\nDescription: {}\nDate: {}".format (Description , Date))
    
details ()

# open the input file
with open('students.txt', 'r') as f:
    lines = f.readlines()