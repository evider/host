import socket

# 定义要查询的域名列表
domains = [
    "www.google.com",
    "www.facebook.com",
    "www.example.com",
    "github.com",
    "gist.github.com",
    "assets-cdn.github.com",
    "raw.githubusercontent.com",
    "gist.githubusercontent.com",
    "cloud.githubusercontent.com",
    "camo.githubusercontent.com",
    "avatars0.githubusercontent.com",
    "avatars1.githubusercontent.com",
    "avatars2.githubusercontent.com",
    "avatars3.githubusercontent.com",
    "avatars4.githubusercontent.com",
    "avatars5.githubusercontent.com",
    "avatars6.githubusercontent.com",
    "avatars7.githubusercontent.com",
    "avatars8.githubusercontent.com",
    "mail.google.com",
    "inbox.google.com",
    "accounts.google.com",
    "contacts.google.com",
    "groups.google.com",
    "calendar.google.com",
    "drive.google.com",
    "docs.google.com",
    "sheets.google.com",
    "slides.google.com",
    "oldj.github.io"
]

# 创建一个空的hosts文件内容字符串
hosts_content = ""

# 遍历GitHub域名列表进行查询
for domain in domains:
    try:
        ip_address = socket.gethostbyname(domain)
        # 将查询到的IP地址与域名添加到hosts文件内容字符串中
        hosts_content += f"{ip_address} {domain}\n"
    except socket.gaierror:
        print(f"无法解析域名：{domain}")

# 将hosts文件内容写入文件
with open("hosts", "w") as file:
    file.write(hosts_content)
    print("hosts文件已生成")


