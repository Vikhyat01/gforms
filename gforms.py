import csv


def createurl(line):
  URL = "https://docs.google.com/forms/d/e/1FAIpQLSdvCcqTyMU2XAeySFJjgcVhDTCEI3PBmhWs3FdhzHAGhOZgEQ/viewform?usp=pp_url&" + "entry.883835826=" + line[
    1] + "&entry.1784547995=" + line[2] + "&entry.16777235=" + line[3]
  return URL


def Createdoc(name):
  f = open(name, encoding='UTF8')
  csv_reader = csv.reader(f)
  next(csv_reader)
  file = open("data.txt", "w")
  for line in csv_reader:
    file.write("email  --subject='some string' --to=" + line[0] +
               " << EOM\n\n")
    file.write("For P1 = " + line[1] + ", P2= " + line[2] + " and P3 = " +
               line[3] + "\n")
    file.write("Please fill out [this form] (" + createurl(line) + ")\n\n")
    file.write("EOM\n\n")
  file.close()


Createdoc("/content/drive/MyDrive/Colab Notebooks/trial.csv")


