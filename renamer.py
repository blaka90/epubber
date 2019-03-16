import zipfile
from lxml import etree
import os
import getpass
from time import sleep
from sys import platform, exit


os_sys = platform
user = getpass.getuser()

if "darwin" in os_sys:
	downloads = "/Users/"+user+"/Downloads/"
	epub_dir = "/Users/"+user+"/Documents/python/epubber/temp"
elif "linux" in os_sys:
	downloads = "/home/" + user + "/Downloads/"
	epub_dir = "/home/" + user + "/Documents/python/epubber/temp"
else:
	print("Sorry something went wrong when changing directorys")
	sleep(2)
	exit(10)

os.chdir(downloads)


def get_epub_info(fname):
	ns = {
		'n': 'urn:oasis:names:tc:opendocument:xmlns:container',
		'pkg': 'http://www.idpf.org/2007/opf',
		'dc': 'http://purl.org/dc/elements/1.1/'
	}

	# prepare to read from the .epub file
	try:
		zzip = zipfile.ZipFile(fname)

		# find the contents meta file
		txt = zzip.read('META-INF/container.xml')
		tree = etree.fromstring(txt)
		cfname = tree.xpath('n:rootfiles/n:rootfile/@full-path', namespaces=ns)[0]

		# grab the metadata block from the contents meta file
		cf = zzip.read(cfname)
		tree = etree.fromstring(cf)
		p = tree.xpath('/pkg:package/pkg:metadata', namespaces=ns)[0]
		title = p.xpath('dc:title/text()', namespaces=ns)[0]

		return title
	except Exception as e:
		print("-" * 15 + "\n" + str(e) + ":")
		print(fname)
		exit(7)


'''
def get_dir():
	u_dir = raw_input("type the directory you want to work with?: ")
	if os.path.isdir(u_dir):
		os.chdir(u_dir)
	else:
		print "not a valid path please try again"
		main()
	return u_dir
'''


def renamer():
	for f in os.listdir(downloads):
		if f.endswith(".epub"):
			f_name = f[:13]
			f_title = get_epub_info(f) + ".epub"
			os.rename(f, f_title)
			for n in os.listdir(downloads):
				ext = "_code.zip"
				ext2 = ".pdf"
				zip_title = f_title[:-5] + ".zip"
				pdf_title = f_title[:-5] + ext2
				if n.lower() == f_name + ext:
					os.rename(n, zip_title)
				if n.endswith(ext2) and n.startswith(f_name):
					os.rename(n, pdf_title)
			sleep(0.25)
		else:
			continue



