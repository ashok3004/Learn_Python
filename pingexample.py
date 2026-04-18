import subprocess
host='www.facebook.com'
result=subprocess.run(['ping','-c','4',host],capture_output=True,text=True)
print("ping result for the {host}:\n ", result.stdout)
with open('output.txt','w') as fo:
    subprocess.run(['ping','-c','4',host],stdout=fo)
    print("output of result is stored successfully")