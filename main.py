print('\033[93m'+"""
 _   _            _           
| |_| |_  __ _ __| |___ _ __  
| / / ' \/ _` / _` / -_) '  \ 
|_\_\_||_\__,_\__,_\___|_|_|_|
                              
      _              _       _ _ 
 __ _| |  _ __  __ _| |_  __| (_)
/ _` | | | '  \/ _` | ' \/ _` | |
\__,_|_| |_|_|_\__,_|_||_\__,_|_|
                                 
""")
print('\033[91m'+"""
                         _         __ _           _           
     _ __ ___  _   _ ___(_) ___   / _(_)_ __   __| | ___ _ __ 
    | '_ ` _ \| | | / __| |/ __| | |_| | '_ \ / _` |/ _ \ '__|
    | | | | | | |_| \__ \ | (__  |  _| | | | | (_| |  __/ |   
    |_| |_| |_|\__,_|___/_|\___| |_| |_|_| |_|\__,_|\___|_|   
                                                          
""")
print('\033[93m'+"""
    
    \033[93myoutube =\033[92m b2n.ir/khodekhadem 
    \033[93mtelegram =\033[92m @khodekhadem
    \033[93minstagram =\033[92m khodekhadem
    """
    )  
try: 
    import os
    import sys
    from googlesearch import search 
    import requests
    import wget
    from tqdm import tqdm
    from clint.textui import progress

except ImportError: 
        
    print("in 2 dastoor ro vared kon \n(pip install -r requirements.txt)\n(pip3 install -r requirements.txt)")
    print("********************")
    print("enter these two command \n(pip install -r requirements.txt)\n(pip3 install -r requirements.txt)")

class bcolors:
    blue = '\033[96m'
    green = '\033[92m'
    yellow = '\033[93m'
    red = '\033[91m'
    normal = '\033[0m'

def download_link(link):
	link = 'mpv --audio-display=no  "'+link+'"'
	os.system(link)	




# to search
print(bcolors.blue+"matn ahang , maddahi ya ... ro benevis\n ***be farsi benevisid\n")
print("enter a part of the music text \n"+bcolors.normal)
query = sys.argv[1]
print("\n")
site_list = []
for j in search(query,  lang='ir', num=10, stop=10, pause=2): 
    if j.find("youtube.com") == -1 and j.find("aparat.com") == -1 :
        site_list.append(j)



for music_i in range (len(site_list)):


	music_list = []
	webpage=requests.get( site_list[music_i] )
	webpage = webpage.text    

	cc = 0
	while 1==1 :
	    c = webpage.find('.mp3"',cc)
	    cc = c+1
	    #print(c)
	    #print(webpage[c-20:c+20])
	    if c == -1:
	        #print("braked")
	        break
	    b = webpage.rfind('href="',0,c+1)
	    #print(b)
	    a = webpage.rfind('<',0,c+1)
	    #print(a)
	    if a != -1 and b != -1 and c != -1 :
	        if a < b :       
	            music_url = webpage[b+6:c+4]
	            #print(music_url)
	            music_list.append(music_url)
	

	if len(music_list) > 0 :

		for i in range (len(music_list)) :
			if "320" in (music_list[i][ music_list[i].rfind("/")+1   : ].replace("%20"," ")):
				download_link(music_list[i])
			else :
				download_link(music_list[0])
			if i == 4 :

				break
		    
		    
		print(bcolors.green+"\ndownload shoro shod")        
		print("\ndownload started :)\n"+bcolors.normal)
		#mp3 = requests.get(music_list[music_num])
		#name = music_url[ music_url.rfind("/")+1   : ].replace("%20"," ")
		#with open('./' + name , 'wb') as f:
		#    f.write(mp3.content)

		#wget.download(music_list[music_num])
		print(bcolors.yellow+"")
		download_link(music_list[music_num])
		print(bcolors.green+"\ndownload tamoom shod \nahang zakhire shod\n")
		print("download end  \nmusic saved"+bcolors.normal)
		break





    
