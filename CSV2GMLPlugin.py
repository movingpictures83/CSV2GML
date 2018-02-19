import sys
#import numpy
import PyPluMA


class CSV2GMLPlugin:
   def input(self, filename):
      self.myfile = filename

   def run(self):
      filestuff = open(self.myfile, 'r')
      firstline = filestuff.readline()
      self.bacteria = firstline.split(',')
      self.bacteria.remove('\"\"')
      self.n = len(self.bacteria)
      self.ADJ = []
      i = 0
      for line in filestuff:
         contents = line.split(',')
	 self.ADJ.append([])
         for j in range(self.n):
            value = float(contents[j+1])
            if (i != j and value != 0):
               self.ADJ[i].append(value)
            else:
               self.ADJ[i].append(0)
         i += 1

   def output(self, filename):
      gmlfilename = self.myfile[0:len(self.myfile)-3] + "gml"
      gmlfile = open(gmlfilename, 'w')
      PyPluMA.log("Writing GML file ")

      gmlfile.write("graph [\n")
      for i in range(self.n):
         gmlfile.write("node [\n")
         gmlfile.write("id "+str(i)+"\n")
         gmlfile.write("label "+self.bacteria[i].strip()+"\n")
         gmlfile.write("]\n")

      for i in range(self.n):
         for j in range(i+1, self.n):
            if (self.ADJ[i][j] != 0):
               gmlfile.write("edge [\n")
               gmlfile.write("source "+str(i)+"\n")
               gmlfile.write("target "+str(j)+"\n")
               gmlfile.write("weight "+str(self.ADJ[i][j])+"\n")
               gmlfile.write("]\n")

      gmlfile.write("]\n")




