import xml.etree.cElementTree as ET

with open('mypage.html', 'w') as myFile:
    myFile.write('<html>')
    myFile.write('<body>')
    myFile.write("<pre>TYPE / STRING_ID / TIP_ID / ICON")
    tree = ET.parse("dstoolbar.xml")  #File name
    root = tree.getroot()
    #print("ROOT TAG = " + root.tag + "\n")
    for child_of_root in root:
        attrib_root = str(child_of_root.attrib.get('handle'))
        #print(attrib_root)
        myFile.write("<pre><br><br>------")
        myFile.write(attrib_root)
        myFile.write("------<br><br>")
        for child_of_child in child_of_root.iter(tag = "entry"):
            attrib_child = str(child_of_child.attrib)    	
            typeval = str(child_of_child.get('type'))
            stringval = str(child_of_child.get('stringid'))
            tipval = str(child_of_child.get('tipid'))
            iconval = str(child_of_child.get('icon'))
            if typeval == "None":
                myFile.write("&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;")
                myFile.write(typeval)
                myFile.write(" / ")
                myFile.write(stringval )
                myFile.write(" / ")
                myFile.write(tipval )
                myFile.write(" / ")
                myFile.write(iconval )
                myFile.write("<br>")
                
            else:
                myFile.write(typeval )
                myFile.write(" / ")               
                myFile.write(stringval )
                myFile.write(" / ")
                myFile.write(tipval )
                myFile.write(" / ")
                myFile.write(iconval )
                myFile.write("<br>")
    myFile.write('</body>')
    myFile.write('</html>')
