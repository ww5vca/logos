# %%
import glob
import os
import urllib.parse

import imagesize

# %%
fdLst = ['OEM', 'Supplier', 'Flag', 'Icon', 'Model']
templateSheet = """                <li id="{}">{}</li>
"""
templateBox = """        <div class="box {}">
            <div class="img-box">
                <img src="./logos/{}/{}.png"
                alt="{} {}x{} png" title="{} {}x{} png">
            </div>
            <div class="txt txt-hidden">{} {}x{} png</div>
        </div>
"""

# %%
htmlSheet = """                <!-- replacer flag sheet -->
"""
htmlBox = """        <!-- replacer flag box -->
"""
for fd in fdLst:
    fdLower = fd.lower()
    htmlSheet += templateSheet.format(fdLower, fd)
    gbPath = os.path.normpath(os.path.join("./logos/", fdLower, "*.png"))
    for i in glob.glob(gbPath):
        imgSize = imagesize.get(i)
        imgInfo = [fdLower, os.path.basename(i)[:-4], imgSize[0], imgSize[1], "png"]        
        htmlBox += templateBox.format(imgInfo[0], 
                                      imgInfo[0], urllib.parse.quote(imgInfo[1].encode('utf-8')), 
                                      imgInfo[1], imgInfo[2], imgInfo[3], imgInfo[1], imgInfo[2], imgInfo[3], imgInfo[1], imgInfo[2], imgInfo[3])

with open("./index.html", "w", encoding="utf-8") as i:
    with open("./template.html", "r", encoding="utf-8") as d:
        for htmlLine in d:
            if "replacer flag sheet" in htmlLine:
                i.write(htmlSheet)
            elif "replacer flag box" in htmlLine:
                i.write(htmlBox)
            else:
                i.write(htmlLine)