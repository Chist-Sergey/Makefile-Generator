# Setup  

## Step 1.  

Pick up the version you want to run.  
There is a short summary of every available version:  

VERSION                 PROS                                CONS  
1.0                       simple code &             limited combinations  
                            readable result          (ex: "v", "vi")  

1.1                        still simple &               lacks double   combination  
                             readable result         (ex: "v", "vig",   but not "vi")

2.0                       all combinations         hard coded  
                             are included                the result is hard to read  
                             (ex: "v", "vi", "vig")  

3.0                       readable result &        exponentially slow  
                            combinations may      by n! / (n - r)!  
                            be exteded

## Step 2.  

Go to the file and download it raw, or you can download   it directly via Terminal/Console with cURL/Wget.

**Tip: replace the version number to your desired version**

Manual: https://github.com/Chist-Sergey/Makefile-Generator/blob/master/src/genmakefile-v1.0.py

cURL: curl -LJO https://raw.githubusercontent.com/Chist-Sergey/Makefile-Generator/main/src/genmakefile-v1.0.py

RHEL7.6: wget https://raw.githubusercontent.com/Chist-Sergey/Makefile-Generator/main/src/genmakefile-v1.0.py --output-document=genmakefile.py

## Step 3 (optional).
See "[extra.md](./extra.md)".  

# This is it.  

See "[usage.md](./usage.md)" next.  

