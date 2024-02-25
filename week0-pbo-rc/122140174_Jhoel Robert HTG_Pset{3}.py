# The final Problem set is to use the File I/O. you will create a file Me.txt and write some lines. At the end, you’ll have txt files look like this

file_name = 'ME.txt'

text = "Name: Jhoel Robert...dst \nNIM : 122140174 \nResolusi saya ditahun ini: Tidak ada resolusi, pengennya mencari makna hidup di dunia ini."

with open(file_name, 'w') as f:
    f.write(text)