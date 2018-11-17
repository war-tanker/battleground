import subprocess

def terminal(command):
    output = subprocess.Popen(command.split(' '), stdout=subprocess.PIPE).communicate()[0]
    return output.decode().strip()
