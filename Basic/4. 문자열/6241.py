url = "http://www.example.com/test?p=1&q=2"

protocol_str= "://"
protocol = url.split(protocol_str)[0]

host_str= "/"
index = url.find(protocol_str)
index_end = url.rfind(host_str)

host = url[index+len(protocol_str):index_end]
others = url[index_end+1:]

print(f"protocol: {protocol}")
print(f"host: {host}")
print(f"others: {others}")


