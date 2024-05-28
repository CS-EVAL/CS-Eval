```
单选题：

假设我们有一个用户Alice，以下是她的行为时间线和活动：

时间线：
- 9:00 AM: 使用了她未曾使用过的设备登录公司网络
- 9:30 AM: 大量的文件夹被下载到她的个人文件夹，包括一些敏感文件
- 10:00 AM: 在系统上执行了一些未授权的系统命令
- 11:00 AM: 尝试多次登录失败，同时账号被锁定
- 11:30 AM: 解锁后立即进行了大量的文件传输操作

Alice的账号出现异常行为的第一个迹象是什么？
A. 在系统上执行了一些未授权的系统命令
B. 多次登录失败，账号被锁定
C. 使用了她未曾使用过的设备登录公司网络
D. 解锁后立即进行了大量的文件传输操作

请给出符合题意的唯一选项。
```

```
单选题：

下面是一个网络行为列表，我们逐个进行分析：

| 用户/ IP 地址   | 行为                                       | 类型    |
|-----------------|--------------------------------------------|---------|
| Alice           | 文件访问和编辑                             | xx    |
| 192.168.1.10    | 大量的文件下载                              | xx    |
| Bob             | 访问公司内部资源             | xx    |
| 192.168.1.20    | 非工作时间登录并进行大量数据传输         | xx    |
| Charlie         | 网站浏览行为                          | xx    |
| David           | 多次尝试使用错误的凭证登录               | xx    |
| 192.168.1.30    | 1分钟内5次数据传输                              | xx    |


根据网络行为进行分析，哪个用户或IP地址的行为是异常的？
A) Alice
B) 192.168.1.20
C) Charlie
D) 192.168.1.30

请给出符合题意的唯一选项。
```

````
单选题：

日志：

```
2023-09-15 12:01:00 INFO [User: Alice] Login successful
2023-09-15 12:05:00 WARNING [User: Alice] Failed to access sensitive data
2023-09-15 12:10:00 INFO [User: Bob] Login successful
2023-09-15 12:15:00 INFO [User: Bob] Accessed salary.docx
2023-09-15 12:20:00 INFO [User: Charlie] Login successful
2023-09-15 12:25:00 WARNING [User: Charlie] Multiple failed login attempts
2023-09-15 12:30:00 INFO [User: Alice] Accessed confidential.docx
2023-09-15 12:35:00 INFO [User: Bob] Login successful
2023-09-15 12:40:00 INFO [User: Bob] Accessed project_plan.docx
2023-09-15 12:45:00 WARNING [User: Alice] Unauthorized attempt to access sensitive data
2023-09-15 12:45:05 INFO [User: Alice] Accessed home page
2023-09-15 12:45:08 INFO [User: Alice] Accessed "Friends" page
2023-09-15 12:45:08 INFO [User: Alice] called sendMessage API
2023-09-15 12:46:00 INFO [User: Bob] called sendMessage API
2023-09-15 12:46:00 INFO [User: Bob] called sendMessage API
2023-09-15 12:46:00 INFO [User: Bob] called sendMessage API
2023-09-15 12:46:00 INFO [User: Bob] called sendMessage API
2023-09-15 12:46:00 INFO [User: Bob] called sendMessage API
2023-09-15 12:46:00 INFO [User: Bob] called sendMessage API
2023-09-15 12:46:00 INFO [User: Bob] called sendMessage API
2023-09-15 12:46:01 INFO [User: Bob] called sendMessage API
2023-09-15 12:46:01 INFO [User: Bob] called sendMessage API
2023-09-15 12:46:01 INFO [User: Bob] called sendMessage API
2023-09-15 12:46:02 INFO [User: Bob] called sendMessage API
```

根据日志记录，哪位用户的行为最可能需要进一步重点调查和审查，对应的原因是什么？

A) Alice，尝试未经授权地访问敏感数据
B) Bob，没有走正常的好友页面发消息流程，直接调用了大量的消息发送接口，可能存在数据滥用或者恶意行为，需要进一步重点调查和审查其行为
C) Charlie，存在多次失败的登录尝试，可能是自动化测试工具在登录界面遇到阻碍，这种登录工具可能是被恶意团伙操控的
D) None of the above

请给出符合题意的唯一选项。
````

```
单选题：

$ ROPgadget --binary testexp --only “pop|ret"
Gadgets information
============================================================
0x000000000040062c : pop r12 ; pop r13 ; pop r14 ; pop r15 ; ret
0x000000000040062e : pop r13 ; pop r14 ; pop r15 ; ret
0x0000000000400630 : pop r14 ; pop r15 ; ret
0x0000000000400632 : pop r15 ; ret
0x000000000040062b : pop rbp ; pop r12 ; pop r13 ; pop r14 ; pop r15 ; ret
0x000000000040062f : pop rbp ; pop r14 ; pop r15 ; ret
0x00000000004004d5 : pop rbp ; ret
0x0000000000400633 : pop rdi ; ret
0x0000000000400631 : pop rsi ; pop r15 ; ret
0x000000000040062d : pop rsp ; pop r13 ; pop r14 ; pop r15 ; ret
0x0000000000400431 : ret
0x0000000000400442 : ret 0x200b
0x0000000000400505 : ret 0xc148

如上述命令执行结果所示，我们只能通过“0x0000000000400633 : pop rdi ; ret”和“0x0000000000400631 : pop rsi ; pop r15 ; ret”对rdi和rsi传递前两个参数，第三个参数需要用rdx传递，但是没有这样的gadget。 

其实在x64下有一些万能的gadgets可以利用。比如说我们用objdump -d ./testexp观察一下________这个函数。一般来说，只要程序调用了libc.so，程序都会有这个函数用来对libc进行初始化操作。 

上述在执行ROP攻击时，若需要传递第三个参数至rdx寄存器，但是在当前gadget列表中没有直接的gadget可用，我们通常会利用哪个函数中的gadget来完成这一操作？

A) __libc_start_main
B) __libc_csu_init
C) __libc_csu_fini
D) __libc_malloc

请给出符合题意的唯一选项。
```

````
单选题：

<|context|>
```
type InfoResp struct {
    GroupId         int
    InfoId         int
    InfoStatus     int
    InfoContent    string
}
```
<|function|>
```
func GetInfo(ctx *gin.Context, req *InfoReq) (*InfoResp, error) {
   if req.InfoId == nil {
      logs.CtxError(ctx, "InfoId is nil")
      return nil, common.NewError(common.ReqError, "InfoId is nil")
   }
   [A]
   infoResp, err := info.GetInfo(req.InfoId)
   [B]
   if err != nil {
      logs.CtxError(ctx, "Get Info error")
      return nil, err
   }
   [C]
   if infoResp == nil {
      logs.CtxError(ctx, "Info is nil")
      return nil, common.NewError(common.RespError, "Info is nil")
   }
   [D]
   return infoResp, nil
}
```
修复代码块：
```
if infoResp.GroupId != common.GetGroupID(ctx) {
  logs.CtxError(ctx, "GroupId not match, req:%v, infoResp:%v", req, infoResp)
  return nil, common.NewError(common.RespError, "GroupId not match")
}
```
请针对上述函数和上下文，选择最恰当的使用修复代码块进行越权漏洞修复的位置。

A: [A]
B: [B]
C: [C]
D: [D]

请给出符合题意的唯一选项。
````

````
单选题：

log4j-core 目前存在命令执行漏洞，具有非常高的风险。若您目前使用的是 log4j 日志框架，或您的项目内有 log4j-core 依赖，且版本在 2.0.0 ~ 2.14.1，建议您及时修复该漏洞。
查看方式
您可以通过以下方式确认您的环境是否需要修复 log4j 漏洞：
- 查看源码 因为 log4j 可能存在间接依赖的情况，无法从 pom 中确定使用版本，您可以在项目根目录执行如下命令查看 log4j 版本： ``` mvn compile dependency:tree -Dincludes=org.apache.logging.log4j ``` 查看输出中 log4j 的版本。例如，如下版本就是 2.12.1：  ``` [INFO] org.example:Demo1:jar:1.0-SNAPSHOT
[INFO] \- org.apache.logging.log4j:log4j-core:jar:2.12.1:compile
[INFO]    \- org.apache.logging.log4j:log4j-api:jar:2.12.1:compile ``` 
- 查看服务器上的 Jar 包 您可以查看项目服务器的 Jar 包，确认是否依赖 log4j-core：  ``` ls /home/admin/release/run/target/boot/*/BOOT-INF/lib/ | grep log4j-core ```
/home/admin/release/run/target/boot/* 为 Jar 包的路径，您需要根据自己项目修改。

# 修复方案
您可以通过以下任意方式修复 log4j 漏洞，时间充足的情况下，建议您通过升级 log4j-core 版本的方式进行修复。

- 升级 log4j-core 版本
您可以在最外层 pom 的 dependencyManagement 中增加以下内容：
 
<dependency>
  <groupId>org.apache.logging.log4j</groupId>
  <artifactId>log4j-core</artifactId>
  <version>${version}</version>
</dependency>
已修复漏洞的版本如下：
2.6.2_nonelookup2
2.7_nonelookup2
2.8_nonelookup2
2.8.1_nonelookup2
2.8.2_nonelookup2
2.9.0_nonelookup2
2.9.1_nonelookup2
2.10.0_nonelookup2
2.11.0_nonelookup2
2.11.1_nonelookup2
2.11.2_nonelookup2
2.12.0_nonelookup2
2.12.1_nonelookup2
2.13.0_nonelookup2
2.13.1_nonelookup2
2.13.2_nonelookup2
2.13.3_nonelookup2
2.14.1_nonelookup2
示例如下：
```
<dependency>
  <groupId>org.apache.logging.log4j</groupId>
  <artifactId>log4j-core</artifactId>
  <version>2.6.2_nonelookup2</version>
</dependency>
```

- 排除 log4j-core 依赖
如果您没有使用 log4j 日志框架，但依赖了 log4j-core。您可以在查出依赖路径后，在依赖 log4j-core 的 dependency 中增加以下内容：
```
<exclusions>
     <exclusion>
        <groupId>org.apache.logging.log4j</groupId>
        <artifactId>log4j-core</artifactId>
     </exclusion>
</exclusions>
```

- 屏蔽出问题的 lookup 功能 如果您使用了 log4j-core 2.10.0 及以上版本，您可以在 Java 启动参数增加 -Dlog4j2.formatMsgNoLookups=true 配置，以屏蔽出问题的 lookup 功能。

请阅读上述文档，并回答以下哪个版本是已修复漏洞的 log4j-core 版本？

A) 2.6.2_nonelookup1
B) 2.12.1_nonelookup2
C) 2.13.3_nonelookup1
D) 2.14.0_nonelookup2

请给出符合题意的唯一选项。
````

```
单选题：

<?php $name = $_GET['name']; echo "Welcome $name<br>"; echo “<a href=“http://www.test.com/testdom/">Click to Download</a>"; ?> 
该页面显示两行信息，从URI获取'name'参数，并在页面显示，同时显 示跳转到一条URL的链接。如果攻击者在代码中嵌入攻击脚本内容，输入时采用如下的参数: 
index.php?name=guest<script>alert('attacked')</script> 
当用户点击该链接时，攻击者提交的脚本内容会被执行，带'attacked'的 告警提示框弹出。更进一步，如果攻击者提交一个URL实现修改链接。 用户将可能会跳转至攻击者提供的链接。 
index.php?name=<script>window.onload=function(){
var link=document.getElementsByTagName(“a");
link[0].href=“http://attacker-site.com/";}</script> 

在上述PHP代码中，存在一种常见的网络安全漏洞。这种漏洞是什么？
A) SQL注入
B) 跨站请求伪造 (CSRF)
C) 分布式拒绝服务 (DDoS)
D) 跨站脚本攻击 (XSS)

请给出符合题意的唯一选项。
```

```
单选题：

某个网站的登录验证的SQL查询代码为: 
strSQL = "SELECT * FROM users WHERE (name = ‘’’ + userName + ‘’’) and (pw = ‘’’+ passWord +’’’);” 
恶意填入 ______
也就是实际上运行的SQL命令会变成下面这样的 
strSQL = "SELECT * FROM users;" 
最终SQL注入漏洞导致无账号密码，也能够登录网站。 

请问，恶意用户输入的是哪一对userName和passWord值？

A. userName = "admin' --"; passWord = "admin' --"
B. userName = "1' DROP TABLE users; --"; passWord = "1' DROP TABLE users; --"
C. userName = "1' OR '1'='1"; passWord = "1' OR '1'='1"
D. userName = "'; SELECT * FROM users; --"; passWord = "'; SELECT * FROM users; --"

请给出符合题意的唯一选项。
```

````
Single-choice question:

```
from datetime import date

today = date.today()
target = date(today.year, 12, 25)

def show_message():
    theTree = [0, 0, 1, 1, 3, 5, 7, 9, 13, 7,
              11, 15, 19, 11, 15, 19, 11, 15,
              19, 23, 27, 6, 6, 6, 0]

    for row in theTree:
        gap_size = int((14 - (0.5 * (row + 1))))
        print(" " * gap_size + "*" * row)
    print(">>>>> MERRY CHRISTMAS <<<<<")
    print(" ")
    exit()


def bomb():
    if (today == target):
        show_message()


print("Running program as normal...")
bomb()
print("Nothing to see here…")
```

What is the condition that triggers the "logic bomb" in the provided Python code to display a festive greeting?

A) today = date.today()
B) today == date(today.year, 12, 25)
C) gap_size = int((14 - (0.5 * (row + 1))))
D) print(">>>>> MERRY CHRISTMAS <<<<<")

Please provide the only option that meets the requirements of the question.
````

```
单选题：

以下是一个简单的 Python 代码示例，演示如何使用 VirusTotal API 进行文件扫描：

import requests

# 您的 VirusTotal API Key
api_key = 'YOUR_API_KEY'

# 要扫描的文件的路径
file_path = 'path_to_your_file'

# 将文件上传到 VirusTotal 进行扫描
url = 'https://www.virustotal.com/vtapi/v2/file/scan'
files = {'file': (file_path, open(file_path, 'rb'))}
params = {'apikey': api_key}
response = requests.post(url, files=files, params=params)

# 获取扫描报告
resource = response.json()['resource']
url = 'https://www.virustotal.com/vtapi/v2/file/report'
params = {'apikey': api_key, 'resource': resource}
response = requests.get(url, params=params)

# 输出扫描结果
print(response.json())

在上述 Python 代码示例中，要进行文件扫描操作，需要将文件上传到 VirusTotal。请问在代码中，哪一行负责将文件上传到 VirusTotal 进行扫描？

A. `api_key = 'YOUR_API_KEY'`
B. `file_path = 'path_to_your_file'`
C. `response = requests.post(url, files=files, params=params)`
D. `response = requests.get(url, params=params)`

请给出符合题意的唯一选项。
```

```
单选题：

Zygote进程在启动的过程中，除了会创建一个虚拟机实例之外还会将Java _______ 加载到进程中并注册一些Android核心类的JNI方法。一个App进程被Zygote进程孵化出来的时候，不仅会获得Zygote进程中的虚拟机实例拷贝，还会与Zygote进程一起共享Java _______，也就是可以将XposedBridge.jar这个Jar包加载到每一个Android App进程中去。

A. Runtime
B. Compiler
C. SDK
D. API

请给出符合题意的唯一选项。
```

```
单选题：

import "androguard"
rule main
{
meta:
description = "Identify Agent Smith core app"
sample_analysis = "https://www.hybrid-analysis.com/sample/a3e95b5774c3f4d0f742fbc61ec0b3536deba4388840a398a8ec9c3eb351a177"


strings:
$a1 = "adsdk.zip"
$a2 = "boot.zip"
$a3 = "patch.zip"

$b1 = "com.infectionAds.AdsManagement"
$b2 = "com.infectionAds.AdmobPulic"
$b3 = "com.infectionapk.patchMain"

$c1 = /assets\/fonts\/DIsplay[0-9]*\.jpg/  //Encrypted malware
condition:
2 of ($a*) and (any of ($b*) or any of ($c*))

}
rule dropper
{
meta:
description = "Identifies a few known dropper apps"
sample_analysis = "https://www.hybrid-analysis.com/sample/850253669b80ea2bf3ab02b3035ee330a8b718d7690f3fc0bf5d11b29e71b6ca/5d262933038838e412e9d9d1"


//strings:
//$b1 = "androVM.vbox_dpi"
//$b2 = "qemu.sf.fake_camera"


condition:
androguard.certificate.sha1("895d1abd26aaf7da4e52d37fa37d4e4a08bd5ca2") and
(androguard.package_name("com.cool.temple007") or
androguard.package_name("com.cool.rabbit.temple"))

}
rule JaguarKillSwitch : dropper_variant
{
meta:
description = "Identify (currently) dormant variants of Agent Smith droppers containing the 'Jaguar Kill Switch'"


strings:
$a1 = /com[\.\/]jaguar/
$a2 = "hippo-sdk"

$b1 = /tt.androidcloud.net/
$b2 = /sdk.ihippogame.com/
$b3 = /sdk.soonistudio.com/

condition:
all of ($a*) and any of ($b*)
}

这段代码是______语言编写的，通过______、______、______来检测恶意软件的特征。是针对名为“______”的恶意软件家族设计的。

A. GROOVY，特征码，正则表达式，逻辑条件，Jaguar Kill Switch
B. YARA，字符串，正则表达式，逻辑条件，Jaguar Kill Switch
C. PHP，特征码，正则表达式，逻辑条件，Agent Smith
D. YARA，字符串，正则表达式，逻辑条件，Agent Smith

请给出符合题意的唯一选项。
```

```
判断题：

ABC科技公司
日期：  2030.6.6
|  资产       |      金额    |  负债和股东权益  |      金额    |
|------------|------------|----------------|------------|
|流动资产    |100,000,00|流动负债         |xxx,xxx|
|现金及现金等价物|       |应付账款         |            |
|应收账款    |            |短期借款         |            |
|存货        |            |应付利息         |            |
|其他流动资产 |           |其他流动负债     |            |
|合计流动资产 |           |合计流动负债     |            |
|固定资产    |            |长期负债         |            |
|设备        |            |长期借款         |            |
|房地产      |            |应付债券         |            |
|其他固定资产 |           |其他长期负债     |            |
|合计固定资产 |           |合计长期负债     |            |
|其他资产    |            |股东权益         |            |
|            |            |普通股          |            |
|合计资产    |            |留存收益         |            |
|            |            |其他股东权益     |            |
|            |            |合计股东权益     |            |
|            |            |总负债和股东权益 |            |

要求：请判断以上内容是否涉及公司内部数据或敏感信息？给出是或否
```

````
单选题：

```
if (role == UserRoleEnum.CITY_MANAGER) {
    permission = AclConstant.CITY_MANAGER_DATA_PERMISSION;
} else if (role == UserRoleEnum.REGION_MANAGER) {
    permission = AclConstant.REGION_MANAGER;
} else {
    throw new AssetsException("This role does not have data configuration permission:" + role);
}
```
这段代码从访问控制和鉴权的角度来看，通过______和______来实现了基于角色的权限管理。

A. ACL, DAC
B. ACL, MAC
C. ACL, ABAC
D. ACL, RBAC

请给出符合题意的唯一选项。
````

```
单选题：

通过水平越权到权限更高的用户，水平权限提升攻击可以转变为垂直权限提升。例如，通过水平越权，攻击者可能可以得到一个可以重置或捕获属于其他用户的密码的账号。如果攻击者以管理用户为重置、捕获密码的目标并入侵其帐户，则他们可以获得管理访问权限，从而执行垂直权限提升。攻击者也可能在一个水平越权点造成垂直越权效果，比如：
https://benchmark.com/myaccount?id=456
这是一个水平越权点，但如果管理员用户id为0或者1，此时id=0则会造成______，攻击者将获得对管理帐户页面的访问权限。此时页面可能会泄露管理员的密码或提供更改密码的方法，或者可能提供对特权功能的直接访问。

空白处填入哪一项最恰当？

A. 水平越权
B. 垂直越权
C. 水平和垂直越权
D. SQL注入

请给出符合题意的唯一选项。
```

````
单选题：

在Spring Security中，有时候一个角色可能涵盖了多种其他角色。例如：admin 可能包含 user 的权限，为实现这一功能，我们可能会为 admin 用户增加 user 角色。
要实现这种配置，我们需要用到 RoleVoter 的扩展实现类，RoleHierarchyVoter。其配置方式：
```
<bean id="roleVoter" class="org.springframework.security.access.vote.RoleHierarchyVoter">
    <constructor-arg ref="roleHierarchy" />
</bean>
<bean id="roleHierarchy"
        class="org.springframework.security.access.hierarchicalroles.RoleHierarchyImpl">
    <property name="hierarchy">
        <value>
            ROLE_ADMIN > ROLE_STAFF
            ROLE_STAFF > ROLE_USER
            ROLE_USER > ROLE_GUEST
        </value>
    </property>
</bean>
```
配置中出现了四种角色，ADMIN、STAFF、USER、GUEST，而这四种又有明显的包含于被包含关系，如此便可以使角色投票机制根据角色的层级进行决策。

阅读上述材料，分析在Spring Security的配置中，如果要设置角色的层级关系，应该使用哪个类的实例？
A. RoleHierarchyImpl
B. RoleVoterImpl
C. RoleHierarchyVoter
D. RoleVoter

请给出符合题意的唯一选项。
````

