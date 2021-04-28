import subprocess

result = subprocess.run(['fortune'], stdout=subprocess.PIPE)

print(result.stdout)
