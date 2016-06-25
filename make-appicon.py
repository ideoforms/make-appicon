#!/usr/local/bin/python

#------------------------------------------------------------------------
# make-appicon: Generates Xcode-format AppIcon bundle containing
#               multiple icon thumbnails. Requires ImageMagick and
#               the `convert` command-line tool.
#
# Created by Daniel Jones (2016)
# <http://www.erase.net/>
#------------------------------------------------------------------------

import subprocess
import shutil
import sys
import os

if len(sys.argv) < 2:
    print "Usage: %s <input.png>" % sys.argv[0]
    sys.exit(1)

in_file = sys.argv[1]

#------------------------------------------------------------------------
# Binary and output paths
#------------------------------------------------------------------------
CONVERT = "/usr/local/bin/convert"
AUX_DIR = "aux"
OUT_DIR = "AppIcon.appiconset"
CONTENTS_FILE = "Contents.json"

icon_files = {
    "Icon-40.png" : 40,
    "Icon-40@2x.png" : 80,
    "Icon-40@3x.png" : 120,
    "Icon-60@2x.png" : 120,
    "Icon-60@3x.png" : 180,
    "Icon-76.png" : 76,
    "Icon-76@2x.png" : 152,
    "Icon-83.5@2x.png" : 167,
    "Icon-Small.png" : 29,
    "Icon-Small@2x.png" : 58,
    "Icon-Small@3x.png" : 87
}

if os.path.exists(OUT_DIR):
    print "%s already exists, not creating" % (OUT_DIR)
    sys.exit(1)

os.mkdir(OUT_DIR)
shutil.copy(os.path.join(AUX_DIR, CONTENTS_FILE), os.path.join(OUT_DIR, CONTENTS_FILE))

#------------------------------------------------------------------------
# Iterate over required icon sizes
#------------------------------------------------------------------------
for name, size in icon_files.items():
    print "%s (%dx%d)" % (name, size, size)
    out_file = os.path.join(OUT_DIR, name)
    subprocess.call([ CONVERT, in_file, "-resize", "%dx%d^" % (size, size), "-gravity", "center", "-crop", "%dx%d+0+0" % (size, size), out_file ])

