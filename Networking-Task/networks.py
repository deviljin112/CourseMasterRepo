from ipaddress import ip_interface

print("-=Network Checker=-")

print("Please insert the first IP Address")
print("Format: X.X.X.X/Y")
first = input("=> ")

print("Please input the second IP Address")
print("Format: X.X.X.X/Y")
second = input("=> ")

ip_1 = ip_interface(first)
ip_2 = ip_interface(second)


ans = ip_2.network.overlaps(ip_1.network)

if ans:
    print("These IPs are on the same network.")
else:
    print("These IPs are NOT on the same network.")


# TEST MATERIAL
# 192.168.200.5/30 and 192.168.200.9/30 == FALSE
# 192.168.200.5/30 and 192.168.200.6/30 == TRUE