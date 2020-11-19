from PyQt4 import QtGui
import sys

class Widget(QtGui.QWidget):

       def __init__(self):
           super(Widget, self).__init__()
           self.initUI()


       def initUI(self):
           self.setGeometry(600, 300, 400, 200)
           self.setWindowTitle('Multiple Browse')     

           btn = QtGui.QPushButton('Browse', self)
           btn.resize(btn.sizeHint())
           btn.clicked.connect(self.SingleBrowse)
           btn.move(150, 100)

           self.csv = []     

           self.show()

       def SingleBrowse(self):
           if len(self.csv) < 2:
               filePath = QtGui.QFileDialog.getOpenFileName(self, 
                                                      '',
                                                      "Desktop",
                                                     '*.csv')

               if filePath != "" and not filePath in self.csv:
                   self.csv.append(filePath)
           if len(self.csv) == 2:
               self.process()


       def process(self):
           import pandas as pd
           from pandas import DataFrame

           df1 = pd.read_csv(self.csv[0]) 
           df2 = pd.read_csv(self.csv[1])

           df3 = df1.loc[:, ['a_column', 'b_column']] 

           df3[""] = "" 

           df4 = df2.loc[:, ['c_column','d_column' , 'e_column']]

           new = pd.concat([df3, df4], axis=1)

           new.index = new.index + 1

           new.to_csv('csv2.csv')

def main():
       app = QtGui.QApplication(sys.argv)
       w = Widget()
       app.exec_()


if __name__ == '__main__':
       main()