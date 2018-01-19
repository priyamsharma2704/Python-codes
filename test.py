from xml.etree.ElementTree import ElementTree
import re
l=[]
tree = ElementTree()
tree.parse("mechanical.xml")
root = tree.getroot()
wrapper = (tree.findall("namespace/wrapper"))

for child in wrapper:
	if('subclass' in child.attrib.keys()):
		del child.attrib['subclass']

for parent in root.findall('.//doc/..'):
	for child in parent.findall("doc"):
		#parent.remove(child)		
		if(child.text != None):
			print("child = ",child.text)
tree.write("output.xml", encoding="utf-8", xml_declaration=True)

newline=[]	
wordDic = {
'&lt;': '<',
'&gt;': '>'}

def multiwordReplace(text, wordDic):
  rc = re.compile('|'.join(map(re.escape, wordDic)))
  def translate(match):
    return wordDic[match.group(0)]
  return rc.sub(translate, text)

with open("output.xml","r") as f:    
	for word in f.readlines():
		str2 = multiwordReplace(word, wordDic)
		newline.append(str2)

with open("output.xml","w") as f:
    for line in newline:
        f.writelines(line)



# with open("output.xml","r") as f:    
# 	for word in f.readlines():
# 		newline.append(word.replace("&lt;", "<"))

# with open("output.xml","w") as f:
#     for line in newline:
#         f.writelines(line)	

# with open("output.xml","r") as f:    
# 	for word in f.readlines():
# 		newline1.append(word.replace("&gt;", ">"))