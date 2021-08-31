import sys
import os
import webbrowser
import time
from pyfiglet import Figlet
########################################################
os.system("clear")
########################################################
f = Figlet(font='sbook')
print(f.renderText("DZ-XMAN"))
print("created by ali_bealia")
print('-'*60)
def main():
	per = input("Do You want to continue(Y/N): ")
	if per=='Y' or 'y' :
		print('''
			{1}-install all packages directly
			{2}-by number
			{3}-Exit
			''')
		aa=input("Enter number: ")
		if aa=='1' :
			os.system("pkg install git -y")
			os.system("pkg install python2 -y")
			os.system("pkg install python -y")
			os.system("pkg install perl -y")
			os.system("pkg install java -y")
			os.system("pkg install ruby -y")
			os.system("pkg install php -y")
			os.system("pkg install wget -y")
			os.system("pkg install curl -y")
			os.system("pkg install openssh -y")
			os.system("pkg install lolcat -y")
			if __name__ == '__main__':
				main()
		elif aa=='2' :
			print('''
				{1}-git
				{2}-python
				{3}-python3
				{4}-perl
				{5}-java
				{6}-ruby
				{7}-php
				{8}-wget
				{9}-curl
				{10}-openssh
				{00}-Exit
				''')
			bb = input("Enter number from the list: ")
			if bb=='1' :
				os.system("pkg install git -y")
				if __name__ == '__main__':
					main()
			elif bb=='2' :
				os.system("pkg install python -y")
				if __name__ == '__main__':
					main()
			elif bb=='3' :
				os.system("pkg install python2 -y")
				if __name__ == '__main__':
					main()
			elif bb=='4' :
				os.system("pkg install perl -y")
				if __name__ == '__main__':
					main()

			elif bb=='5' :
				os.system("pkg install java -y")
				if __name__ == '__main__':
					main()
			elif bb=='6' :
				os.system("pkg install ruby -y")
				if __name__ == '__main__':
					main()
			elif bb=='7' :
				os.system("pkg install php -y")
				if __name__ == '__main__':
					main()
			elif bb=='8' :
				os.system("pkg install wget -y")
				if __name__ == '__main__':
					main()
			elif bb=='9' :
				os.system("pkg install curl -y")
				if __name__ == '__main__':
					main()
			elif bb=='10' :
				os.system("pkg install openssh -y")
				if __name__ == '__main__':
					main()
			elif bb=='00' :
				if __name__ == '__main__':
					main()
			else:
				if __name__ == '__main__':
					main()
		elif aa=='3' :
			if __name__ == '__main__':
				main()

		else:
			if __name__ == '__main__':
				main()
	elif per=='N' or 'n' :
		webbrowser.get('https://www.youtube.com/channel/UCEKd2l6FS-0iNdC190gxa-w')
		sys.exit([arg])
	else:
		if __name__ == '__main__':
			main()
if __name__ == '__main__':
	main()

    



    

