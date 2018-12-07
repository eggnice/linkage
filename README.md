# Linkage
## 简介
#### &ensp;&ensp;Linkage主要功能是移动云BCOP,BCEC,BCEBS,BCSDN几个系统实现联调,降低系统沟通成本,编写各系统基类满足系统自身业务的自动化运维需求,实现多系统业务巡检,提供上层服务类满足一线二线运维需求。
## 安装
### 1. 构建虚拟环境(可选)
#### &ensp;&ensp;开发者用户推荐，使用pyenv和virtualenv构建纯净的python环境，推荐python版本2.7.10
```Bash
pyenv virtualenv 2.7.10 linkage
pyenv activate linkage
```
### 2. 拉取当前版本
```Bash
git clone http://192.168.182.51/promise/linkage.git
cd linkage
```
### 3. 安装依赖包
```Bash
pip install -r requirements.txt
```
### 4. 安装Linkage
```Bash
python setup.py install
```
## 使用
&ensp;&ensp;Linkage暂时功能是提供各系统自身业务运维自动化入口以及各系统功能模块的互相调用。例：
```Bash
>>>from linkage.op.built import orderserver
>>>test = orderserver.order(orderid)
>>>test.status()

输出用户订单信息
```
## 版本更新记录
```Bash
V1.0.1
实现移动云自动化业务运维的基本场景功能
V1.0.2
修改导入方式和ec代码bug
增加clm包和op的signature
增加性能库配置到op配置文件
修改utils中的wexcel模块
修改去除输出格式
SDN修改端口封堵日志输出
OP优化resourceservice代码
EC修改执行超时问题07/17
OP修改orderservice代码
添加OP的cloudmaster数据库写权限账号-13/10




