import firebase_admin
from firebase_admin import credentials, storage
from PyQt5.QtWidgets import QApplication, QTreeView, QFileSystemModel, QWidget, QVBoxLayout
from PyQt5.QtCore import Qt

# Initialize Firebase Admin SDK
cred = credentials.Certificate('project1-b992a-firebase-adminsdk-gj507-160a321299.json')
firebase_admin.initialize_app(cred, {
    'storageBucket': 'project1-b992a.appspot.com'
})

# Get a reference to the bucket
bucket = storage.bucket()

# Create a PyQt5 application
app = QApplication([])

# Create a tree view widget and set the root path to '/'
treeview = QTreeView()
treeview.setRootIsDecorated(True)
treeview.setAlternatingRowColors(True)

# Create a file system model for the tree view
model = QFileSystemModel()
model.setRootPath('/')
treeview.setModel(model)

# Get a list of all files in the Firebase Storage bucket
blobs = bucket.list_blobs()

# Add each file to the file system model
for blob in blobs:
    model.setRootPath('/')
    row_count = model.rowCount()
    model.insertRows(row_count, 1)
    index = model.index(row_count, 0)
    model.setData(index, blob.name)
    flags = model.flags(index)
    model.setData(index, flags & ~Qt.ItemIsEditable, Qt.ItemDataRole)

# Create a main widget and layout for the tree view
widget = QWidget()
layout = QVBoxLayout()
layout.addWidget(treeview)
widget.setLayout(layout)

# Show the main widget
widget.show()

# Run the PyQt5 application
app.exec_()
