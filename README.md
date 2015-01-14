tornado在线代理谷歌
==============
__配置文件__
--------
> [proxy]
>  host = www.google.com.sg # 我的服务器新加坡，所以我代理的是sg。
>  port = 443                                                                                           
>  protocol = https
>  js = js.js   # 指定js的文件，文件内容会被添加到html内容的最后面，可以用来修改页面元素
>  cookies = PREF=ID=047808f19f6de346:U=0f62f33dd8549d11:FF=2:LD=zh-CN:NW=1:TM=1325338577:LM=1332142444:GM=1:SG=2:S=rE0SyJh2w1IQ-Maw # 设置cookies，这里的cookie表示语言是zh-cn，在新窗口中打开。

__运行代理__
> python run.py

__用nginx来反向代理它__
> 
upstream proxy_google{                                                                                                                  
    server 127.0.0.1:1111;
}
server {
    listen 80; 
    server_name g.tuxpy.info;
    rewrite ^(.*)$ https://g.tuxpy.info$1 permanent;
}
server{
    listen 443;
    server_name g.tuxpy.info;
    ssl on; 
    ssl_certificate /home/www/1_g.tuxpy.info_bundle.crt;
    ssl_certificate_key /home/www/2_g.tuxpy.info.key;
    location /{
        proxy_pass_header Server;
        proxy_set_header Host \$http_host;
        proxy_redirect off;
        proxy_set_header X-Real-IP \$remote_addr;
        proxy_set_header X-Scheme \$scheme;
        proxy_pass http://proxy_google;
        }   
}
