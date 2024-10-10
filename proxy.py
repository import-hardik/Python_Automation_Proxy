import subprocess

def get_ssid():
    try:
        # Use the nmcli command to get the SSID of the active connection
        result = subprocess.run(['nmcli', '-t', '-f', 'active,ssid', 'dev', 'wifi'], 
                                stdout=subprocess.PIPE, text=True)
        
        for line in result.stdout.splitlines():
            if line.startswith("yes"):
                ssid = line.split(":")[1]
                return ssid
        return "Not connected to any WiFi network."
    
    except Exception as e:
        return f"An error occurred: {e}"

def run_command(command):
    try:
        result = subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        
        # Output the result
        if result.stderr:
            print("Error Output:\n", result.stderr)
            
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while running the command: {e}")


# Print the SSID
if get_ssid()=="HCST_Mathura":
    run_command("gsettings set org.gnome.system.proxy mode 'manual'")
else:
    run_command("gsettings set org.gnome.system.proxy mode 'auto'")
print("Proxy Updated")
