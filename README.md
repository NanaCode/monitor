###monitor.conf          配置文件，可以配置绑定ip及端口信息

###monitor.log           日志文件，日志将会输出到这个文件

###cmd/api.py            api服务的启动文件

###api/routers.py        路由文件，这里可以定义url到具体处理方法的映射

###api/controllers.py    这里是url对应的具体的处理方法




#注意：
###这里可以启动一个monitor-api，可以接收http请求，完成启动monitor、关闭monitor、获取monitor数据的操作，具体操作自行编写。

###还需要增加一个在后台周期性获取监控数据并插入数据库的进程，该进程可以通过启动monitor和关闭monitor进行启动和停止控制。

###界面部分则可以通过发送http请求调用这些接口。

###这里没有编写认证的中间件，就是说谁都可以调用，还无法保证安全性。

