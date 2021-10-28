#coding=utf-8
#!/usr/bin/python2
#coding=utf-8
try:
    import os,re,time
except IOError:
    os.system("pip2 install requests")
    os.system("pip2 install mechanize")
    os.system("python2 infect.xo")

try:
    os.mkdir("/sdcard/infect-tool")
except OSError:
    pass

420 = """
\033[1;97m     .... NO! ...                  ... MNO! ...
   ..... MNO!! ...................... MNNOO! ...
 ..... MMNO! ......................... MNNOO!! .
.... MNOONNOO!   MMMMMMMMMMPPPOII!   MNNO!!!! .
 ... !O! NNO! MMMMMMMMMMMMMPPPOOOII!! NO! ....
    ...... ! MMMMMMMMMMMMMPPPPOOOOIII! ! ...
   ........ MMMMMMMMMMMMPPPPPOOOOOOII!! .....
   ........ MMMMMOOOOOOPPPPPPPPOOOOMII! ...  
    ....... MMMMM..    OPPMMP    .,OMI! ....
     ...... MMMM::   o.,OPMP,.o   ::I!! ...
         .... NNM:::.,,OOPM!P,.::::!! ....
          .. MMNNNNNOOOOPMO!!IIPPO!!O! .....
         ... MMMMMNNNNOO:!!:!!IPPPPOO! ....
           .. MMMMMNNOOMMNNIIIPPPOO!! ......
          ...... MMMONNMMNNNIIIOO!..........
       ....... MN MOMMMNNNIIIIIO! OO ..........
    ......... MNO! IiiiiiiiiiiiI OOOO ...........
  ...... NNN.MNO! . O!!!!!!!!!O . OONO NO! ........
   .... MNNNNNO! ...OOOOOOOOOOO .  MMNNON!........
   ...... MNNNNO! .. PPPPPPPPP .. MMNON!........
      ...... OO! ................. ON! .......
         ................................

\033[1;97m     
\033[1;93m      
\033[1;93m      
\033[1;93m      
\033[1;97m       
\033[1;97m     
\033[1;97m------------------------------------------------- 
\033[1;97m(~) Author  : Mosin 420
\033[1;97m(~) Github  : https://github.com***
\033[1;97m(~) Fb Page : https://facebook.com***
\033[1;97m-------------------------------------------------
"""

def main():
    os.system("clear")
    print(abm)
    os.system("cd load && python2 __loading__")
    os.system("clear")
    print(abm)
    print("\033[1;97m[\033[1;93m1\033[1;97m] Install infect tool for cloning")
    time.sleep(0.05)
    print("\033[1;97m[\033[1;93m2\033[1;97m] Install infect extracting tool")
    time.sleep(0.05)
    print("\033[1;97m[\033[1;93m0\033[1;97m] Tool Logout")
    time.sleep(0.05)
    print("\033[1;97m-------------------------------------------------")
    mx()
def mx():
    tech_abm = raw_input("\n[!] Select a valid option : ")
    if tech_abm =="1":
        os.system("cd data && python2 data")
    if tech_abm =="2":
        os.system("cd exts && python2 exts")
    if tech_abm =="0":
        print("")
        print("\033[1;92mTool Logout Successfull").center(50)
        print("")
        os.system("exit")
    else:
        print("")
        print("\033[1;91mPlease select a valid option").center(50)
        print("")
        time.sleep(1)
        main()
if __name__ == '__main__':
    main()
