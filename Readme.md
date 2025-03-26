<!-- <link rel="stylesheet" type="text/css" href="readme.css" /> -->

# 控制器测试用例

## HTTP API 测试

### 测试环境
* 运行测试的主机具备wifi硬件
* 配器控制器1个、采集器1个、回风温度1个、环境温度1个、人体模块1个
* 子设备已连接至控制器

### 测试方法
1. 子设备上电
1. 开启控制器AP
1. 执行测试用例
    * 测试用例中，控制器 http api 测试使用 mark: http_api_itower_controller
    * 通过wifi连接之控制器的AP
    * 逐一发送http 请求，请求url http://192.168.20.1 
    * 解析、验证响应值

## 控制器内存测试
### 测试方法
