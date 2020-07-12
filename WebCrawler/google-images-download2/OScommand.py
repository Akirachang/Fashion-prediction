# Python program to explain os.system() method  
      
# importing os module  
import os  
  
# Command to execute 
# Using Windows OS command 
# cmd = 'python3 bing_scraper.py --search "日系服饰" --limit 10 --download --chromedriver /Users/akirachang/Downloads/chromedriver'
  
# # Using os.system() method 
# os.system(cmd) 

# cmd = 'python3 bing_scraper.py --search "韩系服饰" --limit 10 --download --chromedriver /Users/akirachang/Downloads/chromedriver'

# os.system(cmd) 

cmd = 'python3 bing_scraper.py --search "西方服饰" --limit 10 --download --chromedriver /Users/akirachang/Downloads/chromedriver'

os.system(cmd) 
