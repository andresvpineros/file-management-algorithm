filename = 'allowed_list.txt'
remove_list = ["192.168.97.225", "192.168.158.170", "192.168.201.40", "192.168.58.57"]

def read_file(filename):
    with open(filename, 'r') as file:
        return file.read()

def update_file(filename, new_list):
    with open(filename, 'w') as file:
        file.write(list_to_text(new_list))

def text_to_list(text):
    return text.split('\n')

def list_to_text(list):
    return "\n".join(list)

# Open the file and read its contents, next save into the variable allowed_ip_addresses as a list
allowed_ip_addresses = text_to_list(read_file(filename))

# Iterate through the list and validate each one if is on the remove list and remove it
for ip in allowed_ip_addresses:
    if ip in remove_list:
        allowed_ip_addresses.remove(ip)

# Update the file with the new changes in the list
update_file(filename, allowed_ip_addresses)

# Print the updated file
print(read_file(filename))