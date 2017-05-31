# fuwa

# 1 查询周围的福娃
http://fuwa.hmg66.com/api/queryv2?geohash=102.2301-33.2827&radius=10000&biggest=0
经度－纬度
查询自己周围radius半径远的福娃，单位m
第一次调用biggest = 0
后续调用　取返回near中福娃gid 最后一个数值，比如fuwa_i_2323 则biggest=2323 依次类推

```
message: "OK",
code: 0,
data: {
"far":[ {
geo: "113.300937-23.085474",
pic: "http://wsim.66boss.com/fuwa/brciqydlwvmtnxz.jpg",
pos: "世界纺织博览中心B坐",
video: "",
hider: "100000354",
number: 64,  此处福娃数量
distance: 808.3202,
name: "CHU",
gender: "女",
detail: "测试",
avatar: "https://imgcdn.66boss.com/imagesu/avatar/20170515023034206335.jpeg",
signature: "",
location: "广东 广州市"
}
{
geo: "113.320937-23.185474",
pic: "http://wsim.66boss.com/fuwa/brciqydlwvmtnxz.jpg",
pos: "世界纺织博览中心A坐",
video: "",
hider: "100000354",
number: 22,  此处福娃数量
distance: 808.3202,
name: "CHU",
gender: "女",
detail: "测试",
avatar: "https://imgcdn.66boss.com/imagesu/avatar/20170515023034206335.jpeg",
signature: "",
location: "广东 广州市"
}

]
"near":[{
pic: "http://wsim.66boss.com/fuwa/brciqydlwvmtnxz.jpg",
pos: "珠江国际纺织城",
video: "",
hider: "100000354",
geo: "113.300937-23.085474",
id: "6",
distance: 808.3202,
name: "CHU",
gender: "女",
detail: "测试",
gid: "fuwa_i_2353", ##2353 递减分页每页最多１００个，请求提交最大值，服务器返回数据都比提交的最大值小
avatar: "https://imgcdn.66boss.com/imagesu/avatar/20170515023034206335.jpeg",
signature: "",
location: "广东 广州市"
},

pic: "http://wsim.66boss.com/fuwa/brciqydlwvmtnxz.jpg",
pos: "珠江国际纺织城",
video: "",
hider: "100000354",
geo: "113.300937-23.085474",
id: "64",
distance: 808.3202,
name: "CHU",
gender: "女",
detail: "测试",
gid: "fuwa_i_2349", 
avatar: "https://imgcdn.66boss.com/imagesu/avatar/20170515023034206335.jpeg",
signature: "",
location: "广东 广州市"
},

]
}
}
```
# 1.1 查询周围的缘分
http://fuwa.hmg66.com/api/querystrangerv2?geohash=102.2301-33.2827&radius=10000&biggest=x
经度－纬度
查询自己周围radius半径远的福娃，单位m
第一次调用biggest = 0
后续调用　取返回near中福娃gid 最后一个数值，比如fuwa_i_2323 则biggest=2323 依次类推

```
message: "OK",
code: 0,
data: {
"far":[ {
geo: "113.300937-23.085474",
pic: "http://wsim.66boss.com/fuwa/brciqydlwvmtnxz.jpg",
pos: "世界纺织博览中心B坐",
video: "",
hider: "100000354",
number: 64,  此处福娃数量
distance: 808.3202,
name: "CHU",
gender: "女",
detail: "测试",
avatar: "https://imgcdn.66boss.com/imagesu/avatar/20170515023034206335.jpeg",
signature: "",
location: "广东 广州市"
}
{
geo: "113.320937-23.185474",
pic: "http://wsim.66boss.com/fuwa/brciqydlwvmtnxz.jpg",
pos: "世界纺织博览中心A坐",
video: "",
hider: "100000354",
number: 22,  此处福娃数量
distance: 808.3202,
name: "CHU",
gender: "女",
detail: "测试",
avatar: "https://imgcdn.66boss.com/imagesu/avatar/20170515023034206335.jpeg",
signature: "",
location: "广东 广州市"
}

]
"near":[{
pic: "http://wsim.66boss.com/fuwa/brciqydlwvmtnxz.jpg",
pos: "珠江国际纺织城",
video: "",
hider: "100000354",
geo: "113.300937-23.085474",
id: "6",
distance: 808.3202,
name: "CHU",
gender: "女",
detail: "测试",
gid: "fuwa_i_2353", ##2353 递减分页每页最多１００个，请求提交最大值，服务器返回数据都比提交的最大值小
avatar: "https://imgcdn.66boss.com/imagesu/avatar/20170515023034206335.jpeg",
signature: "",
location: "广东 广州市"
},

pic: "http://wsim.66boss.com/fuwa/brciqydlwvmtnxz.jpg",
pos: "珠江国际纺织城",
video: "",
hider: "100000354",
geo: "113.300937-23.085474",
id: "64",
distance: 808.3202,
name: "CHU",
gender: "女",
detail: "测试",
gid: "fuwa_i_2349", 
avatar: "https://imgcdn.66boss.com/imagesu/avatar/20170515023034206335.jpeg",
signature: "",
location: "广东 广州市"
},

]
}
}
```

# 2.1 查询自己抓到的福娃
http://fuwa.hmg66.com/api/querymy?user=100000076

```
"message": "Ok",
"code": 0,
"data": [
{
   "gid": "fuwa_c_107",
   "id": "11"
   "awarded": false,  #还没有兑奖
   "pos": "广州大酒店",       #位置
   "creator": "雨飞的"
   "creatorid": "100000076"
},
{
   gid: "fuwa_i_119",
   id: "14"
   awarded: false,  #还没有兑奖
   pos: "广州大酒店",       #位置
   creator: "雨飞的"
   "creatorid": "100000076"
},
```
# 2.2 查询自己申请的福娃
http://fuwa.hmg66.com/api/querymyapply?user=100000076

```
"message": "Ok",
"code": 0,
"data": [
{
   "gid": "fuwa_c_107",
   "id": "11"
   "creator": "雨飞的"
},
{
   gid: "fuwa_i_119",
   id: "14"
   creator: "雨飞的"
},
```

# 3 抓福娃　不再使用
POST http://fuwa.hmg66.com/api/capture?user=xxx&gid=xx&sign=xx
gid 是福娃全局ＩＤ
照片ＰＯＳＴ　在body里面name=file

# 3.1 抓福娃
GET http://fuwa.hmg66.com/api/capturev2?user=xxx&gid=xx&sign=xx
gid 是福娃全局ＩＤ
sign 是签名
user=是userid

# 5 藏福娃 
POST http://fuwa.hmg66.com/api/hidev2?owner=xx&detail=店内活动&pos=xx&geohash=102.2-33.22&validtime=1/2/3/4&number=xxx&type=1/0&class=1
owner福娃所有者
pos 福娃位置　比如广州珠江纺织城Ａ区
geohash 经纬度
福娃线索图片采用POST name=file
视频采用POST name=video
detail 福娃活动详情
type=1福娃，０缘分
number 藏福娃数量 （不能多于可用福娃数量,仅申请的福娃可以藏）
class 分类，美食、女装，男装，鞋帽，娱乐，用１，２，３，4，5
如果type=0藏缘分福娃，那么class 设置成i

```
图片为file 视频为video
    <form action='upload' enctype="multipart/form-data" method='post'>
    <input type='file' name='file'/><br/>
    <input type='file' name='video'/><br/>
    <input type='submit' value='submit'/>
    </form>
```

# 7 福娃详情
http://fuwa.hmg66.com/api/querydetail?fuwagid=fuwa_i_110
###当用户停留在背包-福娃详情页面时，需要定时3秒请求接口，刷新
```
{
message: "Ok",
code: 0,
data: {
awarded: false,  #还没有兑奖
pos: "广州大酒店",       #位置
creator: "雨飞的"
}
}
```
# 7.1 福娃活动介绍
http://fuwa.hmg66.com/api/huodong?fuwagid=fuwa_i_110
```
{
message: "Ok",
code: 0,
data: "抢到本次福娃用户，本店消费全场八折"
}
```

# 8 查询出售 
http://fuwa.hmg66.com/msg/querysell

# 8.1 查询我的出售 
http://fuwa.hmg66.com/msg/querymysell?userid=xx

# 9 出售福娃
http://fuwa.hmg66.com/msg/sell?id=xx&owner=xx&amount=x&fuwagid=x&sign=x
id是福娃编号
amount 是售价
fuwagid 是福娃全局标识
sign 签名
sign=md5(/sell?id=xx&owner=xx&amount=x&fuwagid=x&platform=boss66)

# 10 支付系统通知购买成功 
http://fuwa.hmg66.com/msg/notice?orderid=xx&buyer=x&fuwagid=x

# 11 查询我的消息　
http://fuwa.hmg66.com/msg/myinfo?userid=
```
{
    "message": "Ok",
    "code": 0,
    "data": [
   {
     "id"  :   3
     "type": 1   #代表活动推广 ,有url无content 
     "nick": "港棉纺织",
     "snap": "http://a.b.c.d/a.jpg",
     "title": "庆十一友情回馈",
     "url":  "http://a.b.c.d/ina.html"
     "content":  "",
    },
    {
     "id"  :   4
     "type": 0   #代表系统通知 ,有content 无url
     "nick": "我最摔",
     "snap": "http://a.b.c.d/a.jpg",
     "title": "系统通知",
     "content":  "你的福娃被抓取",
     "url": "";
    }

     ]
}
```

# 12 赠送福娃
http://fuwa.hmg66.com/api/donate?token=xx&fuwagid=xx&fromuser=xx&sign=mmm
token = base64(接收福娃用户的id)
fuwagid 要赠送的福娃全局标识
fromuser 赠送人的用户id
sign  签名
sign=md5(/donate?token=xx&fuwagid=xx&fromuser=xx&platform=boss66)

# 13 申请福娃
http://fuwa.hmg66.com/msg/apply?userid=xx&name=xxx&phone=zz&shop=1&purpose=店内活动&region=广州&number=100
userid 用户ＩＤ
name 联系人姓名或公司名
phone 电话
shop 1公司，０个人
purpose 活动说明
region 福娃使用区域
number 申请福娃个数

# 14 扫描福娃，发送奖品，
http://fuwa.hmg66.com/api/award?userid=xx&fuwagid=xx
userid 用户ＩＤ 一般是商家用户ＩＤ ，准确来说是福娃创建者id
fuwagid 福娃ｉｄ

```
{
    "message": "成功", "已兑奖", "你不是福娃所有人"
    "code": 0,1,2  三种可能
}
```


# 15 撤销我的出售
http://fuwa.hmg66.com/msg/cancelsell?orderid=xx&fuwagid=xx&userid=xx


# 16 提现申请
http://fuwa.hmg66.com/msg/money?userid=xx&amount=xx&alipay=xx&name=小啊&sign=xx
userid 用户ID
amount 体现金额
alipay 支付宝帐号
sign 签名
md5(/money?userid=100000076&alipay=22233322x&amount=13&name=%E5%B0%8F%E5%95%8A&platform=boss66)

# 17 查询可用余额
http://fuwa.hmg66.com/msg/querymoney?userid=100000078
userid 用户ID


# 18 增加播放次数
http://fuwa.hmg66.com/api/hit?filemd5=adfefadfcafda&class=1&hash=
filemd5 是视频文件ＭＤ５　校验值。
class 是视频分类1,2,3,4,5, 美食，女装，男装，鞋帽，玩乐，
如果是萌友视频class设置为i
hash 是签名


# 19 查询福娃视频入口则为http://fuwa.hmg66.com/api/queryvideo?geohash=102.2301-33.2827&class=2
class 是分类1,2,3,4,,,,

```
{
   code : 0
   message: "OK",
   data:[
   {
    name: "CHU",
    userid : "10000023",
    gender: "女",
    avatar: "https://imgcdn.66boss.com/imagesu/avatar/20170515023034206335.jpeg",
    video: "http://wsim.66boss.com/avatar/20170.mp4"
    width:1024
    height:768
    filemd5:"3ea31ba3efg1331a398"
    distance: 1000 距离你距离
   },
   {,
    name: "CHU",
    userid : "10000023",
    gender: "女",
    avatar: "https://imgcdn.66boss.com/imagesu/avatar/20170515023034206335.jpeg",
    video: "http://wsim.66boss.com/avatar/20170.mp4"
    width:1024
    height:768
    filemd5:"3ea31ba3efg1331a398"
    distance: 1000 距离你距离
    },

    ]
}
```
# 20 查询特定商家的福娃 ,观看完视频　带我去寻宝接口
http://fuwa.hmg66.com/api/queryv3?geohash=102.2301-33.2827&radius=50000&biggest=0&userid=xx
geohash 经度－纬度
查询商家radius半径远的福娃，单位m 此处应该是视频离你距离一倍，如果视频距离你500M 那么调用这个接口时，radius=1000
第一次调用biggest = 0
后续调用　取返回near中福娃gid 最后一个数值，比如fuwa_c_2323 则biggest=2323 依次类推

```
message: "OK",
code: 0,
data: {
"far":[ {
geo: "113.300937-23.085474",
pic: "http://wsim.66boss.com/fuwa/brciqydlwvmtnxz.jpg",
pos: "世界纺织博览中心B坐",
video: "",
hider: "100000354",
number: 64,  此处福娃数量
distance: 808.3202,
name: "CHU",
gender: "女",
detail: "测试",
avatar: "https://imgcdn.66boss.com/imagesu/avatar/20170515023034206335.jpeg",
signature: "",
location: "广东 广州市"
}
{
geo: "113.320937-23.185474",
pic: "http://wsim.66boss.com/fuwa/brciqydlwvmtnxz.jpg",
pos: "世界纺织博览中心A坐",
video: "",
hider: "100000354",
number: 22,  此处福娃数量
distance: 808.3202,
name: "CHU",
gender: "女",
detail: "测试",
avatar: "https://imgcdn.66boss.com/imagesu/avatar/20170515023034206335.jpeg",
signature: "",
location: "广东 广州市"
}

]
"near":[{
pic: "http://wsim.66boss.com/fuwa/brciqydlwvmtnxz.jpg",
pos: "珠江国际纺织城",
video: "",
hider: "100000354",
geo: "113.300937-23.085474",
id: "6",
distance: 808.3202,
name: "CHU",
gender: "女",
detail: "测试",
gid: "fuwa_i_2353", ##2353 递减分页每页最多１００个，请求提交最大值，服务器返回数据都比提交的最大值小
avatar: "https://imgcdn.66boss.com/imagesu/avatar/20170515023034206335.jpeg",
signature: "",
location: "广东 广州市"
},

pic: "http://wsim.66boss.com/fuwa/brciqydlwvmtnxz.jpg",
pos: "珠江国际纺织城",
video: "",
hider: "100000354",
geo: "113.300937-23.085474",
id: "64",
distance: 808.3202,
name: "CHU",
gender: "女",
detail: "测试",
gid: "fuwa_i_2349", 
avatar: "https://imgcdn.66boss.com/imagesu/avatar/20170515023034206335.jpeg",
signature: "",
location: "广东 广州市"
},

]
}
}
```

# 21 查询盟友视频入口则为http://fuwa.hmg66.com/api/querystrvideo?geohash=102.2301-33.2827
同上 19
区别在于没有分类

# 22 查询特定用户的福娃 ,观看完视频　带我去寻宝接口
http://fuwa.hmg66.com/api/querystrangev3?geohash=102.2301-33.2827&radius=50000&biggest=0&userid=xx
同20 一直
geohash 经度－纬度
查询特定用户radius半径远的福娃，单位m 此处应该是固定值，比如50000 50KM 一个城市的距离
第一次调用biggest = 0
后续调用　取返回near中福娃gid 最后一个数值，比如fuwa_i_2323 则biggest=2323 依次类推

# 23 查询分类
http://fuwa.hmg66.com/api/queryclass
```
{
   code : 0
   message: "OK",
   data:[
   {name:"美食", enum:"1"},
   {name:"女装", enum:"2"},
   {name:"男装", enum:"3"},
   {name:"鞋帽", enum:"4"},
   {name:"玩乐", enum:"5"},
   ]
}
```

# 关于签名 
只对抓福娃ＵＲＬ　签名，其余不要求
每个url后面都有 sign=xxx 签名计算方法是对uri&platform=boss66 进行md5
uri 是这个地址串 不含sign=
举个例子：
http://localhost:1688/capture?user=john&gid=fuwa_6&sign=7ad54cafb52668e4264320c3145c6422
md5(/capture?user=john&gid=fuwa_6&platform=boss66)
结果：
7ad54cafb52668e4264320c3145c6422

## 二维码格式
第一种       fuwa:fuwa:fuwa_c_123                      
第二种       fuwa:user:AEjOkadJMKaGK 
                        
前边是福娃的二维码， 后面是福娃赠送接收用户口令二维码

## 数据库：
globalid  是全局ID，逐渐递增

fuwa_i_xxxx 是找缘分福娃的全局标识,xxxx是数字，hash 类型
"name":创建者昵称
"creator" 创建者用户id
"pos" 藏的地理位置信息，比如广州珠江
"awarded" 是否已兑奖
"owner" 当前所有人id
"id" 福娃编号


fuwa_c_xxxx 是寻宝福娃的全局标识,xxxx是数字，hash 类型
"name":创建者昵称
"creator" 创建者用户id
"pos" 藏的地理位置信息，比如广州珠江
"awarded" 是否已兑奖
"owner" 当前所有人id
"id" 福娃编号

xxxxxx_pack 是用户捕获到的福娃列表,比如:100000076_pack ，集合类型
xxxxxx_apply是用户申请的福娃列表,比如:100000076_apply ，集合类型


fuwa_i 是缘分福娃GEO地理位置信息
fuwa_i 是寻宝福娃GEO地理位置信息

============个人笔记用，By Rain================
video_g_1 美食
video_g_2 女装 
video_g_3 男装
video_g_4 鞋帽
video_g_5 玩乐
寻宝视频地理位置坐标
video_g_i 盟友视频地理位置坐标

filemd5{
name:
gender:
avatar:
userid:
video:
width:1024
height:768
}
有序集合
　美食　video_1 filemd5 播放次数
　女装　video_2 filemd5  播放次数
　男装　video_3 filemd5 播放次数
　鞋帽　video_4 filemd5 播放次数
　玩乐　video_5 filemd5 播放次数

盟友　　video_i filemd5 播放次数
　
推荐算法　前十名最热视频，优先返回，geodistance 求距离，
然后再按距离运近推荐 georadius withdistance asc

