import requests as req

print("Welcome to IsItdown.py! \n"
      "Please write a URL or URLs you want to check. (seperated by comma)")

url_list = input().split()
print(url_list)

for i in range(len(url_list)-1):
    if url_list[i] == ',':
        print(i)
        url_list.pop(i)

print(url_list)