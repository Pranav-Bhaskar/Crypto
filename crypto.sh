#!/bin/bash
echo "+================================================+";
echo "|---------------------ABOUT----------------------|";
echo "+================================================+";
echo "|---THIS TOOL HAS BEEN MADE BY PRANAV BHASKAR.---|"; 
echo "|--IF YOU ARE NOT HIM BETTER STAY AWAY FROM IT.--|";
echo "+================================================+";
echo "|---THIS TOOL WAS MADE FOR EDUCATIONAL PURPOSE---|";
echo "|ONLY AND IF MISSUSED IT IS NOT HIS RESPONSIBIITY|";
echo "+================================================+";
echo "";
echo "+================================================+";
echo "|--------------------CREDITS---------------------|";
echo "+================================================+";
echo "|------E-MAIL = [pranavbhaskar23@gmail.com]------|";
echo "+================================================+";
echo "|FB = [www.fb.com/profile.php?id=100006318544877]|";
echo "+================================================+";
echo "|--GITHUB = [https://github.com/Pranav-Bhaskar]--|";
echo "+================================================+";
echo "";
echo "+===================================================+";
echo "|----------------IMPORTANT NOTE---------------------|";
echo "+===================================================+";
echo "|CHANGING THE CREDITS WILL NOT MAKE YOU THE DEVLOPER|";
echo "+===================================================+";
echo "";
echo "";
echo "Is this the FIRST TIME (Y/N) : ";
read varN
if [ $varN == 'Y' ] || [ $varN == 'y' ]
then
	echo "";
	echo "+================================================+";
	echo "|-------------Installing Python 3.X--------------|";
	echo "+================================================+";
	echo "";
	sudo apt install python3
	echo "";
	
fi
echo "";
echo "+================================================+";
echo "|--------YOU CAN NOW BEGIN WITH THE HACK---------|";
echo "+================================================+";
echo "";
fla='0';
while [ $fla == '0' ]; do
	echo "DO YOU WANT TO ENCRYPT OR DECRYPT? (E/D) : ";
	read var
	if [ $var == 'E' ] || [ $var == 'e' ]
	then
		echo "YOU CHOSE TO ENCRYPT.";
		fla='1';
		flag='1';
		echo "ENTER THE KEY : ";
		read key
		while [ $flag == '1' ]; do
			echo "Enter the directory of the file : ";
			read file_dir
			if [[ -f $file_dir ]]
			then 
				flag='0';
			fi
		done
		python3 encrypto.py $file_dir $key;
		echo "The file can be found in the file $file_dir.encrypto";
	elif [ $var == 'D' ] || [ $var == 'd' ]
	then
		fla='1';
		flag='1';
		echo "YOU CHOSE TO DECRYPT.";
		echo "ENTER THE KEY : ";
		read key
		while [ $flag == '1' ]; do
			echo "Enter the directory of the file : ";
			read file_dir
			if [[ -f $file_dir ]]
			then 
				flag='0';
			fi
		done
		python3 decrypto.py $file_dir $key;
		echo "The file can be found in the file $file_dir.decrypto";
	fi
done
echo "+================================================+";
echo "|----------------HAPPY CRYPTING------------------|";
echo "+================================================+";
