# megavideo.py
# This file is part of the megadown.
#
# Copyright(c) 2010 Krystof Celba
# kristofc@seznam.cz
#
# This file may be licensed under the terms of of the
# GNU General Public License Version 2 (the ``GPL'').
#
# Software distributed under the License is distributed
# on an ``AS IS'' basis, WITHOUT WARRANTY OF ANY KIND, either
# express or implied. See the GPL for the specific language
# governing rights and limitations.
#
# You should have received a copy of the GPL along with this
# program. If not, go to http://www.gnu.org/licenses/gpl.html
# or write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#

from xml.dom.minidom import parse, parseString
import urllib, re
	
def baseN(num,b,numerals="0123456789abcdefghijklmnopqrstuvwxyz"):
	return ((num == 0) and  "0" ) or ( baseN(num // b, b, numerals).lstrip("0") + numerals[num % b])

class megavideo:
	url = ""       # download url of video 
	size = ""      # size of video
	time = ""      # time of video
	title = ""     # title of video
	desc = ""      # description of video
	date = ""      # added date of video
	favorited = "" # number of favorites by users 
	comments = ""  # number of comments
	category = ""  # category of video
	tags = ""      # tags of video
	rating = ""    # rating of video
	
	def __init__(self, video_link):
		xml = parseString(urllib.urlopen(self.get_xml_link(video_link)).read())
		attr = xml.childNodes[0].childNodes[0]
		s = attr.getAttribute("s")
		un = attr.getAttribute("un")
		k1 = attr.getAttribute("k1")
		k2 = attr.getAttribute("k2")
		self.url = 'http://www'+s+'.megavideo.com/files/'+self.decrypt(un, int(k1), int(k2))+'/video.flv'
		self.size = str(round(int(attr.getAttribute("size"))/1048576.0, 1))
		self.time = attr.getAttribute("runtimehms")
		self.title = attr.getAttribute("title")
		self.desc = attr.getAttribute("description")
		self.date = attr.getAttribute("added")
		self.favorited = attr.getAttribute("favorited")
		self.comments = attr.getAttribute("comments")
		self.category = attr.getAttribute("category")
		self.tags = attr.getAttribute("tags")
		self.rating = attr.getAttribute("favorited")
		
	
	def get_xml_link(self, video_url):
		video_url += '"'
		video_code =re.findall(r'v=(.*?)"',video_url)[0]
		return "http://www.megavideo.com/xml/videolink.php?v=" + video_code

	def decrypt(self, _str, key1, key2):
		loc1 = []
		for i in _str:
			loc1.append(("000"+baseN(int(i, 16), 2))[-4:])
	
		loc1 = [s for s in ("".join(loc1))] 
		loc6 = []
		for i in range(384):
			key1 = (key1 * 11 + 77213) % 81371.0;
       			key2 = (key2 * 17 + 92717) % 192811.0;
        		loc6.append((key1 + key2) % 128.0);


		for i in range(256, -1, -1):
       		 	loc5 = int(loc6[i]);
        		loc4 = i % 128;
        		loc8 = loc1[loc5];
        		loc1[loc5] = loc1[loc4];
        		loc1[loc4] = loc8;
	
		for i in range(128):
        		loc1[i] = str(int(loc1[i]) ^ int(loc6[i + 256]) & 1);
	

		loc12 = "".join(loc1)
    		loc7 = []
    		for i in range(0, len(loc12), +4):
			loc9 = loc12[i:i+4]
        		loc7.append(loc9);

    		loc2 = [];
    		for i in range(len(loc7)):
			try:
        			loc2.append(baseN(int(loc7[i], 2), 16))
			except:
				loc2.append("0")
				pass

		return "".join(loc2)



