# use_cloudflare_cdn_web_site_list

本项目手机使用cloudflare加速的一些网站，欢迎增加补充。

# 使用方法

1. 使用[better-cloudflare-ip](https://github.com/badafans/better-cloudflare-ip)或[CloudflareSpeedTest](https://github.com/XIU2/CloudflareSpeedTest)筛选出当前网络下最优的cloudflare主机ip
2. 然后使用本项目脚本update_host.py

```bash
python update_host.py --ip=x.x.x.x --domain=use_cloudflare_domain_list.txt
```
产生host文件

3. 使用[SwitchHost](https://github.com/oldj/SwitchHosts)工具设置host文件

深圳电信用户也可以使用本项目提供的两个host(host目录下)文件，使用SwitchHost添加远程host连接即可，两个文件为作者深圳电信网络自用，会不定时更新。
