import csv


def createurl(P1, P2, P3):
  URL = "https://docs.google.com/forms/d/e/1FAIpQLSdvCcqTyMU2XAeySFJjgcVhDTCEI3PBmhWs3FdhzHAGhOZgEQ/viewform?usp=pp_url&" + "entry.883835826=" + P1 + "&entry.1784547995=" + P2 + "&entry.16777235=" + P3
  return URL


def Createdoc(name):
  f = open(name, encoding='UTF8')
  csv_reader = csv.reader(f)
  #skipping header(first) line
  next(csv_reader)
  file = open("data.txt", "w")
  for line in csv_reader:
    #splitting up every line in csv into separate variables
    Email = line[0]
    P1val = line[1]
    P2val = line[2]
    P3val = line[3]
    file.write("email  --subject='some string' --to=" + Email + " << 
    EOM\n\n")
    file.write("For P1 = " + P1val + ", P2= " + P2val + " and P3 = " + 
    P3val    + "\n")
    file.write("Please fill out [this form] (" +
               createurl(P1val, P2val, P3val) + ")\n\n")
    file.write("EOM\n\n")
  file.close()


Createdoc("/content/drive/MyDrive/Colab Notebooks/trial.csv")


