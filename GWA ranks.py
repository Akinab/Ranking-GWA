def details ():
    Description = "Ranking GWA."
    Date = "05-16-23"
    print ("\nDescription: {}\nDate: {}".format (Description , Date))
    
details ()

# open the input file
with open('students.txt', 'r') as f:
    lines = f.readlines()

# initialize variables to hold the highest GWA and the name of the student who got it
highest_gwa = 0.0
highest_gwa_student = ""

# iterate over the lines in the file
for line in lines:
    # split the line into a list of name and GWA
    name, gwa = line.strip().split()
    # convert the GWA to a float
    gwa = float(gwa)