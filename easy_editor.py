import os
from PyQt5.QtWidgets import QApplication, QWidget, QFileDialog, QLabel, QPushButton, QListWidget, QHBoxLayout, QVBoxLayout
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PIL import Image
from PIL import ImageFilter
class ImageProcesor():
   def __init__ (self):
      self.image = None
      self.filename = None
      self.save_dir = 'mod'
   def loadImage(self, filename):
      self.filename = filename
      image_path = os.path.join(workdir, filename)
      self.image = Image.open(image_path)
   def showImage(label, path):
      image.hide()
      pixmapimage = QPixmap(path)
      w, h = image.width(), image.height()
      pixmapimage = pixmapimage.scaled(w, h, Qt.KeepAspectRatio)
      image.setPixmap(pixmapimage)
      image.show()
   def gray(self):
      self.image = self.image.convert("L")
      self.saveImage()
      image_path = os.path.join(workdir, self.save_dir, self.filename)
      self.showImage(image_path)
   def blur(self):
      self.image = self.image.filter(ImageFilter.BLUR)
      self.saveImage()
      image_path = os.path.join(workdir, self.save_dir, self.filename)
      self.showImage(image_path)
   def right(self):
      self.image = self.image.transpose(Image.ROTATE_270)
      self.saveImage()
      image_path = os.path.join(workdir, self.save_dir, self.filename)
      self.showImage(image_path)
   def left(self):
      self.image = self.image.transpose(Image.ROTATE_90)
      self.saveImage()
      image_path = os.path.join(workdir, self.save_dir, self.filename)
      self.showImage(image_path)
   def mirror(self):
      self.image = self.image.transpose(Image.FLIP_LEFT_RIGHT)
      self.saveImage()
      image_path = os.path.join(workdir, self.save_dir, self.filename)
      self.showImage(image_path)
   def saveImage(self):
      path = os.path.join(workdir, self.save_dir)
      if not(os.path.exists(path) or os.path.isdir(path)):
         os.mkdir(path)
      image_path = os.path.join(path, self.filename)
      self.image.save(image_path)
   
def chooseWorkdir():
   global workdir
   try:
      workdir = QFileDialog.getExistingDirectory()
   except:
      pass

def filter(fiels, extensions):
    result = []
    for res in fiels:
        for ext in extensions:
            if res.endswith(ext):
                result.append(res)
    return result
def showFilenamesList():
   try:
      extensions = ['.jpg', '.png', '.jpeg']
      chooseWorkdir()
      result = filter(os.listdir(workdir), extensions)
      file_list.clear()
      for res in result:
         file_list.addItem(res)
   except:
      pass

def showChosenImage():
    if file_list.currentRow() >= 0:
        filename = file_list.currentItem().text()
        workimage.loadImage(filename)
        image_path = os.path.join(workdir, workimage.filename)
        workimage.showImage(image_path)

#Создание окна 1
app = QApplication([])
window = QWidget()
window.resize(1150, 600)
window.setWindowTitle('Easy Editor')
# вижеты
but_folder = QPushButton('Папка')
but_left = QPushButton('Влево')
but_right = QPushButton('Вправо')
but_gray = QPushButton('серый')
but_blur = QPushButton('Размыть')
but_mirror = QPushButton('Зеркало')

file_list = QListWidget()
image = QLabel('IMAGE')
#линии
top_line = QHBoxLayout()
left_line = QVBoxLayout()
right_line = QVBoxLayout()
but_line = QHBoxLayout()
#вижеты на окне 1
but_line.addWidget(but_left)
but_line.addWidget(but_right)
but_line.addWidget(but_gray)
but_line.addWidget(but_blur)
but_line.addWidget(but_mirror)

left_line.addWidget(but_folder)
left_line.addWidget(file_list)
right_line.addWidget(image)
right_line.addLayout(but_line)

top_line.addLayout(left_line, 20)
top_line.addLayout(right_line, 80)
window.setLayout(top_line)
window.show()

workdir = ''
workimage = ImageProcesor()
file_list.currentRowChanged.connect(showChosenImage)
but_folder.clicked.connect(showFilenamesList)

but_gray.clicked.connect(workimage.gray)
but_left.clicked.connect(workimage.left)
but_right.clicked.connect(workimage.right)
but_mirror.clicked.connect(workimage.mirror)
but_blur.clicked.connect(workimage.blur)


app.exec()