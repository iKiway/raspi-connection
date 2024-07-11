import subprocess
ls_output = subprocess.check_output(f"python ted.py", universal_newlines=True)
print(ls_output)