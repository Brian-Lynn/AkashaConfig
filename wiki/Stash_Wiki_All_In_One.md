# Stash Wiki 文档目录 (精简版)

- [欢迎使用 Stash App 👋](#欢迎使用-stash-app)
- [快速上手](#快速上手)
- [iOS](#ios)
- [规则类型](#规则类型)
- [规则集合](#规则集合)
- [协议类型](#协议类型)
- [策略组](#策略组)
- [远程代理集](#远程代理集)
- [延迟测试](#延迟测试)
- [配置样例](#配置样例)
- [覆写文件（Override）](#覆写文件override)
- [策略组图标](#策略组图标)
- [Stash HTTP Engine](#stash-http-engine)
- [MitM](#mitm)
- [Force HTTP Engine](#force-http-engine)
- [HTTP 重写](#http-重写)
- [语法与接口](#语法与接口)
- [改写 HTTP](#改写-http)
- [面板 (Tile)](#面板-tile)
- [定时任务](#定时任务)
- [内置 DNS 服务](#内置-dns-服务)
- [为局域网设备提供代理](#为局域网设备提供代理)
- [服务提供商订阅](#服务提供商订阅)
- [网络性能增强](#网络性能增强)
- [按需启动](#按需启动)
- [Stash Mac](#stash-mac)
- [编写高效的配置文件](#编写高效的配置文件)
- [防止代理被检测](#防止代理被检测)
- [授权与激活](#授权与激活)
- [TestFlight 相关问题](#testflight-相关问题)
- [IPv6 兼容性](#ipv6-兼容性)
- [URL Schema](#url-schema)
- [越狱 iOS 系统内存限制修改](#越狱-ios-系统内存限制修改)
- [无法安装 Stash Mac 帮助程序 (Helper)](#无法安装-stash-mac-帮助程序-helper)
- [Stash 与其他 VPN 的冲突解决方法](#stash-与其他-vpn-的冲突解决方法)

---

# 欢迎使用 Stash App 👋

[Stash 用户文档易用且强劲的网络工具](/)

* [Stash 简介](/)
* [快速上手](/get-started)
* 更新日志

  + [iOS](/release-notes/ios)
* 分流规则

  + [规则类型](/rules/rule-types)
  + [规则集合](/rules/rule-set)
* 代理协议

  + [协议类型](/proxy-protocols/proxy-types)
  + [策略组](/proxy-protocols/proxy-groups)
  + [远程代理集](/proxy-protocols/proxy-providers)
  + [延迟测试](/proxy-protocols/proxy-benchmark)
* 配置文件

  + [配置样例](/configuration/example-config)
  + [覆写配置（Override）](/configuration/override)
  + [策略组图标](/configuration/proxy-group-icon)
* HTTP 引擎

  + [简介](/http-engine/intro)
  + [MitM](/http-engine/mitm)
  + [强制 HTTP 引擎](/http-engine/force-http-engine)
  + [HTTP 重写](/http-engine/rewrite)
* JavsScript 脚本

  + [语法与接口](/script/syntax-and-interface)
  + [改写 HTTP](/script/rewrite-requests)
  + [面板（Tile）](/script/tile)
  + [定时任务](/script/scheduled-tasks)
* 功能介绍

  + [内置 DNS 服务](/features/dns-server)
  + [为局域网设备提供代理](/features/provide-proxy-to-lan-device)
  + [服务提供商订阅](/features/service-provider-subscription)
  + [网络性能增强](/features/network-performance-enhance)
  + [按需启动](/features/on-demand)
* [Stash Mac](/stash-mac)
* 常见问题

  + [编写高效配置](/faq/effective-stash)
  + [防止代理被检测](/faq/proxy-detected)
  + [授权与激活](/faq/license-activation)
  + [TestFlight 相关](/faq/testflight)
  + [IPv6 兼容性](/faq/ipv6-compatible)
  + [URL Schema](/faq/url-schema)
  + [越狱修改内存限制](/faq/jailbreak-ios-memory-limit)
  + [无法安装帮助程序 (Helper)](/faq/stash-mac-helper)
  + [Stash 与其他 VPN 冲突](/faq/conflict-with-vpn)

On This Page

* [社交媒体](#社交媒体)
* [咨询合作](#咨询合作)
* [Stash on iOS](#stash-on-ios)
* [Stash on tvOS](#stash-on-tvos)
* [Stash on macOS](#stash-on-macos)

Stash 简介

# 欢迎使用 Stash App 👋

Stash 是 Clash Premium 内核在 Apple 设备上的最佳实现客户端，为 iOS、tvOS、macOS 与 visionOS 平台完整适配 Clash 功能。

此外，基于 Apple 平台特性，Stash 在 Clash Premium 功能基础上额外提供了以下特性：

* **配置同步**：Stash 的配置文件、规则、订阅等信息可以通过 iCloud 同步到所有设备上，实现一次配置，多设备共享。
* **远程控制**：Stash 设备的地址均安全存储于 iCloud，登录相同 iCloud 账号的设备可以直接远程控制局域网内的 Stash 设备，无需手动管理地址和密码。
* **快捷操作**：用户可以通过小组件、Today 视图、Widget、Siri 快捷指令等方式快速启动、停止、切换节点等操作 Stash。
* **按需连接**：基于 Apple 平台的 VPN On Demand 功能，用户可以根据 SSID、域名、应用等条件自动连接或断开 Stash。
* **增强的网络引擎**：Stash 支持 MitM 功能，允许用户查看 HTTPS 流量，并基于 Apple WebKit 引擎提供 JavaScript 脚本改写其中的内容。
* **深度定制**：为了更好地适配移动设备，Stash 深入定制了内核与运行时代码，优秀地控制了内存、电量与网络资源消耗。
* **丰富代理协议**：紧跟开源社区的发展，Stash 支持 Hysteria、VLESS、TUIC、WireGuard 等多种热门代理协议。

## 社交媒体

欢迎订阅 [Telegram 频道 (opens in a new tab)](https://t.me/StashFeed) 或关注 [X (Twitter) (opens in a new tab)](https://x.com/StashAppDev) 以获取最新消息。

欢迎加入 [Telegram 讨论组 (opens in a new tab)](https://t.me/StashFans)，与数万名 Stash 用户在线交流。

## 咨询合作

如有任何咨询或合作事宜，请发送电子邮件至 [info@stash.ws](mailto:info@stash.ws)。

## Stash on iOS

Stash 已经上架于 iOS App Store。

[(opens in a new tab)](https://apps.apple.com/app/stash/id1596063349?platform=iphone&l=zh-CN)

## Stash on tvOS

Stash 已经上架于 tvOS App Store。

[(opens in a new tab)](https://apps.apple.com/app/stash/id1596063349?platform=appleTV&l=zh-CN)

## Stash on macOS

Stash Mac 版本专为 macOS 平台设计，欲了解更多详情，请[点击这里](/stash-mac)。

[请点击这里查看 Stash Mac 的价格信息 (opens in a new tab)](https://stash.ws/macos/pricing/)

Last updated on 2025年4月18日

[快速上手](/get-started "快速上手")

---

# 快速上手

[Stash 用户文档易用且强劲的网络工具](/)

* [Stash 简介](/)
* [快速上手](/get-started)
* 更新日志

  + [iOS](/release-notes/ios)
* 分流规则

  + [规则类型](/rules/rule-types)
  + [规则集合](/rules/rule-set)
* 代理协议

  + [协议类型](/proxy-protocols/proxy-types)
  + [策略组](/proxy-protocols/proxy-groups)
  + [远程代理集](/proxy-protocols/proxy-providers)
  + [延迟测试](/proxy-protocols/proxy-benchmark)
* 配置文件

  + [配置样例](/configuration/example-config)
  + [覆写配置（Override）](/configuration/override)
  + [策略组图标](/configuration/proxy-group-icon)
* HTTP 引擎

  + [简介](/http-engine/intro)
  + [MitM](/http-engine/mitm)
  + [强制 HTTP 引擎](/http-engine/force-http-engine)
  + [HTTP 重写](/http-engine/rewrite)
* JavsScript 脚本

  + [语法与接口](/script/syntax-and-interface)
  + [改写 HTTP](/script/rewrite-requests)
  + [面板（Tile）](/script/tile)
  + [定时任务](/script/scheduled-tasks)
* 功能介绍

  + [内置 DNS 服务](/features/dns-server)
  + [为局域网设备提供代理](/features/provide-proxy-to-lan-device)
  + [服务提供商订阅](/features/service-provider-subscription)
  + [网络性能增强](/features/network-performance-enhance)
  + [按需启动](/features/on-demand)
* [Stash Mac](/stash-mac)
* 常见问题

  + [编写高效配置](/faq/effective-stash)
  + [防止代理被检测](/faq/proxy-detected)
  + [授权与激活](/faq/license-activation)
  + [TestFlight 相关](/faq/testflight)
  + [IPv6 兼容性](/faq/ipv6-compatible)
  + [URL Schema](/faq/url-schema)
  + [越狱修改内存限制](/faq/jailbreak-ios-memory-limit)
  + [无法安装帮助程序 (Helper)](/faq/stash-mac-helper)
  + [Stash 与其他 VPN 冲突](/faq/conflict-with-vpn)

On This Page

* [导入远程配置](#导入远程配置)
* [使用本地配置](#使用本地配置)

快速上手

# 快速上手

要在你的 iOS 设备上启用 Stash，只需导入一份 Stash/Clash 格式的配置文件。Stash 需要配置文件来指定代理服务器和网络策略，你可以通过 URL 下载服务提供商的配置，或者导入存放在 iCloud/OneDrive 中的本地文件来使用 Stash。

## 导入远程配置

如果你的服务提供商提供了 Stash/Clash Premium/Clash 的订阅链接，在 Stash 中导入远程配置是最简单的方式。

1. 在 Stash 的设置页面，选择配置文件；
2. 在 Stash 的配置列表中，选择从 URL 下载；
3. 在输入框中输入您的订阅地址，然后点击下载；
4. 确保您希望使用的配置文件已被选中；
5. 返回到 Stash 首页，点击启动；

现在，您的 Stash 已经准备就绪，尽情享用吧！😉

## 使用本地配置

使用本地配置可以充分自定义你的 Stash 分流策略，并利用 Stash 中强大的可视化编辑功能来完成配置编写。

1. 您可以通过 AirDrop 或者打开存放在 iCloud/OneDrive 中的 Stash/Clash Premium/Clash 配置文件，选择 Stash 打开；
2. 确保您希望使用的配置文件已被选中；
3. 返回到 Stash 首页，点击启动；

现在，您的 Stash 已经准备就绪，尽情享用吧！😉

Last updated on 2024年8月4日

[Stash 简介](/ "Stash 简介")[iOS](/release-notes/ios "iOS")

---

# iOS

[Stash 用户文档易用且强劲的网络工具](/)

* [Stash 简介](/)
* [快速上手](/get-started)
* 更新日志

  + [iOS](/release-notes/ios)
* 分流规则

  + [规则类型](/rules/rule-types)
  + [规则集合](/rules/rule-set)
* 代理协议

  + [协议类型](/proxy-protocols/proxy-types)
  + [策略组](/proxy-protocols/proxy-groups)
  + [远程代理集](/proxy-protocols/proxy-providers)
  + [延迟测试](/proxy-protocols/proxy-benchmark)
* 配置文件

  + [配置样例](/configuration/example-config)
  + [覆写配置（Override）](/configuration/override)
  + [策略组图标](/configuration/proxy-group-icon)
* HTTP 引擎

  + [简介](/http-engine/intro)
  + [MitM](/http-engine/mitm)
  + [强制 HTTP 引擎](/http-engine/force-http-engine)
  + [HTTP 重写](/http-engine/rewrite)
* JavsScript 脚本

  + [语法与接口](/script/syntax-and-interface)
  + [改写 HTTP](/script/rewrite-requests)
  + [面板（Tile）](/script/tile)
  + [定时任务](/script/scheduled-tasks)
* 功能介绍

  + [内置 DNS 服务](/features/dns-server)
  + [为局域网设备提供代理](/features/provide-proxy-to-lan-device)
  + [服务提供商订阅](/features/service-provider-subscription)
  + [网络性能增强](/features/network-performance-enhance)
  + [按需启动](/features/on-demand)
* [Stash Mac](/stash-mac)
* 常见问题

  + [编写高效配置](/faq/effective-stash)
  + [防止代理被检测](/faq/proxy-detected)
  + [授权与激活](/faq/license-activation)
  + [TestFlight 相关](/faq/testflight)
  + [IPv6 兼容性](/faq/ipv6-compatible)
  + [URL Schema](/faq/url-schema)
  + [越狱修改内存限制](/faq/jailbreak-ios-memory-limit)
  + [无法安装帮助程序 (Helper)](/faq/stash-mac-helper)
  + [Stash 与其他 VPN 冲突](/faq/conflict-with-vpn)

On This Page

* [3.0.0](#300)
* [新增](#新增)
* [优化](#优化)
* [修复](#修复)
* [2.7.1](#271)
* [2.7.0](#270)
* [新增](#新增-1)
* [优化](#优化-1)
* [修复](#修复-1)
* [2.6.6](#266)
* [2.6.5](#265)
* [2.6.4](#264)
* [新增](#新增-2)
* [优化](#优化-2)
* [修复](#修复-2)
* [2.6.3](#263)
* [2.6.2](#262)
* [2.6.1](#261)
* [新增](#新增-3)
* [优化](#优化-3)
* [修复](#修复-3)
* [2.6.0](#260)
* [新增](#新增-4)
* [优化](#优化-4)
* [修复](#修复-4)
* [2.5.6](#256)
* [2.5.5](#255)
* [2.5.4](#254)
* [2.5.3](#253)
* [2.5.2](#252)
* [2.5.0](#250)
* [2.4.7](#247)
* [2.4.6](#246)
* [2.4.4](#244)
* [2.4.2](#242)
* [2.4.1](#241)
* [2.4.0](#240)
* [2.3.1](#231)
* [2.3.0](#230)
* [经过重构后全新的可视化编辑器](#经过重构后全新的可视化编辑器)
* [2.2.4](#224)
* [2.2.3](#223)
* [2.2.2](#222)
* [2.2.1](#221)
* [新功能](#新功能)
* [改进](#改进)
* [Bug 修复](#bug-修复)
* [2.2.0](#220)
* [功能](#功能)
* [改进](#改进-1)
* [修复](#修复-5)
* [2.1.1](#211)
* [2.1.0](#210)
* [2.0.0](#200)
* [1.6.9](#169)
* [1.6.8](#168)
* [1.6.7](#167)
* [1.6.6](#166)
* [1.6.5](#165)
* [1.6.4](#164)
* [1.6.3](#163)
* [1.6.2](#162)
* [1.6.1](#161)
* [1.6.0](#160)
* [1.5.4](#154)
* [1.5.3](#153)
* [1.5.2](#152)
* [1.5.1](#151)
* [1.5.0](#150)
* [1.4.3](#143)
* [1.4.2](#142)
* [1.4.1](#141)
* [1.4.0](#140)
* [1.3.1](#131)
* [1.3.0](#130)
* [1.2.1](#121)
* [1.2.0](#120)
* [1.1.1](#111)
* [1.1.0](#110)
* [1.0.4](#104)
* [新功能](#新功能-1)
* [优化](#优化-5)

更新日志

iOS

## 3.0.0

### 新增

* 支持 ShadowSocks2022 协议
* 支持 ShadowTLS
* 支持 AND、OR、NOT 逻辑规则
* 新增 DOMAIN-WILDCARD 规则
* 新增 DOMAIN-REGEX 规则
* 新增 NETWORK 规则，可选值 tcp, udp
* 新增 PROTOCOL 规则，可选值 TCP, HTTP, HTTPS, UDP, QUIC
* 新增 URL-REGEX 规则
* 新增 USER-AGENT 规则
* 新增 body-rewrite 重写，支持：
* request-jq, request-replace-regex, request-json-replace, request-json-add, request-json-del
* response-jq, response-replace-regex, response-json-replace, response-json-add, response-json-del
* 支持嗅探 TLS Client Hello，获取 SNI 域名
* 在发起 UDP 连接时，现在会尝试使用目标代理发起 DNS 查询以确定目的地址的 IP
* 支持嗅探 QUIC / HTTP3
* 连接页现在能展示更详细的 TCP / UDP 协议信息
* DoH 和 DoH3 支持配置 UserAgent
* IP 信息提供商新增 BGP.Tools
* 重写支持读取 zstd 压缩算法
* 可视化编辑：
* 新增 reject-drop
* 支持修改 url-rewrite、header-rewrite、body-rewrite
* 支持修改脚本
* 支持长按复制图标 URL

### 优化

* 大幅优化耗电，尤其时在低负载场景下的功耗
* 优化 QUIC 嗅探
* 优化大量远程资源更新
* 优化 UDP 高并发下的内存使用
* 优化内存池分配策略
* 优化可视化编辑长文本显示
* 优化 ECH 实现

### 修复

* 修复图标第二次导入可能会异常的问题
* 修复可视化编辑排序的问题

ℹ️

发布于 2025 年 3 月 30 日

## 2.7.1

新年快乐！

* 修复部分服务提供商配置可能会闪退的问题

ℹ️

发布于 2025 年 1 月 1 日

## 2.7.0

### 新增

* iOS 18 Control Widget
* 新增 REJECT-DROP 策略
* 新增在 Stash 运行时更新 GEOIP 数据库
* 新增通过可视化编辑器编辑基本重写
* 新增 ip.im IP 信息提供商
* 图标适配 iOS 18 Dark 和 Tinted

### 优化

* 更新远程资源时，现在 Stash 将使用 ETag 协商缓存。在资源未变化时，Stash 不会重新下载资源，以节省用户及规则集合提供方的带宽。
* 当设置 server-cert-fingerprint 时，无需配置 skip-cert-verify 为 true
* 优化多语言翻译
* 优化系统 DNS

### 修复

* 修复部分情况下配置文件名称异常的问题

ℹ️

发布于 2024 年 10 月 21 日

## 2.6.6

* 修复 2.6.5 版本 YAML 空格可能导致配置文件识别错误的问题
* 优化 QUIC

ℹ️

发布于 2024 年 9 月 11 日

## 2.6.5

* 优化嗅探
  当连接到域名时，Stash 会对所有解析结果同时发起 TCP 握手并使用最快成功的连接。当嗅探到域名时，Stash 会触发一次 DNS 解析以进行上述功能。当域名在公共解析服无解析时，可能会导致连接错误，本次版本提高了与无解析域名的兼容性。
* 优化 HTTP 引擎对带端口的 Host 的兼容性
* Happy Eyeballs Dual Stack 从实验性功能移动到正式版，开启后会优化 IPv4 与 IPv6 双栈的兼容性
* 支持 Proxy-Providers 中设置 benchmark-url 与 benchmark-timeout
* 修复部分 UI 列表的意外跳动

ℹ️

发布于 2024 年 9 月 7 日

## 2.6.4

### 新增

* 支持 Hysteria 2 端口跳跃特性
* 新增 SSH 协议支持
* 新增 Juicity 协议支持
* Shortcuts 支持 match\_geosite 语法
* 当 CA 证书不受信任时，MitM 功能会自动关闭
* 支持在 MitM 设置页面删除已创建的证书
* 新增俄语支持

### 优化

* 优化 QUIC 协议 0-RTT
* 优化脚本 Header 兼容性
* 优化跳过代理 / 路由页面交互
* 优化 App 体积
* 优化 CA 证书逻辑，现在签发的证书有效期为 10 年
* 优化安装 CA 证书交互逻辑

### 修复

* 修复了可视化编辑中拖拽排序时 UI 可能错位的问题
* 修复部分情况下缓存文件占用空间过大的问题

ℹ️

发布于 2024 年 8 月 2 日

## 2.6.3

* 优化 WireGuard 连接稳定性
* 优化 Hysteria2 在部份网络下 0-RTT 的兼容性
* 优化运行时 MitM 证书生成过程，减少重复计算、提高性能和节省电源消耗
* 优化使用 underlying-proxy 的 WireGuard，在连接出错时能自动恢复
* 修复 15.4 以下系统脚本无法运行的问题

ℹ️

发布于 2024 年 6 月 18 日

## 2.6.2

* 修复部分情况 $persistentStore 可能无法正确保存的问题

ℹ️

发布于 2024 年 5 月 29 日

## 2.6.1

### 新增

* Stash 现已优化嗅探，支持在「仅使用 Tunnel 代理」下使用更多的覆写
* 现已支持嗅探 TCP 连接中可能的 HTTP 请求，包括 Method Host URL
* 支持 DNS over HTTP/3
* 支持代理服务器的 Server Certificate Fingerprint Pinning，开启后会在 TLS 握手时验证服务器证书 SHA256 指纹
* 工具新增 Script Hub
* 支持点击策略组图标折叠策略组

### 优化

* 优化脚本性能和内存占用，脚本性能大幅提升
* 优化基于 QUIC 协议的性能
* 优化断开 VPN 连接时的速度

### 修复

* 修复 iPad 上无法扫描 QR Code 的问题
* 修复一个可视化编辑可能的崩溃
* 修复最近引入的一个脚本内存占用延迟释放问题
* 修复脚本 $httpClient 异常处理不正确的问题
* 修复脚本 $persistentStore.write 传入值为 null 或 undefined 时不能保存的问题
* 修复 Today Widget 点击开关后状态可能不刷新的问题
* 修复脚本超时异常的问题
* 修复部份脚本执行失败问题

ℹ️

发布于 2024 年 5 月 22 日

## 2.6.0

### 新增

* 支持 iOS 17 Interactive Widget
* 更换 JavaScript 引擎，新引擎支持 WebAPI
* 支持 DNS 查询跟随规则
* 新增支持 classical text 规则集合
* 新增支持一键更新全部覆写
* 新增覆写分类
* 新增覆写图标
* 支持代理「Apple 推送通知」、「Wi-Fi Calling，彩信，短信」、「AirPlay， AirDrop」
* 脚本 $environment 支持 device-model
* 脚本 $httpClient 支持参数 timeout、insecure、auto-cookie、auto-redirect

### 优化

* 优化 UDP 兼容性
* 优化 Script 内存
* 优化覆写预览
* 优化脚本 $httpclient 兼容性，修复与部分服务器的通信可能会异常的问题
* 优化可视化 DNS 编辑，支持从首页进入

### 修复

* 修复 DNS over QUIC 响应超时的问题
* 修正脚本 $argument 参数行为，当未设置 argument 时，$argument 为 undefined
* 修正部分巨型规则匹配可能不准确的问题
* 修复 doq 可能会导致断开的问题
* 修复网络连接不能正确识别来自 Stash 内部的连接的问题
* 修复导入配置可能会没响应的问题
* 修复一处策略组崩溃
* 修复同名覆写无法安装的问题

ℹ️

发布于 2024 年 4 月 2 日

## 2.5.6

* 修复部分情况下，按钮开关状态不正确的问题
* 修复部分转换后的脚本无法安装的问题
* 修正并发脚本部分情况下异常的问题
* 优化脚本内存占用
* 脚本 setTimeout() 支持传入参数：
  setTimeout(function, delay, param1, param2, /\* …, \*/ paramN)

ℹ️

发布于 2023 年 12 月 15 日

## 2.5.5

* 修复上一个版本使用脚本时内存异常导致断开的问题

ℹ️

发布于 2023 年 12 月 6 日

## 2.5.4

* 修复一些潜在的崩溃
* 修复部分情况下脚本无法运行的问题

ℹ️

发布于 2023 年 12 月 4 日

## 2.5.3

* 修复 Network Extension 部分小概率崩溃。
* 修复定时脚本可能不准时的问题。
* 修复在设置页面切换配置首页信息可能不刷新的问题。
* 修复部分情况下无法点开首页规则的问题。
* 修复部分情况下重复提示配置自动更新的问题。

ℹ️

发布于 2023 年 11 月 18 日

## 2.5.2

* 修复 Hysteria 2 部分情况下超时的问题
* 错误修复和改进

ℹ️

发布于 2023 年 11 月 9 日

## 2.5.0

* 提升了虚拟网卡性能
* 支持 Hysteria 2 协议
* 修复 GEOSITE 相关问题
* 修复 WireGuard 协议在漫游时的问题
* 当从蜂窝数据切换至 Wi-Fi 时，基于 QUIC 的协议将尝试漫游至 Wi-Fi
* 当从蜂窝数据切换至 Wi-Fi 时，DoH/DoQ 将重新建立连接，以确保更准确的 DNS 查询记录
* Stash 现在能够自动屏蔽 MitM 列表中的 QUIC 流量，并让它回退至 HTTP1/2
* 修正了首页信息更新滞后的问题
* 修复 IPv6 环境下路由表可能闪退的问题
* 实验性地引入了 Happy Eyeballs Dual Stack 功能
  开启此功能后，IPv6 和 IPv4 将被同等对待。在并发模式下，例如，Stash 会同时对域名的所有 A 记录和 AAAA 记录进行 TCP 握手尝试，并选择最快握手成功的进行连接。

ℹ️

发布于 2023 年 11 月 7 日

## 2.4.7

* 修复 Sub-Store™

ℹ️

发布于 2023 年 10 月 9 日

## 2.4.6

* 修复在高负载的情况下 Network Extension 可能会断开的问题

ℹ️

发布于 2023 年 10 月 4 日

## 2.4.4

* 优化 JavaScript 引擎
* 新增「开关」快捷指令

ℹ️

发布于 2023 年 9 月 27 日

## 2.4.2

* 优化 HTTP 引擎的兼容性
* 错误修复和改进

ℹ️

发布于 2023 年 9 月 22 日

## 2.4.1

* 错误修复和改进

ℹ️

发布于 2023 年 9 月 20 日

## 2.4.0

* 配置同步支持将配置文件传输到 tvOS
* 远程控制器支持自动注册设备
* 优化 QUIC 协议
* 优化耗电
* 优化 UI 动画
* 错误修复和改进

ℹ️

发布于 2023 年 9 月 16 日

## 2.3.1

* 修复 Country.mmdb 无法自动更新的问题
* 修复部分情况下在未启动时策略组页面不显示的问题
* 修复部分情况下无法读取 iCloud 文件的问题

ℹ️

发布于 2023 年 7 月 9 日

## 2.3.0

* 新增支持 Tuic v5 协议
* 自动生成名称为 PROXY 的策略组，默认包含所有代理，方便外部 Override 引用

### 经过重构后全新的可视化编辑器

* 可视化编辑器支持保留注释和样式
* 本地代理编辑支持更多代理协议和字段
* 规则编辑支持更多字段和拖动排序
* 策略组编辑支持更多字段和支持在界面隐藏策略组
* 远程代理集编辑支持更多字段
* 规则集编辑支持更多字段和直接选择远程规则集
* 代理链支持单独设置延迟测试，以整体方式进行测试，提供更准确的结果
* 删除或重命名代理、策略组以及远程代理等操作，会联动修改引用，确保操作的一致性
* 订阅卡片支持展示多个服务提供商的订阅信息
* 首页点击相关卡片，快速进入可视化编辑界面进行编辑和管理
* 扫描二维码导入支持从相册选择图片
* 扫描二维码导入支持更多格式的二维码
* 扫描二维码导入支持导入带插件、混淆、承载网络、TLS 的二维码
* 优化菜单显示
* 优化图标集合安装和删除
* 优化一键删除日志，保留最新日志
* 优化在 iOS 15+ 设备上的交互
* 修复上游 DNS 服务器返回 Fake IP 情况下的兼容性
* 修复可视化编辑 DNS、日志等级时可能造成配置错误的问题
* 修复部分 UI 错位
* 修复部分情况下 iOS 13 闪退
* 修复一系列错误

ℹ️

发布于 2023 年 6 月 24 日

## 2.2.4

* 最近请求显示更多信息
* 全面优化软件性能
* 优化 iCloud 文件储存
* 优化 UI 细节
* iCloud 中的配置文件变更支持实时重新加载
* 修复部分情况下自动测速失效的问题
* 修复部分情况下无法自动更新远程资源的问题
* 错误修复和改进

ℹ️

发布于 2023 年 5 月 24 日

## 2.2.3

* 改善 Vmess 的性能问题
* 错误修复和改进

ℹ️

发布于 2023 年 5 月 10 日

## 2.2.2

* 新增自定义 Host 功能
* 修复 iPad 右侧页面在部分情况下不更新的问题
* 修复首页配置文件在部分情况下不更新的问题

ℹ️

发布于 2023 年 4 月 28 日

## 2.2.1

### 新功能

* 新增 GEOSITE 规则类型。
* 脚本 $httpClient 现支持二进制模式。
* 脚本 $httpClient 现支持通过 HTTP Header 指定出站代理策略。
* 新增 Stash 远程控制器，可通过 Stash iOS / Stash Mac Dashboard 控制其他设备上的 Stash。已保存的远程设备将通过 iCloud 同步。
* 支持 TLS Session Resumption，提升 TLS 握手效率。此功能需服务器端支持，可在连接页面确认是否成功启用。
* 新增 Lite 模式，优化内存占用与电池耗电，部分功能将被禁用。
* 新增 no-track 参数，匹配到此规则的连接将在连接列表中隐藏。

### 改进

* 优化大量 nameserver-policy 场景下的内存占用。
* 改进网络诊断页面。
* 提升 HTTP / TLS 嗅探能力。
* 提高 relay 策略组稳定性。
* 优化首页与策略组页面性能，修复卡顿问题。
* 提高 Stash Tile 计时器准确性。
* 优化网络切换下 DNS 缓存刷新策略。
* 改善脚本编辑器用户体验。
* 提升安装 Override 用户体验。

### Bug 修复

* 修复部分可视化编辑问题。
* 解决 override 合并时 emoji 表情被转义的问题。
* 修复一系列下载配置的兼容性问题。

ℹ️

发布于 2023 年 4 月 26 日

## 2.2.0

### 功能

* 新增 GEOSITE 规则类型。
* 脚本 $httpClient 现支持二进制模式。
* $httpClient 现支持通过 HTTP Header 指定出站代理策略。
* 新增 Stash 远程控制器，可通过 Stash iOS / Stash Mac Dashboard 控制其他设备上的 Stash。已保存的远程设备将通过 iCloud 同步。
* 支持 TLS Session Resumption，提升 TLS 握手效率。此功能需服务器端支持，可在连接页面确认是否成功启用。
* 新增 Lite 模式，优化内存占用与电池耗电，部分功能将被禁用。
* 新增 no-track 参数，匹配到此规则的连接将在连接列表中隐藏。

### 改进

* 优化大量 nameserver-policy 场景下的内存占用。
* 改进网络诊断页面。
* 提升 HTTP / TLS 嗅探能力。
* 提高 relay 策略组稳定性。
* 优化首页与策略组页面性能，修复卡顿问题。
* 提高 Stash Tile 计时器准确性。
* 优化网络切换下 DNS 缓存刷新策略。
* 改善脚本编辑器用户体验。
* 提升安装 Override 用户体验。

### 修复

* 修复部分可视化编辑问题。
* 解决 override 合并时 emoji 表情被转义的问题。
* 修复一系列下载配置的兼容性问题。

ℹ️

发布于 2023 年 4 月 21 日

## 2.1.1

错误修复和优化

ℹ️

发布于 2023 年 2 月 26 日

## 2.1.0

* WireGuard 现在可以作为 Layer 4 的代理使用
* 节点信息新增入站信息和出站信息显示
* 全新的 JavaScript 脚本引擎
* 脚本现在支持并发执行
* 脚本现在支持二进制脚本
* 脚本现在支持将通知跳转到 URL
* 脚本新增环境变量 $environment.system（iOS / macOS）
* 可视化编辑器现在支持 WireGuard 和 TUIC
* 通过扫描二维码导入配置文件
* 优化的仪表板现在显示网络流量统计信息、DNS 缓存信息和规则总数
* 通过将 interval 设置为 -1 可关闭自动策略组连通性检查
* 调整了各种 QUIC 协议实现以提高兼容性
* 减少了 Hysteria 的内存占用
* 修正了 Stash HTTP 引擎中一些请求的行为
* 修复了通知无法堆叠的问题
* 优化了脚本 Header 的兼容性
* 新增了 Override 语法

ℹ️

发布于 2023 年 1 月 4 日

## 2.0.0

* 完全重构的网络引擎
* 全新的用户界面

Stash 2 重新设计了网络转发引擎，从 TCP、QUIC、DNS 多个层面优化网络性能。为各种代理协议单独设计的健康检查策略，及时感知代理节点离线，配合 URL-TEST 构建高可用策略组。

简洁明了的首页，展示实时的网络流量，链路质量，流媒体解锁信息，更允许你使用 JavaScript 编写自定义面板（Tile）。

ℹ️

发布于 2022 年 11 月 20 日

## 1.6.9

* 错误修复和改进

ℹ️

发布于 2022 年 8 月 19 日

## 1.6.8

* 修复部分情况下证书可能安装失败的问题
* 优化 iCloud 同步过程

ℹ️

发布于 2022 年 8 月 16 日

## 1.6.7

* 提高数据包传输性能

ℹ️

发布于 2022 年 7 月 31 日

## 1.6.6

* 修复了一些已知问题

ℹ️

发布于 2022 年 7 月 23 日

## 1.6.5

* 新增日语翻译
* 新增韩语翻译

ℹ️

发布于 2022 年 6 月 11 日

## 1.6.4

* 修复部分信息显示不正确的问题

ℹ️

发布于 2022 年 6 月 9 日

## 1.6.3

错误修复和改进

ℹ️

发布于 2022 年 6 月 8 日

## 1.6.2

* 修复脚本 HTTP Header 解析的问题
* 修复 CA 证书页面潜在崩溃的问题
* 修复部分情况下脚本日志不显示的问题
* 修复部分情况下配置文件无法切换的问题

ℹ️

发布于 2022 年 6 月 1 日

## 1.6.1

* 新增 Connection Log
* 新增本地配置文件通过 "subscribe-url" Key 获取订阅信息
* 新增可视化编辑导入 Icon Set JSON
* 新增 Time Tab 到 Connection 页面，查看连接过程各环节耗时
* 新增 Fallback DNS 开关，如需要 Fallback DNS 请手动开启
* 新增支持长按刷新订阅信息
* 新增延迟测试方法修改
* 新增日志列表显示
* 新增独立脚本日志
* 提高 HTTP Engine 与部分客户端的兼容性
* 修复 Exclude 列表可能不生效
* 修复 Rule Set 匹配不正确问题
* 修复 Rule Provider 加载后规则丢失问题
* 显示 HTTP 连接的 Request Header
* 支持切换策略组时打断现有连接
* 完善 Shortcuts 支持
* 取消了 URL-Regex 规则，可以用 HTTP 改写代替
* 通过缓存策略优化了大量规则匹配的性能
* 优化 iCloud 同步过程
* 修复 iPad 测速失败的问题

ℹ️

发布于 2022 年 5 月 16 日

## 1.6.0

* 新增 iCloud 配置同步
* 新增覆写仓库
* 新增 TUIC 协议
* 支持 Cellular SSID Policy
* 支持 Rewrite Header
* 支持 HTTP 协议自定义 Headers
* 支持 Script Argument
* 支持 Script 同时修改 Request & Response
* 支持安装配置文件的自定义证书
* 新增覆写导入
* 新增长按复制 URL
* 兼容 DNS Fallback
* 兼容无过期时间的订阅信息

ℹ️

发布于 2022 年 5 月 11 日

## 1.5.4

现在可以通过 App 申请参加 TestFlight 测试啦！

ℹ️

发布于 2022 年 4 月 26 日

## 1.5.3

* 修复 http engine 兼容性问题
* 修复 hysteria 断流问题

ℹ️

发布于 2022 年 4 月 17 日

## 1.5.2

* 内核性能优化
* 新增内置 SpeedTest 测速
* 支持在 TUN 模式下执行脚本和改写
* 流媒体解锁检测支持 Disney +
* 支持修改 Skip-Proxy，Exclude-Tun-Routes
* 支持覆写列表的排序功能

ℹ️

发布于 2022 年 4 月 15 日

## 1.5.1

* 优化 JavaScript 内存占用
* JavaScript Console Log 输出到 Stash 日志
* 修复部分情况下可视化修改 DNS 失败的问题

ℹ️

发布于 2022 年 4 月 5 日

## 1.5.0

* 完全重构的 JavaScript 引擎
* 支持 Hybrid 并发混合网络
* 支持自定义 GEOIP 数据库
* 支持 VLESS / XTLS 协议
* 支持局域网代理
* 支持自行签发的 ECC 根证书
* 支持自定义配置文件更新时间
* 支持可视化更新 Script Providers
* 优化批量更新 Providers 速度
* 优化 UI 编辑代理服务器
* 修复 DNS 编辑不生效的问题
* 修复错误的内存警告

ℹ️

发布于 2022 年 4 月 1 日

## 1.4.3

* hysteria 更新到 v1.0.1
* 修复部分协议兼容性问题
* 可视化编辑器支持 relay
* 可视化编辑器支持 domain-text / ipcidr-text

ℹ️

发布于 2022 年 3 月 11 日

## 1.4.2

* 优化测速
* 显示 http 请求 metadata
* 增加 DNS 配置可视化编辑
* 优化 IP-CIDR 规则内存占用
* 优化配置文件加载过程
* 优化配置文件更新过程
* 修改代理名称之后同时修改代理组中的名称
* 下载配置文件时检查配置文件是否格式正确

ℹ️

发布于 2022 年 3 月 6 日

## 1.4.1

* 支持 DNS-over-QUIC
* 优化内存占用
* 新增兼容文本格式的规则集
  [https://github.com/STASH-NETWORKS-LIMITED/stash-example/blob/main/config.yaml#L485 (opens in a new tab)](https://github.com/STASH-NETWORKS-LIMITED/stash-example/blob/main/config.yaml#L485)

规则集合文档：
[https://manual.stash.ws/basic/rule-set (opens in a new tab)](https://manual.stash.ws/basic/rule-set)

ℹ️

发布于 2022 年 2 月 24 日

## 1.4.0

* 支持使用覆写覆盖当前配置文件的部分设定
* 支持使用 JavaScript 脚本改写 HTTP(S) 请求，脚本运行情况与控制台输出可以在日志中查看。 首个版本可能不兼容某些 JavaScript 语法，请等待后续更新。
* 增加组策略的代理快捷增加和删除
* 支持使用系统 DNS
* 性能优化
* 允许自定义通知
* 支持扫码添加 SS 和 SSR 代理
* 修复个人热点 DNS 不正确的问题
* 修复可视化编辑器中文编码的问题
* 修复部分 Domain 规则集无法使用的问题
* 修复删除 Rule 闪退的问题

ℹ️

发布于 2022 年 2 月 14 日

## 1.3.1

* 允许自定义应用图标
* 允许自定义代理组图标
* 新增手动更新 Provider
* 新增 MitM 规则导入
* 完善可视化编辑器
* 优化捷径启动过程
* 修复某些情况下代理添加失败的问题
* 修复编辑器键盘高度问题
* 优化 Hysteria 协议 ReceiveWindow，优化内存占用，避免超出 NE 内存限制。感谢 Hysteria 作者 tobyxdd 提供技术支持。

Icon 配置文件参考：
[https://github.com/STASH-NETWORKS-LIMITED/stash-example/blob/main/config.yaml#L366 (opens in a new tab)](https://github.com/STASH-NETWORKS-LIMITED/stash-example/blob/main/config.yaml#L366)

ℹ️

发布于 2022 年 2 月 13 日

## 1.3.0

* 全新的首页 DashBoard 界面
* 全新策略组界面
* 允许自定义首页布局
* 可视化编辑器支持选择代理和代理组
* 新增 Tun Only 模式，以改善和某些应用的兼容性问题
* 支持 Hysteria Auth
* 支持 307 重定向
* 支持主动打断连接
* 支持更多正则表达式格式
* 更新 Hysteria 到 0.9.6
* 完善日志显示
* 优化内存占用
* 优化耗电
* 修复 iPad 分屏模式下策略组显示问题
* 在规则集下载失败时，允许 Stash 继续启动
* 修复小组件启动失败的情况

ℹ️

发布于 2022 年 1 月 30 日

## 1.2.1

* 新增 Rewrite & MitM Mixin 订阅配置文件
* 新增 Today Extension (小组件)
* 新增 Hysteria 支持
* 新增 3D Touch 长按支持
* 增强配置文件转换兼容性
* 优化代理编辑

参考配置：[https://github.com/STASH-NETWORKS-LIMITED/stash-example/blob/main/config.yaml#L319 (opens in a new tab)](https://github.com/STASH-NETWORKS-LIMITED/stash-example/blob/main/config.yaml#L319)

ℹ️

发布于 2022 年 1 月 19 日

## 1.2.0

* 新增 MITM
* 新增 URL 重写 (URL Rewrite)
* 新增强制使用 Stash Engine 以 HTTP 协议处理 TCP 连接
* 新增使用 Script 来编写规则，能不同的条件进行组合，使得规则编写更灵活更自由
* 新增快捷指令
* 新增可视化编辑器
* 适配 Clash v1.9.0 Vmess 配置格式
* 优化统计、当前链接、实时日志等更新逻辑
* 优化 iPad 视图
* 优化错误提示逻辑
* 修复某些情况下 iOS 14 系统崩溃
* 修复负载均衡无法显示的问题
* 修复远程控制器返回

MITM 示例:
[https://github.com/STASH-NETWORKS-LIMITED/stash-example/blob/main/config.yaml#L26 (opens in a new tab)](https://github.com/STASH-NETWORKS-LIMITED/stash-example/blob/main/config.yaml#L26)

Rewrite 示例:
[https://github.com/STASH-NETWORKS-LIMITED/stash-example/blob/main/config.yaml#L33 (opens in a new tab)](https://github.com/STASH-NETWORKS-LIMITED/stash-example/blob/main/config.yaml#L33)

Script Shorcuts 示例:
[https://github.com/STASH-NETWORKS-LIMITED/stash-example/blob/main/config.yaml#L38 (opens in a new tab)](https://github.com/STASH-NETWORKS-LIMITED/stash-example/blob/main/config.yaml#L38)

Force-HTTP-Engine 示例:
[https://github.com/STASH-NETWORKS-LIMITED/stash-example/blob/main/config.yaml#L16 (opens in a new tab)](https://github.com/STASH-NETWORKS-LIMITED/stash-example/blob/main/config.yaml#L16)

ℹ️

发布于 2021 年 12 月 29 日

## 1.1.1

* 针对 iOS 14 或以下用户优化
* 增加 Provider 使用代理更新
* 增加策略组列表视图
* 增加诊断工具
* 增加 YAML 格式校验
* 增加 iPerf3 反向模式测试
* 修复部分情况下 Rule Set 不匹配的问题
* 修复部分情况下配置文件切换策略组不更新的问题
* 优化性能
* 优化内存
* 优化电源管理
* 优化折叠动画
* 优化震动反馈
* 优化策略组显示
* 优化订阅配置文件修改
* 优化首页状态
* Stash Engine 更新 v1.1.0

ℹ️

发布于 2021 年 12 月 22 日

## 1.1.0

* 新增按需连接
* 新增订阅信息
* 使用 Stash Engine v1.0.2
* 支持在 Select Proxy Group 根据 SSID 自动切换策略
  配置格式参考 [https://github.com/STASH-NETWORKS-LIMITED/stash-example/blob/main/config.yaml#L335 (opens in a new tab)](https://github.com/STASH-NETWORKS-LIMITED/stash-example/blob/main/config.yaml#L335)
* 新增隐藏 VPN 图标
* 新增日志搜索功能
* 增加网络变化通知
* 增加当前连接显示策略
* 增加路由表
* 增加文件导出功能
* 优化的 Rule-Set 匹配器
* 优化网络切换过程
* 优化 Country.mmdb
* 优化主页面
* 优化策略组页面
* 优化策略组暗黑模式
* 优化代理组类型显示
* 优化展开的点击事件
* 优化日志显示
* 优化速率显示
* 优化首页配置文件名称过长的问题

ℹ️

发布于 2021 年 12 月 16 日

## 1.0.4

### 新功能

* 新增代理信息检测
* 新增流媒体解锁检测
* 新增代理服务器 UDP 检测
* 新增代理服务器 IPv6 检测
* 新增长按服务器查看更多信息
* 新增 Airdrop 文件导入
* 增加复制配置文件的功能

### 优化

* 切换网络后 VPN 不断线
* 优化切换配置过程
* 优化配置页面弹框
* 优化配置编辑器
* 优化测速结果显示
* Bug 修复

ℹ️

发布于 2021 年 12 月 10 日

Last updated on 2025年4月5日

[快速上手](/get-started "快速上手")[规则类型](/rules/rule-types "规则类型")

---

# 规则类型

[Stash 用户文档易用且强劲的网络工具](/)

* [Stash 简介](/)
* [快速上手](/get-started)
* 更新日志

  + [iOS](/release-notes/ios)
* 分流规则

  + [规则类型](/rules/rule-types)
  + [规则集合](/rules/rule-set)
* 代理协议

  + [协议类型](/proxy-protocols/proxy-types)
  + [策略组](/proxy-protocols/proxy-groups)
  + [远程代理集](/proxy-protocols/proxy-providers)
  + [延迟测试](/proxy-protocols/proxy-benchmark)
* 配置文件

  + [配置样例](/configuration/example-config)
  + [覆写配置（Override）](/configuration/override)
  + [策略组图标](/configuration/proxy-group-icon)
* HTTP 引擎

  + [简介](/http-engine/intro)
  + [MitM](/http-engine/mitm)
  + [强制 HTTP 引擎](/http-engine/force-http-engine)
  + [HTTP 重写](/http-engine/rewrite)
* JavsScript 脚本

  + [语法与接口](/script/syntax-and-interface)
  + [改写 HTTP](/script/rewrite-requests)
  + [面板（Tile）](/script/tile)
  + [定时任务](/script/scheduled-tasks)
* 功能介绍

  + [内置 DNS 服务](/features/dns-server)
  + [为局域网设备提供代理](/features/provide-proxy-to-lan-device)
  + [服务提供商订阅](/features/service-provider-subscription)
  + [网络性能增强](/features/network-performance-enhance)
  + [按需启动](/features/on-demand)
* [Stash Mac](/stash-mac)
* 常见问题

  + [编写高效配置](/faq/effective-stash)
  + [防止代理被检测](/faq/proxy-detected)
  + [授权与激活](/faq/license-activation)
  + [TestFlight 相关](/faq/testflight)
  + [IPv6 兼容性](/faq/ipv6-compatible)
  + [URL Schema](/faq/url-schema)
  + [越狱修改内存限制](/faq/jailbreak-ios-memory-limit)
  + [无法安装帮助程序 (Helper)](/faq/stash-mac-helper)
  + [Stash 与其他 VPN 冲突](/faq/conflict-with-vpn)

On This Page

* [DOMAIN](#domain)
* [DOMAIN-SUFFIX](#domain-suffix)
* [DOMAIN-KEYWORD](#domain-keyword)
* [DOMAIN-WILDCARD](#domain-wildcard)
* [DOMAIN-REGEX](#domain-regex)
* [GEOIP](#geoip)
* [IP-ASN](#ip-asn)
* [IP-CIDR / IP-CIDR6](#ip-cidr--ip-cidr6)
* [NETWORK](#network)
* [PROTOCOL](#protocol)
* [DST-PORT](#dst-port)
* [RULE-SET](#rule-set)
* [GEOSITE](#geosite)
* [PROCESS-NAME](#process-name)
* [PROCESS-PATH](#process-path)
* [SCRIPT](#script)
* [AND](#and)
* [OR](#or)
* [NOT](#not)

分流规则

规则类型

# 规则类型

通过编写规则，您可以指定不同连接的出站方式，例如通过某个代理转发或拦截。规则可以根据连接的 IP、域名、进程名或组合多个条件进行匹配。

对于每一条连接，系统会按照从上到下的顺序依次匹配规则。

规则可以分为以下几种类型（其中 IP 类型可能会触发 DNS 解析）：

* 基于域名
* 基于 IP 或端口
* 基于协议
* 逻辑规则
* 其他复合类型

💡

如需针对 URL 编写规则，请参阅 [HTTP 重写](/http-engine/rewrite) 章节。

💡

在规则末尾可添加 `no-track` 参数来隐藏匹配到此规则的连接，例如
`SCRIPT,quic,REJECT,no-track`。这能有效避免大量 REJECT 记录充斥页面。

💡

可使用 `REJECT` 和 `REJECT-DROP` 这两个内置代理来拦截连接。`REJECT`
会立即返回错误，而 `REJECT-DROP` 会静默丢弃连接，以避免产生连接风暴。

## DOMAIN

完全匹配域名，例如 `DOMAIN,google.com` 匹配 `google.com`，但不匹配 `www.google.com`。

## DOMAIN-SUFFIX

匹配域名后缀，例如 `DOMAIN-SUFFIX,google.com` 匹配 `google.com` 和 `www.google.com`。

## DOMAIN-KEYWORD

关键词匹配域名，例如 `DOMAIN-KEYWORD,google` 匹配 `google.com` 和 `google.jp`。

## DOMAIN-WILDCARD

使用通配符匹配域名，支持 `*` 和 `?`，例如 `DOMAIN-WILDCARD,*.google.com` 匹配 `www.google.com` 和 `mail.google.com`。

其中 `*` 匹配任意数量的字符，`?` 匹配一个字符。

## DOMAIN-REGEX

使用正则表达式匹配域名，例如 `DOMAIN-REGEX,^.*\.google\.com$` 匹配 `www.google.com` 和 `mail.google.com`。

## GEOIP

通过 MaxMind GeoIP 匹配国家代码，例如 `GEOIP,CN`。可添加 `no-resolve` 以避免触发 DNS 解析。

💡

Stash 允许用户替换符合 MaxMind GeoIP
格式的数据库。用户可根据自身需求选择更适合的 MaxMind GeoIP 数据库。

## IP-ASN

通过 IP 自治系统编号匹配，例如 `IP-ASN,714`。可添加 `no-resolve` 以避免触发 DNS 解析。

## IP-CIDR / IP-CIDR6

IP CIDR 范围匹配，例如 `IP-CIDR,192.168.1.0/24`。可添加 `no-resolve` 以避免触发 DNS 解析。

## NETWORK

匹配网络类型，例如 `tcp` 匹配 TCP 协议，`udp` 匹配 UDP 协议。

## PROTOCOL

PROTOCOL 规则比 NETWORK 规则提供更细粒度的判断。支持的协议包括：

* `TCP`
* `UDP`
* `HTTP`
* `HTTPS`
* `QUIC`

## DST-PORT

目标端口匹配，例如 `DST-PORT,80`。

## RULE-SET

引用大量规则时，请使用 [规则集合](/rules/rule-set)。

## GEOSITE

[domain-list-community (opens in a new tab)](https://github.com/v2fly/domain-list-community) 是由 v2fly 社区维护的域名列表。

例如 `GEOSITE,twitter` 匹配 [Twitter (opens in a new tab)](https://github.com/v2fly/domain-list-community/blob/master/data/twitter) 公司相关域名：

```
ads-twitter.com
cms-twdigitalassets.com
periscope.tv
pscp.tv
t.co
tellapart.com
tweetdeck.com
twimg.com
twitpic.com
twitter.biz
twitter.com
twitter.jp
twitter.map.fastly.net
twittercommunity.com
twitterflightschool.com
twitterinc.com
twitteroauth.com
twitterstat.us
twtrdns.net
twttr.com
twttr.net
twvid.com
vine.co
x.com

```

⚠️

domain-list-community 数据不随 Stash 分发，Stash 会在首次使用时从 github.com
按需加载域名数据。首次使用请确保当前配置能正常访问 github.com。

## PROCESS-NAME

进程名称匹配，例如 `PROCESS-NAME,Telegram`。仅对本机进程有效。

⚠️

由于 Network Extension 的限制，Stash iOS/tvOS（包括运行于 Apple silicon
设备上的 iOS 版）不支持 PROCESS-NAME 规则，配置中的进程相关规则将被忽略。

## PROCESS-PATH

进程路径匹配，例如 `PROCESS-PATH,/Applications/Telegram.app/Contents/MacOS/Telegram`。仅对本机进程有效。

⚠️

由于 Network Extension 的限制，Stash iOS/tvOS（包括运行于 Apple silicon
设备上的 iOS 版）不支持 PROCESS-PATH 规则，配置中的进程相关规则将被忽略。

## SCRIPT

通过 Python 表达式匹配请求。表达式必须返回 Boolean 值，执行错误的表达式会被忽略。

表达式可读取以下变量：

```
{
  "network": "string", // 可以是 tcp 或 udp
  "host": "string", // 可能为空
  "dst_ip": "string", // 可能为空
  "dst_port": "number",
  "src_ip": "string", // 仅在网关模式下有效
  "src_port": "number" // 仅在网关模式下有效
}
```

表达式可调用以下函数：

```
def resolve_ip(host: str) -> str:
    pass

def in_cidr(ip: str, cidr: str) -> bool:
    pass

def geoip(ip: str) -> str:
    pass

def ipasn(ip: str) -> int:
    pass

def match_provider(name: str) -> bool:
    pass

def match_geosite(name: str) -> bool:
    pass
```

例如，需要拦截 QUIC 协议的请求，可以这样写：

```
rules:
  - SCRIPT,quic,REJECT
  - SCRIPT,udp-cn,ProxyToCN

script:
  shortcuts: # 可在 rule 中引用
    quic: network == 'udp' and dst_port == 443 # 匹配 QUIC 协议
    udp-cn: network == 'udp' and geoip(dst_ip if dst_ip != '' else resolve_ip(host)) == 'CN' # 匹配发往 CN 的 UDP
    instagram-quic: network == 'udp' and dst_port == 443 and match_geosite('instagram') # 匹配 Instagram 的 QUIC
```

## AND

当需要同时满足多个规则时，可以使用 AND 逻辑规则。

`AND,((#Rule1), (#Rule2), (#Rule3)...),PROXY`

💡

在子规则中，也可以添加 `no-resolve` 参数来避免触发 DNS
解析。例如：`AND,((IP-CIDR,192.168.1.110,no-resolve), (DOMAIN-SUFFIX,example.com), (DOMAIN-KEYWORD, xxx)), DIRECT`

## OR

当需要满足其中一个规则时，可以使用 OR 逻辑规则。

`OR,((#Rule1), (#Rule2), (#Rule3)...),PROXY`

## NOT

对规则取反。

`NOT,((#Rule1)),PROXY`

💡

逻辑规则可以组合使用，例如：`AND,((NOT,((SRC-IP,192.168.1.110))),(DOMAIN,example.com)),DIRECT`

Last updated on 2025年4月9日

[iOS](/release-notes/ios "iOS")[规则集合](/rules/rule-set "规则集合")

---

# 规则集合

[Stash 用户文档易用且强劲的网络工具](/)

* [Stash 简介](/)
* [快速上手](/get-started)
* 更新日志

  + [iOS](/release-notes/ios)
* 分流规则

  + [规则类型](/rules/rule-types)
  + [规则集合](/rules/rule-set)
* 代理协议

  + [协议类型](/proxy-protocols/proxy-types)
  + [策略组](/proxy-protocols/proxy-groups)
  + [远程代理集](/proxy-protocols/proxy-providers)
  + [延迟测试](/proxy-protocols/proxy-benchmark)
* 配置文件

  + [配置样例](/configuration/example-config)
  + [覆写配置（Override）](/configuration/override)
  + [策略组图标](/configuration/proxy-group-icon)
* HTTP 引擎

  + [简介](/http-engine/intro)
  + [MitM](/http-engine/mitm)
  + [强制 HTTP 引擎](/http-engine/force-http-engine)
  + [HTTP 重写](/http-engine/rewrite)
* JavsScript 脚本

  + [语法与接口](/script/syntax-and-interface)
  + [改写 HTTP](/script/rewrite-requests)
  + [面板（Tile）](/script/tile)
  + [定时任务](/script/scheduled-tasks)
* 功能介绍

  + [内置 DNS 服务](/features/dns-server)
  + [为局域网设备提供代理](/features/provide-proxy-to-lan-device)
  + [服务提供商订阅](/features/service-provider-subscription)
  + [网络性能增强](/features/network-performance-enhance)
  + [按需启动](/features/on-demand)
* [Stash Mac](/stash-mac)
* 常见问题

  + [编写高效配置](/faq/effective-stash)
  + [防止代理被检测](/faq/proxy-detected)
  + [授权与激活](/faq/license-activation)
  + [TestFlight 相关](/faq/testflight)
  + [IPv6 兼容性](/faq/ipv6-compatible)
  + [URL Schema](/faq/url-schema)
  + [越狱修改内存限制](/faq/jailbreak-ios-memory-limit)
  + [无法安装帮助程序 (Helper)](/faq/stash-mac-helper)
  + [Stash 与其他 VPN 冲突](/faq/conflict-with-vpn)

分流规则

规则集合

# 规则集合

规则集合功能可以在较低资源占用情况下引用大量规则，并支持后台静默更新而无需重新加载 Stash。要使用规则集合，您需要在 `rule-provide` 下完成声明，之后即可在 `rules` 下引用集合。

```
rule-providers:
  proxy-domain:
    behavior: domain # 使用 domain 类规则集可提高匹配效率
    format: yaml # 使用 yaml 格式的规则集
    url: https://cdn.jsdelivr.net/gh/Loyalsoldier/clash-rules@release/proxy.txt
    interval: 86400

  cn-cidr:
    behavior: ipcidr # 使用 ipcidr 类规则集可提高匹配效率
    format: text # 使用 text 格式的规则集
    url: https://cdn.jsdelivr.net/gh/17mon/china_ip_list@master/china_ip_list.txt
    interval: 86400

rules:
  - RULE-SET,proxy-domain,Proxy
  - RULE-SET,cn-cidr,DIRECT,no-resolve # ipcidr 类规则集支持 no-resolve 参数
```

Stash 支持多种规则集合格式，不同格式支持不同内容类型，并具有不同的资源占用表现：

| 行为（behavior） | 格式 | 支持内容 | 示例 | 匹配性能 |
| --- | --- | --- | --- | --- |
| `domain` | `yaml` | 域名/域名通配符 | [链接 (opens in a new tab)](https://fastly.jsdelivr.net/gh/Loyalsoldier/clash-rules@release/proxy.txt) | 优秀 |
| `domain` | `text` | 域名/域名通配符 | [链接 (opens in a new tab)](https://fastly.jsdelivr.net/gh/Loyalsoldier/surge-rules@release/proxy.txt) | 优秀 |
| `ipcidr` | `yaml` | IPv4/IPv6 集合，CIDR 格式 | [链接 (opens in a new tab)](https://fastly.jsdelivr.net/gh/Loyalsoldier/clash-rules@release/lancidr.txt) | 优秀 |
| `ipcidr` | `text` | IPv4/IPv6 集合，CIDR 格式 | [链接 (opens in a new tab)](https://fastly.jsdelivr.net/gh/17mon/china_ip_list@master/china_ip_list.txt) | 优秀 |
| `classical` | `yaml` | 任意规则类型 | [链接 (opens in a new tab)](https://fastly.jsdelivr.net/gh/Hackl0us/SS-Rule-Snippet@master/Rulesets/Clash/Basic/Apple-direct.yaml) | 较差 |
| `classical` | `text` | 任意规则类型 | [链接 (opens in a new tab)](https://cdn.jsdelivr.net/gh/Loyalsoldier/surge-rules@release/cncidr.txt) | 较差 |

💡

`domain(-text)` 和 `ipcidr(-text)` 类型的规则集合针对大量数据进行了专门优化，当规则条目较多时建议优先选用。

不建议使用包含大量规则的 `classical` 规则集合，这会显著增加 Stash 的内存占用并降低规则匹配速度。

Last updated on 2025年4月6日

[规则类型](/rules/rule-types "规则类型")[协议类型](/proxy-protocols/proxy-types "协议类型")

---

# 协议类型

[Stash 用户文档易用且强劲的网络工具](/)

* [Stash 简介](/)
* [快速上手](/get-started)
* 更新日志

  + [iOS](/release-notes/ios)
* 分流规则

  + [规则类型](/rules/rule-types)
  + [规则集合](/rules/rule-set)
* 代理协议

  + [协议类型](/proxy-protocols/proxy-types)
  + [策略组](/proxy-protocols/proxy-groups)
  + [远程代理集](/proxy-protocols/proxy-providers)
  + [延迟测试](/proxy-protocols/proxy-benchmark)
* 配置文件

  + [配置样例](/configuration/example-config)
  + [覆写配置（Override）](/configuration/override)
  + [策略组图标](/configuration/proxy-group-icon)
* HTTP 引擎

  + [简介](/http-engine/intro)
  + [MitM](/http-engine/mitm)
  + [强制 HTTP 引擎](/http-engine/force-http-engine)
  + [HTTP 重写](/http-engine/rewrite)
* JavsScript 脚本

  + [语法与接口](/script/syntax-and-interface)
  + [改写 HTTP](/script/rewrite-requests)
  + [面板（Tile）](/script/tile)
  + [定时任务](/script/scheduled-tasks)
* 功能介绍

  + [内置 DNS 服务](/features/dns-server)
  + [为局域网设备提供代理](/features/provide-proxy-to-lan-device)
  + [服务提供商订阅](/features/service-provider-subscription)
  + [网络性能增强](/features/network-performance-enhance)
  + [按需启动](/features/on-demand)
* [Stash Mac](/stash-mac)
* 常见问题

  + [编写高效配置](/faq/effective-stash)
  + [防止代理被检测](/faq/proxy-detected)
  + [授权与激活](/faq/license-activation)
  + [TestFlight 相关](/faq/testflight)
  + [IPv6 兼容性](/faq/ipv6-compatible)
  + [URL Schema](/faq/url-schema)
  + [越狱修改内存限制](/faq/jailbreak-ios-memory-limit)
  + [无法安装帮助程序 (Helper)](/faq/stash-mac-helper)
  + [Stash 与其他 VPN 冲突](/faq/conflict-with-vpn)

On This Page

* [Shadowsocks / Shadowsocks2022](#shadowsocks--shadowsocks2022)
* [Shadowsocks Plugin](#shadowsocks-plugin)
* [ShadowsocksR](#shadowsocksr)
* [SOCKS5](#socks5)
* [HTTP](#http)
* [VMess](#vmess)
* [Snell](#snell)
* [Trojan](#trojan)
* [Hysteria](#hysteria)
* [Hysteria2](#hysteria2)
* [VLESS](#vless)
* [TUIC](#tuic)
* [Juicity](#juicity)
* [WireGuard](#wireguard)
* [SSH](#ssh)
* [DIRECT with Specified Interface](#direct-with-specified-interface)

代理协议

协议类型

# 协议类型

Stash 支持多种类型的代理协议，可以代理 TCP / UDP 协议。

每个代理必须含有以下参数：

* `name`：代理名称，每个代理的名称是唯一的。
* `type`：代理类型。
* `server`：服务器地址，可以是域名或者 IP 地址。
* `port`：端口。

---

代理可能支持以下参数：

* `tls`：布尔值，是否基于 TLS 转发。
* `skip-cert-verify`：布尔值，TLS 握手时是否忽略证书验证。
* `server-cert-fingerprint`：字符串，TLS 握手时验证服务器证书 SHA256 指纹，以 Hex 编码。
* `sni`：字符串，TLS 握手时候发送的 [Server Name Indication (opens in a new tab)](https://en.wikipedia.org/wiki/Server_Name_Indication)。若 `sni` 为空，默认为 `server` 字段。
* `alpn`：字符串数组，TLS 握手时候发送的 [Application-Layer Protocol Negotiation (ALPN) (opens in a new tab)](https://developer.mozilla.org/en-US/docs/Glossary/ALPN)。
* `interface-name`：绑定网卡出口，仅在 macOS 支持。

---

此外，对于单个代理的延迟测试，支持修改以下参数：

* `benchmark-url`：延迟测试使用的 URL，默认为 `http://www.apple.com/`。
* `benchmark-timeout`：延迟测试超时，单位秒，默认为 5 秒。
* `benchmark-disabled`：设置为 `true` 时完全禁用延迟测试。

你可以访问[这里](/proxy-protocols/proxy-benchmark)找到更多关于测试代理延迟的信息。

---

对于基于 QUIC 的协议，支持定期更改端口以应对 ISP 针对单个端口的限速，这一方法又称为端口跳跃。

* `ports`：字符串，支持多个端口或端口范围，以逗号分隔，例如 `443,8443,5000-6000`。
* `hop-interval`：整数，端口跳跃间隔，单位秒，默认为 30 秒。

---

在处理 UDP 时，为了最大程度地兼容各种协议的行为，只会向代理以 IP 地址的形式转发，而不会像 TCP 一样将域名解析交由代理处理。因此在发起 UDP 转发请求前，Stash 会尝试通过代理发起 DNS 查询，以获取正确的、符合 CDN 优化的 DNS 解析，再以此地址转发 UDP 包。

Stash 默认使用 1.0.0.1 进行 DNS 查询，你可以通过以下参数修改：

* `udp-nameserver`：数组，DNS 服务器地址，仅支持 UDP 协议。

例如：

```
name: proxy
type: ss
udp-nameserver: ['8.8.4.4', '8.8.8.8:53']
# ...
```

---

不同类型的代理还需要指定一些参数，可以参考下文。

## Shadowsocks / Shadowsocks2022

```
name: ss1
type: ss
server: server
port: 443
cipher: chacha20-ietf-poly1305
password: 'password'
udp: true
plugin: null
plugin-opts:
  mode:
  host:
```

支持以下的加密方式（cipher）：

* `aes-128-gcm`
* `aes-192-gcm`
* `aes-256-gcm`
* `aes-128-cfb`
* `aes-192-cfb`
* `aes-256-cfb`
* `aes-128-ctr`
* `aes-192-ctr`
* `aes-256-ctr`
* `rc4-md5`
* `chacha20`
* `chacha20-ietf`
* `xchacha20`
* `chacha20-ietf-poly1305`
* `xchacha20-ietf-poly1305`
* `2022-blake3-aes-128-gcm`
* `2022-blake3-aes-256-gcm`

### Shadowsocks Plugin

支持以下的插件（plugin）：

`obfs`：使用 [simple-obfs (opens in a new tab)](https://github.com/shadowsocks/simple-obfs) 混淆 TCP 流量。

```
plugin: obfs
plugin-opts:
  mode: tls # 混淆模式，可以选择 http 或 tls
  host: bing.com # 混淆域名，需要和服务器配置保持一致
```

`v2ray-plugin`：使用 [v2ray-plugin (opens in a new tab)](https://github.com/shadowsocks/v2ray-plugin) 将流量承载在 WebSocket 上。

```
plugin: v2ray-plugin
plugin-opts:
  mode: websocket # 暂时不支持 QUIC 协议
  tls: true # wss
  skip-cert-verify: true # 不验证证书
  host: bing.com
  path: '/'
  headers: # 自定义请求头
    key: value
```

`shadow-tls`：使用 [shadow-tls (opens in a new tab)](https://github.com/ihciah/shadow-tls) 进行真实 TLS 握手的同时，可以直接使用某些大公司或机构的证书，而不需要自行签发。

⚠️

目前仅支持 Shadow TLS 的
[v2 (opens in a new tab)](https://github.com/ihciah/shadow-tls/blob/master/docs/protocol-zh.md) 和
[v3 (opens in a new tab)](https://github.com/ihciah/shadow-tls/blob/master/docs/protocol-v3-zh.md)
版本。

```
plugin: shadow-tls
plugin-opts:
  password: singalongsong
  host: weather-data.apple.com
  skip-cert-verify: false # 不验证证书
  version: 3 # 只支持 2 和 3
```

## ShadowsocksR

```
name: ssr
type: ssr
server: server
port: 443
cipher: chacha20-ietf
password: 'password'
obfs: ''
protocol: ''
obfs-param: ''
protocol-param: ''
```

支持的加密方式（cipher）与 Shadowsocks 相同。

支持的混淆方式（obfs）:

* `plain`
* `http_simple`
* `http_post`
* `random_head`
* `tls1.2_ticket_auth`
* `tls1.2_ticket_fastauth`

支持的协议（protocol）:

* `origin`
* `auth_sha1_v4`
* `auth_aes128_md5`
* `auth_aes128_sha1`
* `auth_chain_a auth_chain_b`

## SOCKS5

```
name: socks
type: socks5
server: server
port: 443
# username: username
# password: password
# tls: true
# skip-cert-verify: true
# udp: true
```

## HTTP

```
name: http
type: http
server: server
port: 443
headers:
  key: value
tls: true # https
skip-cert-verify: true
# username: username
# password: password
```

## VMess

```
name: vmess
type: vmess
server: server
port: 443
uuid: d0529668-8835-11ec-a8a3-0242ac120002
cipher: auto
alterId: 64
network:
```

支持加密方式（cipher）：

* `auto`
* `aes-128-gcm`
* `chacha20-poly1305`
* `none`

支持的承载网络（network）：

* `ws`
* `h2`
* `http`
* `grpc`

```
network: ws
ws-opts:
  path: /path
  headers:
    Host: v2ray.com
  max-early-data: 2048
  early-data-header-name: Sec-WebSocket-Protocol
```

```
network: h2
tls: true
h2-opts:
  host:
    - http.example.com
    - http-alt.example.com
  path: /
```

## Snell

```
name: snell
type: snell
server: server
port: 443
psk: yourpsk
udp: true # 需要 v3 以上服务端
version: 3
# obfs-opts:
# mode: http # 或 tls
# host: bing.com
```

Snell UDP 需要 v3 版本以上的服务端支持。

支持的混淆模式（obfs-opts.mode）支持：

* http
* tls

## Trojan

```
name: trojan
type: trojan
server: server
port: 443
password: yourpassword
# udp: true
# sni: example.com # Server Name Indication，如果空会使用 server 中的值
# alpn:
#   - h2
#   - http/1.1
# skip-cert-verify: true
```

支持的承载网络（network）：

* `ws`
* `grpc`

## Hysteria

> Hysteria 是一个功能丰富的，专为恶劣网络环境进行优化的网络工具（双边加速），比如卫星网络、拥挤的公共 Wi-Fi、在中国连接国外服务器等。 基于修改版的 QUIC 协议。

Hysteria 服务端部署请[参考这里 (opens in a new tab)](https://github.com/HyNetwork/hysteria/wiki/%E4%B8%8B%E8%BD%BD%E5%AE%89%E8%A3%85)。

```
name: 'hysteria'
type: hysteria
server: server
port: 443
up-speed: 100 # 上传带宽（单位：Mbps）
down-speed: 100 # 下载带宽（单位：Mbps）
auth-str: your-password
# auth: aHR0cHM6Ly9oeXN0ZXJpYS5uZXR3b3JrL2RvY3MvYWR2YW5jZWQtdXNhZ2Uv # bytes encoded in base64
protocol: '' # udp / wechat-video
obfs: '' # obfs password
sni: example.com # Server Name Indication，如果空会使用 server 中的值
alpn:
  - hysteria
skip-cert-verify: true
```

上传、下行带宽单位为 Mbps，请尽量正确填写，超出实际带宽会有反效果。

外部链接：[base64 在线编码工具 (opens in a new tab)](https://www.base64decode.org/)。

## Hysteria2

⚠️

请注意，Hysteria 2 与 Hysteria 1.x
完全不兼容，两者差异请参考[官方说明 (opens in a new tab)](https://v2.hysteria.network/zh/docs/misc/2-vs-1/)。

Hysteria2 服务端部署请[参考这里 (opens in a new tab)](https://v2.hysteria.network/zh/docs/getting-started/Installation/)。

```
name: 'hysteria2'
type: hysteria2
server: server
port: 443
auth: your-password
fast-open: true
sni: example.com # Server Name Indication，如果空会使用 server 中的值
skip-cert-verify: true
up-speed: 100 # 上传带宽（可选的，单位：Mbps）
down-speed: 100 # 下载带宽（可选的，单位：Mbps）
```

## VLESS

XTLS 协议在 TLS 环境下摆脱冗余加密，提供更优秀的转发性能。

```
name: vless
type: vless
server: server
port: 443
uuid: d0529668-8835-11ec-a8a3-0242ac120002
# flow: xtls-rprx-direct
# skip-cert-verify: true
# network: h2
# tls: true
# ws-opts:
#   path: /path
#   headers:
#     Host: v2ray.com
# grpc-opts:
#   grpc-service-name: "example"
# h2-opts:
#   host:
#     - http.example.com
#     - http-alt.example.com
#   path: /
# reality-opts:
#   public-key:
#   short-id:
```

支持的 XTLS 模式（flow）：

* `xtls-rprx-origin`
* `xtls-rprx-direct`
* `xtls-rprx-splice`
* `xtls-rprx-vision`

## TUIC

TUIC 是一个轻量的基于 QUIC 的代理协议，由 rust 语言编写，目前支持 v4 和 v5 版本。你可以在[这里 (opens in a new tab)](https://github.com/tuic-protocol/tuic)找到更多信息。

```
name: tuic-v5
type: tuic
server: server
port: 443
version: 5
uuid: d0529668-8835-11ec-a8a3-0242ac120002 # for v5
password: your_password # for v5
skip-cert-verify: true
sni: ''
alpn:
  - h3
```

```
name: tuic-v4
type: tuic
server: server
port: 443
version: 4
token: 'your_token' # for v4
skip-cert-verify: true
sni: ''
alpn:
  - h3
```

💡

需要注意的是，Stash 客户端不支持 ALPN 为空，默认的 ALPN 为 h3。请在 TUIC 服务端加上 `--alpn h3` 参数。

请在服务端选择适合的拥塞控制算法 `--congestion-controller` 参数以充分利用带宽。

## Juicity

[Juicity (opens in a new tab)](https://github.com/juicity/juicity) 是一个基于 QUIC 的代理协议，受到 TUIC 的启发。

```
name: juicity
type: juicity
server: server
port: 443
uuid: d0529668-8835-11ec-a8a3-0242ac120002
password: your_password
skip-cert-verify: true
sni: ''
alpn:
  - h3
```

## WireGuard

[WireGuard (opens in a new tab)](https://www.wireguard.com/) 是一个高效的 Layer 3 的 VPN，Stash 支持将其作为 Layer 4 的代理使用，并支持通过其他协议转发 WireGuard 数据包。

```
name: wireguard
type: wireguard
server: server # domain is supported
port: 51820
ip: 10.8.4.8
# ipv6: fe80::e6bf:faff:fea0:9fae # optional
private-key: 0G6TTWwvgv8Gy5013/jv2GttkCLYYaNTArHV0NdNkGI= # client private key
public-key: 0ag+C+rINHBnvLJLUyJeYkMWvIAkBjQPPObicuBUn1U= # peer public key
# preshared-key: # optional
dns: [1.0.0.1, 223.6.6.6] # optional
# mtu: 1420 # optional
# reserved: [0, 0, 0] # optional
# keepalive: 45 # optional
# underlying-proxy: # optional
#   type: trojan
#   server: your-underlying-proxy
#   port: 443
#   password: your-password
```

💡

WireGuard 并非以高吞吐为设计目标的代理协议，Stash 需要在用户空间完成 Layer 3
与 Layer 4 的转换，其性能损耗会比常见代理协议大。在移动设备上，WireGuard
吞吐量一般会比 Layer4 代理协议低。

⚠️

若使用 `underlying-proxy`，其必须支持 UDP 中继，建议使用 UDP over TCP
的协议（如 Trojan、VLESS、VMess、Snell）。

## SSH

通过 [Secure Shell Protocol (SSH) (opens in a new tab)](https://en.wikipedia.org/wiki/Secure_Shell) 转发 TCP 流量，支持密码和密钥认证。

💡

由于 SSH 本身不支持转发 UDP 协议，Stash 无法通过 SSH 协议转发 UDP 流量。

```
name: ssh
type: ssh
server: server # domain is supported
port: 22
user: root
password: password
private-key: |
  -----BEGIN RSA PRIVATE KEY-----
  MIIEpAIBAAKCAQEA0G6TTWwvgv8Gy5013/jv2GttkCLYYaNTArHV0NdNkGI=
  ...
  -----END RSA PRIVATE KEY-----
private-key-passphrase: your-passphrase # optional
```

## DIRECT with Specified Interface

通过新建类型为 `direct` 的代理，并指定 `interface-name` 可以强制某些流量通过指定网卡，常用于解决 VPN 与 Stash 无法同时使用的情况。

例如，本机上的 OpenVPN 使用了 `utun3`，并且希望 `10.4.8.0/24` 都进入 `utun3` 而不是 macOS 的默认网卡。

```
name: my-corp-vpn
type: direct
interface-name: utun3
```

```
rules:
  - IP-CIDR,10.4.8.0/24,my-corp-vpn
```

💡

上述 `utun3` 请根据实际情况更改。

你可以使用 `netstat -rn | grep utun3` 查询 `utun3` 的静态路由表。

Last updated on 2025年5月5日

[规则集合](/rules/rule-set "规则集合")[策略组](/proxy-protocols/proxy-groups "策略组")

---

# 策略组

[Stash 用户文档易用且强劲的网络工具](/)

* [Stash 简介](/)
* [快速上手](/get-started)
* 更新日志

  + [iOS](/release-notes/ios)
* 分流规则

  + [规则类型](/rules/rule-types)
  + [规则集合](/rules/rule-set)
* 代理协议

  + [协议类型](/proxy-protocols/proxy-types)
  + [策略组](/proxy-protocols/proxy-groups)
  + [远程代理集](/proxy-protocols/proxy-providers)
  + [延迟测试](/proxy-protocols/proxy-benchmark)
* 配置文件

  + [配置样例](/configuration/example-config)
  + [覆写配置（Override）](/configuration/override)
  + [策略组图标](/configuration/proxy-group-icon)
* HTTP 引擎

  + [简介](/http-engine/intro)
  + [MitM](/http-engine/mitm)
  + [强制 HTTP 引擎](/http-engine/force-http-engine)
  + [HTTP 重写](/http-engine/rewrite)
* JavsScript 脚本

  + [语法与接口](/script/syntax-and-interface)
  + [改写 HTTP](/script/rewrite-requests)
  + [面板（Tile）](/script/tile)
  + [定时任务](/script/scheduled-tasks)
* 功能介绍

  + [内置 DNS 服务](/features/dns-server)
  + [为局域网设备提供代理](/features/provide-proxy-to-lan-device)
  + [服务提供商订阅](/features/service-provider-subscription)
  + [网络性能增强](/features/network-performance-enhance)
  + [按需启动](/features/on-demand)
* [Stash Mac](/stash-mac)
* 常见问题

  + [编写高效配置](/faq/effective-stash)
  + [防止代理被检测](/faq/proxy-detected)
  + [授权与激活](/faq/license-activation)
  + [TestFlight 相关](/faq/testflight)
  + [IPv6 兼容性](/faq/ipv6-compatible)
  + [URL Schema](/faq/url-schema)
  + [越狱修改内存限制](/faq/jailbreak-ios-memory-limit)
  + [无法安装帮助程序 (Helper)](/faq/stash-mac-helper)
  + [Stash 与其他 VPN 冲突](/faq/conflict-with-vpn)

On This Page

* [策略类型](#策略类型)
* [url-test](#url-test)
* [fallback](#fallback)
* [load-balance](#load-balance)
* [select](#select)
* [relay](#relay)
* [额外功能](#额外功能)
* [定时执行延迟测试](#定时执行延迟测试)
* [基于网络状态自动切换策略](#基于网络状态自动切换策略)
* [灵活地组合代理](#灵活地组合代理)

代理协议

策略组

# 策略组

策略组（`proxy-groups`）是一系列代理（或策略组）的组合。策略组可以像单个代理一样被分流规则引用，并可以指定特殊的策略提高可用性。

* 分流规则可以直接引用代理或策略组，但不能引用远程代理集
* 策略组可以包含多个代理，或者多个远程代理集
* 策略组可以包含另一个策略组
* 不包含任何代理的策略组，会被当作为 `DIRECT` 策略处理
* 支持 `filter` 字段，通过正则表达式过滤节点
* 可以通过 `include-all: true` 引用所有的代理和远程代理集

[(opens in a new tab)](https://mermaid.live/edit#pako:eNqNjz0OwjAMha8SeW4ukIEJNiZYvViNaSOaH7kJIqp6dwIqSAxILNbz9-wne4E-WgYDg1Aa1fGEAUOSeHc8K6136qmrHiSWNH87UibeUNWt3pxl-bX07v6xX8HQgWfx5Gw7bsGgFEIe2TOCadKSXBEwrG2OSo7nGnowWQp3UJKlzHtH7ScP5kLT_KEH63KUDa4PpRlbCA)

## 策略类型

💡

策略组内代理的排序方式默认为配置文件顺序，可以在「网络设置」页面改为按延迟测试结果排序。

### `url-test`

`url-test` 可以定时对包含的代理执行连通性检查，自动选择延迟最短的服务器，不健康的代理会被跳过。

```
- name: auto
  type: url-test
  proxies:
    - ss1
    - ss2
    - vmess
  interval: 300
```

### `fallback`

`fallback` 可以尽量按照用户书写的服务器顺序，在确保服务器可用的情况下，由上至下自动选择服务器，不健康的代理会被跳过。

```
- name: fallback-auto
  type: fallback
  proxies:
    - ss1
    - ss2
    - vmess
```

### `load-balance`

`load-balance` 能充分利用多个代理的带宽，不健康的代理会被跳过。

```
- name: load-balance
  type: load-balance
  strategy: # consistent-hashing / round-robin
  proxies:
    - ss1
    - ss2
    - vmess
```

一般建议将 `strategy` 设置为 `consistent-hashing`，避免频繁改变 IP 触发服务端的安全策略。

### `select`

`select` 用来允许用户手动选择。

```
- name: select
  type: select
  proxies:
    - ss1
    - ss2
    - vmess
    - auto
```

### `relay`

代理的转发链，流量将通过一系列的代理转发到达目的地，仅支持转发 TCP 或使用 UDP over TCP 的协议。`relay` 策略组并不受到内部代理延迟测试的结果影响，需要单独指定测试 URL。

```
- name: relay
  type: relay
  benchmark-url: http://www.apple.com # 建议只使用HTTP协议
  benchmark-timeout: 5 # 延迟测试超时，单位：秒
  # 流量: stash <-> http <-> vmess <-> ss1 <-> ss2 <-> 互联网
  proxies:
    - http
    - vmess
    - ss1
    - ss2
```

💡

如果 `relay` 策略组内的代理无法直接被访问，可以对这些代理配置
`benchmark-disabled: true` 禁用 Stash 对它发起单独的延迟测试。

## 额外功能

### 定时执行延迟测试

Stash 默认会每 600 秒为策略组内包含的代理进行延迟测试，如果策略组包含另外一个策略组，则会递归进行测试。

定时执行延迟测试支持修改下述配置：

* `interval`：单位秒，按一定间隔执行延迟测试，默认为 600 秒，设置为负数则不进行延迟测试。
* `lazy`：懒惰模式，如果设置为 `true`，且策略组在过去一段时间没有被使用，Stash 会跳过自动延迟测试以节省资源。

```
proxy-groups:
  - name: my-proxy-group
    type: select
    # ...
    interval: 300 # 每 300s 检查一次
    lazy: true # 在策略组没有被使用时候，不进行延迟测试
```

### 基于网络状态自动切换策略

`select` 类型的策略组可以根据设备的 SSID / 蜂窝数据自动切换策略。

`default` 和 `cellular` 是两个可选的保留策略：

* 当在 Wi-Fi 环境下，没有匹配到任何 SSID 时，会自动切换到 `default` 对应的代理；
* 在蜂窝数据下，会自动切换到 `cellular` 对应的代理；
* 当没有 `default` 或 `cellular` 时候，不会触发任何操作。

```
- name: ssid-group
  type: select # 类型必须为 select，兼容原版 clash 配置
  proxies:
    - ss1
    - ss2
    - ss3
    - DIRECT
  ssid-policy:
    # 在 SSID 为 office 的 Wi-Fi 中自动切换为 ss1 策略
    # 在 SSID 为 home 的 Wi-Fi 中自动切换为 ss2 策略
    # 在蜂窝数据中自动切换为 ss3 策略
    # 其他的 SSID 默认为 DIRECT
    office: ss1
    home: ss2
    cellular: ss3
    default: DIRECT
```

### 灵活地组合代理

Stash 支持各种方式将多个代理组合成一个策略组。

* 可以通过 `include-all: true` 引用所有的代理和远程代理集
* 不包含任何代理的策略组，会被当作为 `DIRECT` 策略处理。
* 支持 `filter` 字段，通过正则表达式过滤节点

```
proxy-groups:
  - name: my-hongkong-group
    type: select
    include-all: true # 引用所有 proxies & proxy-providers
    filter: 'HK|香港' # 筛选含有 HK 或香港关键字的代理
```

Last updated on 2025年4月9日

[协议类型](/proxy-protocols/proxy-types "协议类型")[远程代理集](/proxy-protocols/proxy-providers "远程代理集")

---

# 远程代理集

[Stash 用户文档易用且强劲的网络工具](/)

* [Stash 简介](/)
* [快速上手](/get-started)
* 更新日志

  + [iOS](/release-notes/ios)
* 分流规则

  + [规则类型](/rules/rule-types)
  + [规则集合](/rules/rule-set)
* 代理协议

  + [协议类型](/proxy-protocols/proxy-types)
  + [策略组](/proxy-protocols/proxy-groups)
  + [远程代理集](/proxy-protocols/proxy-providers)
  + [延迟测试](/proxy-protocols/proxy-benchmark)
* 配置文件

  + [配置样例](/configuration/example-config)
  + [覆写配置（Override）](/configuration/override)
  + [策略组图标](/configuration/proxy-group-icon)
* HTTP 引擎

  + [简介](/http-engine/intro)
  + [MitM](/http-engine/mitm)
  + [强制 HTTP 引擎](/http-engine/force-http-engine)
  + [HTTP 重写](/http-engine/rewrite)
* JavsScript 脚本

  + [语法与接口](/script/syntax-and-interface)
  + [改写 HTTP](/script/rewrite-requests)
  + [面板（Tile）](/script/tile)
  + [定时任务](/script/scheduled-tasks)
* 功能介绍

  + [内置 DNS 服务](/features/dns-server)
  + [为局域网设备提供代理](/features/provide-proxy-to-lan-device)
  + [服务提供商订阅](/features/service-provider-subscription)
  + [网络性能增强](/features/network-performance-enhance)
  + [按需启动](/features/on-demand)
* [Stash Mac](/stash-mac)
* 常见问题

  + [编写高效配置](/faq/effective-stash)
  + [防止代理被检测](/faq/proxy-detected)
  + [授权与激活](/faq/license-activation)
  + [TestFlight 相关](/faq/testflight)
  + [IPv6 兼容性](/faq/ipv6-compatible)
  + [URL Schema](/faq/url-schema)
  + [越狱修改内存限制](/faq/jailbreak-ios-memory-limit)
  + [无法安装帮助程序 (Helper)](/faq/stash-mac-helper)
  + [Stash 与其他 VPN 冲突](/faq/conflict-with-vpn)

On This Page

* [快捷引用远程代理集](#快捷引用远程代理集)

代理协议

远程代理集

# 远程代理集

在配置文件直接声明的代理，无法在后台自动更新。我们更推荐使用远程代理集（proxy-provider），能在后台自动从 URL 更新策略组。

要使用远程代理集，需要在 `proxy-providers` 下定义，并在 `proxy-groups` 中引用。

```
proxy-providers:
  provider-a:
    url: https://raw.githubusercontent.com/STASH-NETWORKS-LIMITED/stash-example/main/config.yaml
    interval: 3600
    filter: 'example'

  provider-b:
    url: https://raw.githubusercontent.com/STASH-NETWORKS-LIMITED/stash-example/main/config.yaml
    interval: 3600

proxy-groups:
  - name: auto
    type: url-test
    interval: 300
    use:
      - provider-a # reference to provider-a
      - provider-b # reference to provider-b
```

一个合法的远程代理集必须包含 `proxies` 字段：

```
proxies:
  - name: 'ss1'
    type: ss
    server: server
    port: 443
    cipher: AEAD_CHACHA20_POLY1305
    password: 'password'
  - name: 'ss2'
    type: ss
    server: server
    port: 443
    cipher: AEAD_CHACHA20_POLY1305
    password: 'password'
```

远程代理集支持通过 `filter` 字段，使用正则表达式过滤代理名。远程代理集为空时候，会以 `DIRECT` 替代。

### 快捷引用远程代理集

Stash 也支持通过 `use-url` 在策略组中快捷引用远程代理集，此时不可指定更新时间和名称。

```
proxy-groups:
  - name: auto
    type: url-test
    interval: 300
    use-url:
      - https://raw.githubusercontent.com/STASH-NETWORKS-LIMITED/stash-example/main/config.yaml
```

Last updated on 2023年3月13日

[策略组](/proxy-protocols/proxy-groups "策略组")[延迟测试](/proxy-protocols/proxy-benchmark "延迟测试")

---

# 延迟测试

[Stash 用户文档易用且强劲的网络工具](/)

* [Stash 简介](/)
* [快速上手](/get-started)
* 更新日志

  + [iOS](/release-notes/ios)
* 分流规则

  + [规则类型](/rules/rule-types)
  + [规则集合](/rules/rule-set)
* 代理协议

  + [协议类型](/proxy-protocols/proxy-types)
  + [策略组](/proxy-protocols/proxy-groups)
  + [远程代理集](/proxy-protocols/proxy-providers)
  + [延迟测试](/proxy-protocols/proxy-benchmark)
* 配置文件

  + [配置样例](/configuration/example-config)
  + [覆写配置（Override）](/configuration/override)
  + [策略组图标](/configuration/proxy-group-icon)
* HTTP 引擎

  + [简介](/http-engine/intro)
  + [MitM](/http-engine/mitm)
  + [强制 HTTP 引擎](/http-engine/force-http-engine)
  + [HTTP 重写](/http-engine/rewrite)
* JavsScript 脚本

  + [语法与接口](/script/syntax-and-interface)
  + [改写 HTTP](/script/rewrite-requests)
  + [面板（Tile）](/script/tile)
  + [定时任务](/script/scheduled-tasks)
* 功能介绍

  + [内置 DNS 服务](/features/dns-server)
  + [为局域网设备提供代理](/features/provide-proxy-to-lan-device)
  + [服务提供商订阅](/features/service-provider-subscription)
  + [网络性能增强](/features/network-performance-enhance)
  + [按需启动](/features/on-demand)
* [Stash Mac](/stash-mac)
* 常见问题

  + [编写高效配置](/faq/effective-stash)
  + [防止代理被检测](/faq/proxy-detected)
  + [授权与激活](/faq/license-activation)
  + [TestFlight 相关](/faq/testflight)
  + [IPv6 兼容性](/faq/ipv6-compatible)
  + [URL Schema](/faq/url-schema)
  + [越狱修改内存限制](/faq/jailbreak-ios-memory-limit)
  + [无法安装帮助程序 (Helper)](/faq/stash-mac-helper)
  + [Stash 与其他 VPN 冲突](/faq/conflict-with-vpn)

On This Page

* [延迟测试方式](#延迟测试方式)

代理协议

延迟测试

# 延迟测试

在 Stash 中，你可以为每个代理指定单独的延迟测试参数，包括：延迟测试目标 URL 和测试的超时时间。

延迟测试超时的代理会被标记为不健康。

```
proxies:
  - name: your-proxy
    type: ss
    server: server
    port: 443
    benchmark-url: http://www.apple.com # 建议只使用 HTTP 协议
    benchmark-timeout: 5 # 延迟测试超时时间，单位：秒
    benchmark-disabled: false # 设置为 `true` 时完全禁用延迟测试
```

💡

如果一个代理被多个策略组引用，多个策略组会共享这个代理的延迟测试结果。若希望一个代理在不同的策略组使用不同的延迟测试参数，请手动创建多个代理。

## 延迟测试方式

Stash 支持多种方式对代理进行延迟测试，包括：

* `UDP`：使用 UDP 报文进行延迟测试
* `TCP`：使用 TCP 握手进行延迟测试（对基于 UDP 的协议如 QUIC 无效）
* `HTTP HEAD`：默认方式，通过代理发送 HTTP HEAD 请求进行延迟测试

Last updated on 2025年4月9日

[远程代理集](/proxy-protocols/proxy-providers "远程代理集")[配置样例](/configuration/example-config "配置样例")

---

# 配置样例

[Stash 用户文档易用且强劲的网络工具](/)

* [Stash 简介](/)
* [快速上手](/get-started)
* 更新日志

  + [iOS](/release-notes/ios)
* 分流规则

  + [规则类型](/rules/rule-types)
  + [规则集合](/rules/rule-set)
* 代理协议

  + [协议类型](/proxy-protocols/proxy-types)
  + [策略组](/proxy-protocols/proxy-groups)
  + [远程代理集](/proxy-protocols/proxy-providers)
  + [延迟测试](/proxy-protocols/proxy-benchmark)
* 配置文件

  + [配置样例](/configuration/example-config)
  + [覆写配置（Override）](/configuration/override)
  + [策略组图标](/configuration/proxy-group-icon)
* HTTP 引擎

  + [简介](/http-engine/intro)
  + [MitM](/http-engine/mitm)
  + [强制 HTTP 引擎](/http-engine/force-http-engine)
  + [HTTP 重写](/http-engine/rewrite)
* JavsScript 脚本

  + [语法与接口](/script/syntax-and-interface)
  + [改写 HTTP](/script/rewrite-requests)
  + [面板（Tile）](/script/tile)
  + [定时任务](/script/scheduled-tasks)
* 功能介绍

  + [内置 DNS 服务](/features/dns-server)
  + [为局域网设备提供代理](/features/provide-proxy-to-lan-device)
  + [服务提供商订阅](/features/service-provider-subscription)
  + [网络性能增强](/features/network-performance-enhance)
  + [按需启动](/features/on-demand)
* [Stash Mac](/stash-mac)
* 常见问题

  + [编写高效配置](/faq/effective-stash)
  + [防止代理被检测](/faq/proxy-detected)
  + [授权与激活](/faq/license-activation)
  + [TestFlight 相关](/faq/testflight)
  + [IPv6 兼容性](/faq/ipv6-compatible)
  + [URL Schema](/faq/url-schema)
  + [越狱修改内存限制](/faq/jailbreak-ios-memory-limit)
  + [无法安装帮助程序 (Helper)](/faq/stash-mac-helper)
  + [Stash 与其他 VPN 冲突](/faq/conflict-with-vpn)

配置文件

配置样例

# 配置样例

Stash 所有的配置文件均使用 [YAML (opens in a new tab)](https://yaml.org/) 格式。在 YAML 格式中，缩进影响了整个配置的结构，用户可以在 [www.yamllint.com (opens in a new tab)](http://www.yamllint.com/) 检查配置是否符合 YAML 格式。

Stash 配置由单个配置文件和若干个[覆写文件](/configuration/override)组成，配置文件是必须的，覆写文件是可选的。覆写的优先级高于配置文件，覆写文件中的字段会覆盖配置文件中的字段。用户可以通过配置和覆写的组合，打造符合自己需求的配置。

虽然配置文件是必须的，但其中每一个字段都有默认值，用户仅需要填写希望更改的字段即可。

```
# 规则模式：rule（规则） / global（全局代理）/ direct（全局直连）
mode: rule

# 5 个级别：silent / info / warning / error / debug。级别越高日志输出量越大，越倾向于调试，若需要请自行开启。
log-level: info

http:
  # 强制使用 HTTP 引擎处理 TCP 连接
  # 捕获后的连接可以使用高级功能，例如重写和脚本
  force-http-engine:
    - '*:80'

  # 以 PKCS #12 编码的 CA 证书
  ca: ''
  # 证书密码
  ca-passphrase: ''
  # 开启中间人攻击（MitM）功能的域名列表，需要确保上述 CA 证书已受系统信任
  mitm:
    - g.cn
    - '*.google.cn'
    - weather-data.apple.com # 默认只对 443 端口开启
    - weather-data.apple.com:* # 使用通配符对所有端口开启
    - '*.weather-data.apple.com' # 域名中也可以使用通配符
    - '-exclude.weather-data.apple.com' # 用-前缀排除域名

  # HTTP(S) 重写，支持 header、302、307、reject 多种策略
  url-rewrite:
    - ^http://g\.cn http://www.google.com header # 重写请求头的域名
    - ^https?://www\.google\.cn https://www.google.com 302 # 直接返回一个 302 重定向的响应
    - ^https?://ad\.example - reject # 拒绝请求

  # 使用 JavaScript 脚本改写 HTTP(S) 请求
  script:
    - match: https://weather-data.apple.com/v2/weather/[\w-]+/-?[0-9]+\.[0-9]+/-?[0-9]+\.[0-9]+\?
      name: weather-us-aqi # 引用 script-providers 中的脚本
      type: response # 脚本类型：request / response
      require-body: true # 如果需要 request / response body，请设置为 true
      timeout: 10 # 脚本超时时间（秒，可选）
      argument: '' # 脚本参数（可选）
      debug: false # 开发模式，每次执行前会从 provider 加载最新脚本
      binary-mode: false # 以二进制模式获取 body
      max-size: 1048576 # 1MB

# 定时任务
cron:
  # 定时执行 JavaScript 脚本
  script:
    - name: weather-us-aqi # 引用 script-providers 中的脚本
      cron: '* * * * *' # cron 表达式，可以在 https://crontab.guru/ 获取更多介绍
      timeout: 10 # 脚本超时时间（秒，可选）
      argument: '' # 脚本参数（可选）
      debug: false # 开发模式，每次执行前会从 provider 加载最新脚本

script-providers:
  weather-us-aqi:
    url: https://example.org/stash/script.js
    interval: 86400

script:
  shortcuts: # 使用表达式编写自定义规则
    quic: network == 'udp' and (dst_port == 443 or dst_port == 4483 or dst_port == 9305) # 可以在规则中引用

# 支持通配符域名（例如: *.clash.dev, *.foo.*.example.com）
# 不使用通配符的域名优先级高于使用通配符的域名（例如: foo.example.com > *.example.com > .example.com）
# 注意: +.foo.com 的效果等同于 .foo.com 和 foo.com
hosts:
  '*.clash.dev': 127.0.0.1
  '.dev': 127.0.0.1
  'alpha.clash.dev': '::1'

# DNS 服务器配置
dns:
  # 以下填写的 DNS 服务器将会被用来解析 DNS 服务的域名
  # 仅填写 DNS 服务器的 IP 地址
  default-nameserver:
    - 223.5.5.5
    - 114.114.114.114
    - system # 使用 iOS 系统 DNS
  # 支持 UDP / TCP / DoT / DoH 协议的 DNS 服务，可以指明具体的连接端口号。
  # 所有 DNS 请求将会直接发送到服务器，不经过任何代理。
  # Stash 会使用最先获得的解析记录回复 DNS 请求
  nameserver:
    # 不建议配置超过 2 个 DNS 服务器，会增加系统功耗
    - https://doh.pub/dns-query
    - https://dns.alidns.com/dns-query
    - quic://dns.adguard.com:853
    - doq://test.dns.nextdns.io:853
    - system # 使用系统 DNS

  # 跳过证书验证，解决部分兼容性问题 https://help.nextdns.io/t/g9hdkjz
  skip-cert-verify: true

  # 对部分域名使用单独的 DNS 服务器
  nameserver-policy:
    'www.baidu.com': 114.114.114.114
    '+.internal.crop.com': system

  # 在以下列表的域名将不会被解析为 fake ip，这些域名相关的解析请求将会返回它们真实的 IP 地址
  fake-ip-filter:
    - '+.stun.*.*'
    - '+.stun.*.*.*'
    - '+.stun.*.*.*.*'
    - '+.stun.*.*.*.*.*'

    # Google Voices
    - 'lens.l.google.com'

    # Nintendo Switch
    - '*.n.n.srv.nintendo.net'

    # PlayStation
    - '+.stun.playstation.net'

    # XBox
    - 'xbox.*.*.microsoft.com'
    - '*.*.xboxlive.com'

    # Microsoft
    - '*.msftncsi.com'
    - '*.msftconnecttest.com'

proxies:
  # shadowsocks
  # 支持加密方式：
  #   aes-128-gcm aes-192-gcm aes-256-gcm
  #   aes-128-cfb aes-192-cfb aes-256-cfb
  #   aes-128-ctr aes-192-ctr aes-256-ctr
  #   rc4-md5 chacha20 chacha20-ietf xchacha20
  #   chacha20-ietf-poly1305 xchacha20-ietf-poly1305
  - name: 'ss1'
    type: ss
    server: server
    port: 443
    benchmark-url: http://www.apple.com
    benchmark-timeout: 5
    cipher: chacha20-ietf-poly1305
    password: 'password'

  - name: 'ss2'
    type: ss
    server: server
    port: 443
    benchmark-url: http://www.apple.com
    benchmark-timeout: 5
    cipher: AEAD_CHACHA20_POLY1305
    password: 'password'
    plugin: obfs
    plugin-opts:
      mode: tls # 混淆模式，可以选择 http 或 tls
      host: bing.com # 混淆域名，需要和服务器配置保持一致

  - name: 'ss3'
    type: ss
    server: server
    port: 443
    benchmark-url: http://www.apple.com
    benchmark-timeout: 5
    cipher: AEAD_CHACHA20_POLY1305
    password: 'password'
    plugin: v2ray-plugin
    plugin-opts:
      mode: websocket # 暂时不支持 QUIC 协议
      tls: true # wss
      skip-cert-verify: true
      host: bing.com
      path: '/'
      headers:
        custom: value

  # vmess
  # 支持加密方式：auto / aes-128-gcm / chacha20-poly1305 / none
  - name: 'vmess'
    type: vmess
    server: server
    port: 443
    benchmark-url: http://www.apple.com
    benchmark-timeout: 5
    uuid: d0529668-8835-11ec-a8a3-0242ac120002
    alterId: 32
    cipher: auto
    tls: true
    skip-cert-verify: true
    servername: example.com # 优先级高于 wss host
    network: ws
    ws-opts:
      path: /path
      headers:
        Host: v2ray.com
      max-early-data: 2048
      early-data-header-name: Sec-WebSocket-Protocol

  # socks5
  - name: 'socks'
    type: socks5
    server: server
    port: 443
    benchmark-url: http://www.apple.com
    benchmark-timeout: 5
    username: username
    password: password
    tls: true
    skip-cert-verify: true

  # http
  - name: 'http'
    type: http
    server: server
    port: 443
    benchmark-url: http://www.apple.com
    benchmark-timeout: 5
    username: username
    password: password
    tls: true # https
    skip-cert-verify: true

  # snell
  - name: 'snell'
    type: snell
    server: server
    port: 44046
    benchmark-url: http://www.apple.com
    benchmark-timeout: 5
    psk: yourpsk
    version: 3
    obfs-opts:
      mode: http # 或 tls
      host: bing.com

  # Trojan
  - name: 'trojan'
    type: trojan
    server: server
    port: 443
    benchmark-url: http://www.apple.com
    benchmark-timeout: 5
    password: yourpsk
    sni: example.com # Server Name Indication，如果为空会使用 server 中的值
    alpn:
      - h2
      - http/1.1
    skip-cert-verify: true

  # hysteria https://github.com/HyNetwork/hysteria/wiki/%E9%AB%98%E7%BA%A7%E7%94%A8%E6%B3%95
  - name: 'hysteria'
    type: hysteria
    server: server
    port: 443
    benchmark-url: http://www.apple.com
    benchmark-timeout: 5
    up-speed: 100 # 上传带宽（单位：Mbps）
    down-speed: 100 # 下载带宽（单位：Mbps）
    auth-str: your-password
    # auth: aHR0cHM6Ly9oeXN0ZXJpYS5uZXR3b3JrL2RvY3MvYWR2YW5jZWQtdXNhZ2Uv # bytes encoded in base64
    protocol: '' # udp / wechat-video
    obfs: '' # obfs password
    sni: example.com # Server Name Indication，如果为空会使用 server 中的值
    alpn:
      - hysteria
    skip-cert-verify: true

  # ShadowsocksR
  # 支持的加密方式: SS 中支持的所有流加密方式
  # 支持的混淆方式:
  #   plain http_simple http_post
  #   random_head tls1.2_ticket_auth tls1.2_ticket_fastauth
  # 支持的协议:
  #   origin auth_sha1_v4 auth_aes128_md5
  #   auth_aes128_sha1 auth_chain_a auth_chain_b
  - name: 'ssr'
    type: ssr
    server: server
    port: 443
    benchmark-url: http://www.apple.com
    benchmark-timeout: 5
    cipher: chacha20-ietf
    password: 'password'
    obfs: tls1.2_ticket_auth
    protocol: auth_sha1_v4
    obfs-param: domain.tld
    protocol-param: '#'

  - name: 'vless'
    type: vless
    server: server
    port: 443
    benchmark-url: http://www.apple.com
    benchmark-timeout: 5
    uuid: d0529668-8835-11ec-a8a3-0242ac120002
    flow: xtls-rprx-direct
    skip-cert-verify: true
    network: h2
    tls: true
    ws-opts:
      path: /path
      headers:
        Host: v2ray.com
    grpc-opts:
      grpc-service-name: 'example'
    h2-opts:
      host:
        - http.example.com
        - http-alt.example.com
      path: /

proxy-groups:
  # 代理的转发链, 在 proxies 中不应该包含 relay. 不支持 UDP.
  # 流量: clash <-> http <-> vmess <-> ss1 <-> ss2 <-> 互联网
  - name: 'relay'
    type: relay
    icon: https://raw.githubusercontent.com/Koolson/Qure/master/IconSet/Color/Direct.png
    proxies:
      - http
      - vmess
      - ss1
      - ss2

  # url-test 可以自动选择延迟最短的服务器
  - name: 'auto'
    type: url-test
    proxies:
      - ss1
      - ss2
      - vmess
    interval: 300

  # fallback 可以尽量按照用户书写的服务器顺序，在确保服务器可用的情况下，自动选择服务器
  - name: 'fallback-auto'
    type: fallback
    proxies:
      - ss1
      - ss2
      - vmess
    interval: 300

  # load-balance 可以使相同 eTLD 请求在同一条代理线路上
  - name: 'load-balance'
    type: load-balance
    proxies:
      - ss1
      - ss2
      - vmess
    interval: 300

  # select 用于允许用户手动选择代理服务器或服务器组
  # 您也可以使用 RESTful API 去切换服务器，这种方式推荐在 GUI 中使用
  - name: Proxy
    type: select
    proxies:
      - ss1
      - ss2
      - vmess
      - auto

  # 基于 SSID 的策略，方便在特殊网络环境下使用特定的代理
  - name: ssid-group
    type: select # 类型必须为 select，兼容原版 clash 配置
    proxies:
      - ss1
      - ss2
      - DIRECT
    ssid-policy:
      # 在 SSID 为 office 的 Wi-Fi 中自动切换为 ss1 策略
      # 在 SSID 为 home 的 Wi-Fi 中自动切换为 ss2 策略
      # 在蜂窝数据中自动切换为 ss3 策略
      # 其他的 SSID 默认为 DIRECT
      office: ss1
      home: ss2
      cellular: ss3
      default: DIRECT

  - name: UseProvider
    type: select
    use:
      - provider1
    proxies:
      - Proxy
      - DIRECT

proxy-providers:
  provider1:
    url: https://example.org/stash/config.yaml
    interval: 3600

rule-providers:
  proxy-domain:
    behavior: domain # 使用 domain 类规则集，可以使匹配更高效
    url: https://cdn.jsdelivr.net/gh/Loyalsoldier/clash-rules@release/proxy.txt
    interval: 86400

  proxy-domain-text:
    behavior: domain-text # 推荐使用 text 格式，解析更高效
    url: https://cdn.jsdelivr.net/gh/Loyalsoldier/surge-rules@release/proxy.txt
    interval: 86400

  lan-cidr:
    behavior: ipcidr
    url: https://cdn.jsdelivr.net/gh/Loyalsoldier/clash-rules@release/lancidr.txt
    interval: 86400

  ip-cidr-text:
    behavior: ipcidr-text
    url: https://cdn.jsdelivr.net/gh/17mon/china_ip_list@master/china_ip_list.txt
    interval: 86400

  apple-direct:
    behavior: classical # 不推荐使用 classical 类规则集
    url: https://cdn.jsdelivr.net/gh/Hackl0us/SS-Rule-Snippet@master/Rulesets/Clash/Basic/Apple-direct.yaml
    interval: 3600

rules:
  - SCRIPT,quic,REJECT,no-track
  - RULE-SET,proxy-domain,Proxy
  - RULE-SET,apple-direct,DIRECT
  - RULE-SET,lan-cidr,DIRECT
  - RULE-SET,ip-cidr-text,DIRECT
  - GEOIP,CN,DIRECT
  - MATCH,Proxy
```

Last updated on 2025年4月9日

[延迟测试](/proxy-protocols/proxy-benchmark "延迟测试")[覆写配置（Override）](/configuration/override "覆写配置（Override）")

---

# 覆写文件（Override）

[Stash 用户文档易用且强劲的网络工具](/)

* [Stash 简介](/)
* [快速上手](/get-started)
* 更新日志

  + [iOS](/release-notes/ios)
* 分流规则

  + [规则类型](/rules/rule-types)
  + [规则集合](/rules/rule-set)
* 代理协议

  + [协议类型](/proxy-protocols/proxy-types)
  + [策略组](/proxy-protocols/proxy-groups)
  + [远程代理集](/proxy-protocols/proxy-providers)
  + [延迟测试](/proxy-protocols/proxy-benchmark)
* 配置文件

  + [配置样例](/configuration/example-config)
  + [覆写配置（Override）](/configuration/override)
  + [策略组图标](/configuration/proxy-group-icon)
* HTTP 引擎

  + [简介](/http-engine/intro)
  + [MitM](/http-engine/mitm)
  + [强制 HTTP 引擎](/http-engine/force-http-engine)
  + [HTTP 重写](/http-engine/rewrite)
* JavsScript 脚本

  + [语法与接口](/script/syntax-and-interface)
  + [改写 HTTP](/script/rewrite-requests)
  + [面板（Tile）](/script/tile)
  + [定时任务](/script/scheduled-tasks)
* 功能介绍

  + [内置 DNS 服务](/features/dns-server)
  + [为局域网设备提供代理](/features/provide-proxy-to-lan-device)
  + [服务提供商订阅](/features/service-provider-subscription)
  + [网络性能增强](/features/network-performance-enhance)
  + [按需启动](/features/on-demand)
* [Stash Mac](/stash-mac)
* 常见问题

  + [编写高效配置](/faq/effective-stash)
  + [防止代理被检测](/faq/proxy-detected)
  + [授权与激活](/faq/license-activation)
  + [TestFlight 相关](/faq/testflight)
  + [IPv6 兼容性](/faq/ipv6-compatible)
  + [URL Schema](/faq/url-schema)
  + [越狱修改内存限制](/faq/jailbreak-ios-memory-limit)
  + [无法安装帮助程序 (Helper)](/faq/stash-mac-helper)
  + [Stash 与其他 VPN 冲突](/faq/conflict-with-vpn)

On This Page

* [语法参考](#语法参考)
* [常见覆写示例](#常见覆写示例)
* [使用 #!replace 语法的覆写示例](#使用-replace-语法的覆写示例)
* [合并示例](#合并示例)

配置文件

覆写配置（Override）

# 覆写文件（Override）

覆写文件（Override）允许用户修改配置文件的部分字段，常用于修改托管、订阅的配置内容。Stash 支持同时启用多个覆写文件，配置将按照从上到下的顺序依次覆盖。

最佳实践建议：为便于单独控制开关和分享，建议按功能点划分覆写文件。

## 语法参考

* 覆写文件使用 YAML 格式，文件后缀为 `.stoverride`
* 通常使用 `name` 和 `desc` 字段作为覆写文件的名称和描述，这两个字段仅用于展示
* 覆写文件对配置文件的修改遵循以下规则：
  + 对于简单类型（string、number、boolean）的同名键，直接覆盖原值
  + 对于字典类型的同名键，采用递归键值合并
  + 对于数组类型的同名键，覆写文件的数组会插入到原数组前面
  + 对于字典类型和数组类型的键，若添加注释 `#!replace`，则采用完全覆盖方式合并

⚠️

当前版本暂不支持修改数组中的特定元素，后续版本将提供相关语法支持。

## 常见覆写示例

```
name: '📺 BiliBili: 🔀 Redirect'
desc: |-
  哔哩哔哩：重定向
  中国站CDN自定义
openUrl: 'http://boxjs.com/#/app/BiliBili.Redirect'
author: |-
  VirgilClyne[https://github.com/VirgilClyne]
homepage: 'https://Redirect.BiliUniverse.io'
icon: 'https://github.com/BiliUniverse/Redirect/raw/main/src/assets/icon_rounded.png'
category: '🪐 BiliUniverse'
date: '2024-12-10 07:13:21'
version: '0.2.12'

http:
  force-http-engine:
    - '*.bilivideo.cn:80'
    - '*.bilivideo.com:80'
    - upos-hz-mirrorakam.akamaized.net:80
    - '*:4480'
    - '*:8000'
    - '*:8082'
    - '*.mcdn.bilivideo.cn:9102'
  mitm:
    - '*.bilivideo.cn:443'
    - '*.bilivideo.com:443'
    - '*.mcdn.bilivideo.com:4483'
    - '*.mcdn.bilivideo.cn:4483'
    - '*.mcdn.bilivideo.cn:8082'
    - '*.mcdn.bilivideo.com:8082'
    - 'upos-*-mirrorakam.akamaized.net:443'
  script:
    - match: ^https?:\/\/.+\.bilivideo\.com\/upgcxcode\/
      name: '📺 BiliBili.Redirect.request'
      type: request
    - match: ^https?:\/\/(.+):(8000|8082)\/v1\/resource\/
      name: '📺 BiliBili.Redirect.request'
      type: request
      argument:
    - match: ^https?:\/\/[xy0-9]+\.mcdn\.bilivideo\.(cn|com):(4483|9102)\/upgcxcode\/
      name: '📺 BiliBili.Redirect.request'
      type: request
      argument:
    - match: ^https?:\/\/(.+):4480\/upgcxcode\/
      name: '📺 BiliBili.Redirect.request'
      type: request
      argument:
    - match: ^https?:\/\/upos-(hz|bstar1)-mirrorakam\.akamaized\.net/upgcxcode\/
      name: '📺 BiliBili.Redirect.request'
      type: request
      argument:
script-providers:
  '📺 BiliBili.Redirect.request':
    url: https://github.com/BiliUniverse/Redirect/releases/download/v0.2.12/request.bundle.js
    interval: 86400
```

## 使用 `#!replace` 语法的覆写示例

```
name: 仅使用 CloudFlare DNS
dns:
  # 将完全覆盖原有 default-nameserver
  default-nameserver: #!replace
    - system
    - 223.5.5.5
    - 1.0.0.1
  # 将完全覆盖原有 nameserver
  nameserver: #!replace
    - https://1.0.0.1/dns-query # CF IPv4
    - https://[2606:4700:4700::1111]/dns-query # CF IPv6
```

## 合并示例

原始配置文件 `config.yaml`：

```
dict:
  k1: true
  k2: 1
  k3:
    - 1
    - 2
    - 3
  k4:
    - 1
    - 2
    - 3
```

覆写文件：

```
key: value
dict:
  k3:
    - 0
  k4: #!replace
    - 1
  k5: null
```

合并后结果：

```
key: value
dict:
  k1: true
  k2: 1
  k3:
    - 0
    - 1
    - 2
    - 3
  k4:
    - 1
  k5: null
```

Last updated on 2025年4月6日

[配置样例](/configuration/example-config "配置样例")[策略组图标](/configuration/proxy-group-icon "策略组图标")

---

# 策略组图标

[Stash 用户文档易用且强劲的网络工具](/)

* [Stash 简介](/)
* [快速上手](/get-started)
* 更新日志

  + [iOS](/release-notes/ios)
* 分流规则

  + [规则类型](/rules/rule-types)
  + [规则集合](/rules/rule-set)
* 代理协议

  + [协议类型](/proxy-protocols/proxy-types)
  + [策略组](/proxy-protocols/proxy-groups)
  + [远程代理集](/proxy-protocols/proxy-providers)
  + [延迟测试](/proxy-protocols/proxy-benchmark)
* 配置文件

  + [配置样例](/configuration/example-config)
  + [覆写配置（Override）](/configuration/override)
  + [策略组图标](/configuration/proxy-group-icon)
* HTTP 引擎

  + [简介](/http-engine/intro)
  + [MitM](/http-engine/mitm)
  + [强制 HTTP 引擎](/http-engine/force-http-engine)
  + [HTTP 重写](/http-engine/rewrite)
* JavsScript 脚本

  + [语法与接口](/script/syntax-and-interface)
  + [改写 HTTP](/script/rewrite-requests)
  + [面板（Tile）](/script/tile)
  + [定时任务](/script/scheduled-tasks)
* 功能介绍

  + [内置 DNS 服务](/features/dns-server)
  + [为局域网设备提供代理](/features/provide-proxy-to-lan-device)
  + [服务提供商订阅](/features/service-provider-subscription)
  + [网络性能增强](/features/network-performance-enhance)
  + [按需启动](/features/on-demand)
* [Stash Mac](/stash-mac)
* 常见问题

  + [编写高效配置](/faq/effective-stash)
  + [防止代理被检测](/faq/proxy-detected)
  + [授权与激活](/faq/license-activation)
  + [TestFlight 相关](/faq/testflight)
  + [IPv6 兼容性](/faq/ipv6-compatible)
  + [URL Schema](/faq/url-schema)
  + [越狱修改内存限制](/faq/jailbreak-ios-memory-limit)
  + [无法安装帮助程序 (Helper)](/faq/stash-mac-helper)
  + [Stash 与其他 VPN 冲突](/faq/conflict-with-vpn)

配置文件

策略组图标

# 策略组图标

为了区分不同的策略组，您可以为每个策略组指定一个图标。在配置文件的 `proxy-groups` 章节中，为策略组添加 `icon` 字段，并输入图片的 URL，支持 JPG 和 PNG 格式的图片。

```
- name: 'auto'
  type: url-test
  icon: https://raw.githubusercontent.com/Koolson/Qure/master/IconSet/Color/Direct.png
  proxies:
    - ss1
    - ss2
    - vmess
  interval: 300
```

Last updated on 2024年8月4日

[覆写配置（Override）](/configuration/override "覆写配置（Override）")[简介](/http-engine/intro "简介")

---

# Stash HTTP Engine

[Stash 用户文档易用且强劲的网络工具](/)

* [Stash 简介](/)
* [快速上手](/get-started)
* 更新日志

  + [iOS](/release-notes/ios)
* 分流规则

  + [规则类型](/rules/rule-types)
  + [规则集合](/rules/rule-set)
* 代理协议

  + [协议类型](/proxy-protocols/proxy-types)
  + [策略组](/proxy-protocols/proxy-groups)
  + [远程代理集](/proxy-protocols/proxy-providers)
  + [延迟测试](/proxy-protocols/proxy-benchmark)
* 配置文件

  + [配置样例](/configuration/example-config)
  + [覆写配置（Override）](/configuration/override)
  + [策略组图标](/configuration/proxy-group-icon)
* HTTP 引擎

  + [简介](/http-engine/intro)
  + [MitM](/http-engine/mitm)
  + [强制 HTTP 引擎](/http-engine/force-http-engine)
  + [HTTP 重写](/http-engine/rewrite)
* JavsScript 脚本

  + [语法与接口](/script/syntax-and-interface)
  + [改写 HTTP](/script/rewrite-requests)
  + [面板（Tile）](/script/tile)
  + [定时任务](/script/scheduled-tasks)
* 功能介绍

  + [内置 DNS 服务](/features/dns-server)
  + [为局域网设备提供代理](/features/provide-proxy-to-lan-device)
  + [服务提供商订阅](/features/service-provider-subscription)
  + [网络性能增强](/features/network-performance-enhance)
  + [按需启动](/features/on-demand)
* [Stash Mac](/stash-mac)
* 常见问题

  + [编写高效配置](/faq/effective-stash)
  + [防止代理被检测](/faq/proxy-detected)
  + [授权与激活](/faq/license-activation)
  + [TestFlight 相关](/faq/testflight)
  + [IPv6 兼容性](/faq/ipv6-compatible)
  + [URL Schema](/faq/url-schema)
  + [越狱修改内存限制](/faq/jailbreak-ios-memory-limit)
  + [无法安装帮助程序 (Helper)](/faq/stash-mac-helper)
  + [Stash 与其他 VPN 冲突](/faq/conflict-with-vpn)

On This Page

* [入站逻辑](#入站逻辑)
* [协商与连接管理](#协商与连接管理)
* [实践与表现](#实践与表现)

HTTP 引擎

简介

# Stash HTTP Engine

Stash 内置高效的 HTTP 引擎，允许用户对系统中的 HTTP 请求进行改写、拦截、抓取、重放，以及对 HTTPS 请求通过 MitM 方式进行解密。

## 入站逻辑

系统中并非所有连接都是 HTTP 请求，Stash 会按照以下策略控制连接是否进入 HTTP 引擎。

* 在「仅使用 Tunnel 代理」关闭的情况下，Stash 会向系统声明 HTTP Proxy。进入 HTTP Proxy 的 HTTP 请求会流入 HTTP 引擎处理。
* 对于从 Tunnel 进入，且命中 `force-http-engine` 列表的 TCP 连接，也会流入 HTTP 引擎处理。
* 对于命中 MitM 列表的 HTTPS 请求，也会流入 HTTP 引擎处理，并且 Stash 会根据 SNI 使用配置的根证书生成临时证书，完成 TLS 握手。
* 其他未命中请求会以 TCP 流转发，不进入 HTTP 引擎。
* 暂时不支持处理 HTTP/3 的请求，Stash 会当作普通 UDP 包转发，此时整体吞吐量一般不如基于 TCP 的 HTTP/1 与 HTTP/2 协议。

在遇到 HTTP 改写、脚本不生效时，可以核对上述规则排查。

## 协商与连接管理

Stash HTTP Engine 完整支持解析 HTTP/1.x 与 HTTP/2 协议。

* 对于 HTTP 请求，Stash HTTP Engine 仅支持 HTTP/1.x 协议，不支持 HTTP/2 Cleartext。
* 对于 HTTPS 请求且开启了 MitM，Stash 会尝试与 App 协商升级到 HTTP/2，也会与 Web Server 协商升级到 HTTP/2，L、R 两侧连接是**各自独立无影响**的。
* Stash HTTP Engine 对于 L、R 两侧连接实行**分别管理**，对于 R 侧连接，Stash 会最大限度地复用 TCP 连接，以减少 TCP / TLS 握手的消耗。

## 实践与表现

在实践中，存在：

* 部分 App 不进行 HTTP/2 协商，但 Web Server 支持 HTTP/2 的情况。在 Stash HTTP Engine 通过 MitM 接管后， L 侧会使用 HTTP/1.1 协议，但 R 侧会协商至 HTTP/2。
* 部分 App 即使在 Web Server 支持 HTTP/2 的情况下，仍为每个 HTTPS 请求创建一个 TLS 连接的情况。在 Stash HTTP Engine 通过 MitM 接管后，实际只会创建单条 TCP 连接到 Web Server。

💡

在使用中遇到任何兼容性问题，请与我们联系 。

Last updated on 2023年3月13日

[策略组图标](/configuration/proxy-group-icon "策略组图标")[MitM](/http-engine/mitm "MitM")

---

# MitM

[Stash 用户文档易用且强劲的网络工具](/)

* [Stash 简介](/)
* [快速上手](/get-started)
* 更新日志

  + [iOS](/release-notes/ios)
* 分流规则

  + [规则类型](/rules/rule-types)
  + [规则集合](/rules/rule-set)
* 代理协议

  + [协议类型](/proxy-protocols/proxy-types)
  + [策略组](/proxy-protocols/proxy-groups)
  + [远程代理集](/proxy-protocols/proxy-providers)
  + [延迟测试](/proxy-protocols/proxy-benchmark)
* 配置文件

  + [配置样例](/configuration/example-config)
  + [覆写配置（Override）](/configuration/override)
  + [策略组图标](/configuration/proxy-group-icon)
* HTTP 引擎

  + [简介](/http-engine/intro)
  + [MitM](/http-engine/mitm)
  + [强制 HTTP 引擎](/http-engine/force-http-engine)
  + [HTTP 重写](/http-engine/rewrite)
* JavsScript 脚本

  + [语法与接口](/script/syntax-and-interface)
  + [改写 HTTP](/script/rewrite-requests)
  + [面板（Tile）](/script/tile)
  + [定时任务](/script/scheduled-tasks)
* 功能介绍

  + [内置 DNS 服务](/features/dns-server)
  + [为局域网设备提供代理](/features/provide-proxy-to-lan-device)
  + [服务提供商订阅](/features/service-provider-subscription)
  + [网络性能增强](/features/network-performance-enhance)
  + [按需启动](/features/on-demand)
* [Stash Mac](/stash-mac)
* 常见问题

  + [编写高效配置](/faq/effective-stash)
  + [防止代理被检测](/faq/proxy-detected)
  + [授权与激活](/faq/license-activation)
  + [TestFlight 相关](/faq/testflight)
  + [IPv6 兼容性](/faq/ipv6-compatible)
  + [URL Schema](/faq/url-schema)
  + [越狱修改内存限制](/faq/jailbreak-ios-memory-limit)
  + [无法安装帮助程序 (Helper)](/faq/stash-mac-helper)
  + [Stash 与其他 VPN 冲突](/faq/conflict-with-vpn)

On This Page

* [使用配置文件配置 MitM](#使用配置文件配置-mitm)
* [配置 CA 证书](#配置-ca-证书)
* [配置 MitM 列表](#配置-mitm-列表)
* [使用图形界面配置 MitM](#使用图形界面配置-mitm)
* [配置 CA 证书](#配置-ca-证书-1)
* [配置 MitM 列表](#配置-mitm-列表-1)
* [系统信任证书](#系统信任证书)

HTTP 引擎

MitM

# MitM

如果想对 HTTPS 请求进行查看、改写、执行脚本，必须启用 MitM 功能。在启用 MitM 功能前，你的设备需要信任自行签发的 CA 证书，该 CA 证书可以由用户导入 Stash，或由 Stash 生成。

⚠️

基于数据安全以及私隐的考虑，任何时候你不应该与他人共享证书，或使用互联网上提供的
CA 证书。

## 使用配置文件配置 MitM

### 配置 CA 证书

```
http:
  # 以 PKCS #12 编码的 CA 证书
  ca: ''
  # 证书密码
  ca-passphrase: ''
  # 开启 MitM 功能的域名列表，需要确保上述 CA 证书已受系统信任
```

### 配置 MitM 列表

```
http:
  # 开启 MitM 功能的域名列表，需要确保上述 CA 证书已受系统信任
  mitm:
    - g.cn
    - '*.google.cn'
    - weather-data.apple.com # 默认只对 443 端口开启
    - weather-data.apple.com:* # 使用通配符对所有端口开启
    - '*.weather-data.apple.com' # 域名中也可以使用通配符
```

至此，MitM 配置完毕。

## 使用图形界面配置 MitM

如果无法在配置文件中添加 CA 证书，可以使用 Stash 的图形界面生成 CA 证书。

### 配置 CA 证书

1、在 Stash 首页，找到 **MitM** ，选择 **[CA 证书]**；

2、点击 **[Stash Generated CA]** 生成新的证书；

3、点击 **[安装 证书]** 安装新证书；

4、 Stash 会自动跳转到 **Safari** 进行证书安装，点击 **[允许]** 安装新的证书；

5、出现 [已下载描述文件] ，则代表证书已成功安装；

### 配置 MitM 列表

1、在 Stash 首页，找到 **MitM** ，选择 **[主机名]**；

2、输入您想添加的域名，如 **\*.google.cn** ，域名中可以使用通配符，点击旁边的 **[+ 号]，添加到 MitM 列表里；**

### 系统信任证书

Last updated on 2023年10月29日

[简介](/http-engine/intro "简介")[强制 HTTP 引擎](/http-engine/force-http-engine "强制 HTTP 引擎")

---

# Force HTTP Engine

[Stash 用户文档易用且强劲的网络工具](/)

* [Stash 简介](/)
* [快速上手](/get-started)
* 更新日志

  + [iOS](/release-notes/ios)
* 分流规则

  + [规则类型](/rules/rule-types)
  + [规则集合](/rules/rule-set)
* 代理协议

  + [协议类型](/proxy-protocols/proxy-types)
  + [策略组](/proxy-protocols/proxy-groups)
  + [远程代理集](/proxy-protocols/proxy-providers)
  + [延迟测试](/proxy-protocols/proxy-benchmark)
* 配置文件

  + [配置样例](/configuration/example-config)
  + [覆写配置（Override）](/configuration/override)
  + [策略组图标](/configuration/proxy-group-icon)
* HTTP 引擎

  + [简介](/http-engine/intro)
  + [MitM](/http-engine/mitm)
  + [强制 HTTP 引擎](/http-engine/force-http-engine)
  + [HTTP 重写](/http-engine/rewrite)
* JavsScript 脚本

  + [语法与接口](/script/syntax-and-interface)
  + [改写 HTTP](/script/rewrite-requests)
  + [面板（Tile）](/script/tile)
  + [定时任务](/script/scheduled-tasks)
* 功能介绍

  + [内置 DNS 服务](/features/dns-server)
  + [为局域网设备提供代理](/features/provide-proxy-to-lan-device)
  + [服务提供商订阅](/features/service-provider-subscription)
  + [网络性能增强](/features/network-performance-enhance)
  + [按需启动](/features/on-demand)
* [Stash Mac](/stash-mac)
* 常见问题

  + [编写高效配置](/faq/effective-stash)
  + [防止代理被检测](/faq/proxy-detected)
  + [授权与激活](/faq/license-activation)
  + [TestFlight 相关](/faq/testflight)
  + [IPv6 兼容性](/faq/ipv6-compatible)
  + [URL Schema](/faq/url-schema)
  + [越狱修改内存限制](/faq/jailbreak-ios-memory-limit)
  + [无法安装帮助程序 (Helper)](/faq/stash-mac-helper)
  + [Stash 与其他 VPN 冲突](/faq/conflict-with-vpn)

HTTP 引擎

强制 HTTP 引擎

# Force HTTP Engine

默认地，所有经由 HTTP Proxy 的请求会由 HTTP 引擎处理，以使用改写、脚本等功能。若希望来自 Tunnel 的 TCP 连接经由 HTTP 引擎处理，需要配置 `force-http-engine`。

```
http:
  # 强制使用 Stash 引擎以 HTTP 协议处理 TCP 连接
  # 捕获后的连接可以使用高级功能，例如重写和脚本
  force-http-engine:
    - '*:80'
    - '*:4480' # BiliBili CDN
    - '*:9102' # BiliBili CDN
```

⚠️

无法解析的请求会被 HTTP 引擎以 Bad Request 响应拒绝。

Last updated on 2023年3月13日

[MitM](/http-engine/mitm "MitM")[HTTP 重写](/http-engine/rewrite "HTTP 重写")

---

# HTTP 重写

[Stash 用户文档易用且强劲的网络工具](/)

* [Stash 简介](/)
* [快速上手](/get-started)
* 更新日志

  + [iOS](/release-notes/ios)
* 分流规则

  + [规则类型](/rules/rule-types)
  + [规则集合](/rules/rule-set)
* 代理协议

  + [协议类型](/proxy-protocols/proxy-types)
  + [策略组](/proxy-protocols/proxy-groups)
  + [远程代理集](/proxy-protocols/proxy-providers)
  + [延迟测试](/proxy-protocols/proxy-benchmark)
* 配置文件

  + [配置样例](/configuration/example-config)
  + [覆写配置（Override）](/configuration/override)
  + [策略组图标](/configuration/proxy-group-icon)
* HTTP 引擎

  + [简介](/http-engine/intro)
  + [MitM](/http-engine/mitm)
  + [强制 HTTP 引擎](/http-engine/force-http-engine)
  + [HTTP 重写](/http-engine/rewrite)
* JavsScript 脚本

  + [语法与接口](/script/syntax-and-interface)
  + [改写 HTTP](/script/rewrite-requests)
  + [面板（Tile）](/script/tile)
  + [定时任务](/script/scheduled-tasks)
* 功能介绍

  + [内置 DNS 服务](/features/dns-server)
  + [为局域网设备提供代理](/features/provide-proxy-to-lan-device)
  + [服务提供商订阅](/features/service-provider-subscription)
  + [网络性能增强](/features/network-performance-enhance)
  + [按需启动](/features/on-demand)
* [Stash Mac](/stash-mac)
* 常见问题

  + [编写高效配置](/faq/effective-stash)
  + [防止代理被检测](/faq/proxy-detected)
  + [授权与激活](/faq/license-activation)
  + [TestFlight 相关](/faq/testflight)
  + [IPv6 兼容性](/faq/ipv6-compatible)
  + [URL Schema](/faq/url-schema)
  + [越狱修改内存限制](/faq/jailbreak-ios-memory-limit)
  + [无法安装帮助程序 (Helper)](/faq/stash-mac-helper)
  + [Stash 与其他 VPN 冲突](/faq/conflict-with-vpn)

On This Page

* [URL 重写](#url-重写)
* [transparent](#transparent)
* [302 / 307](#302--307)
* [reject](#reject)
* [reject-200](#reject-200)
* [reject-img](#reject-img)
* [reject-dict](#reject-dict)
* [reject-array](#reject-array)
* [HTTP header 重写](#http-header-重写)
* [request-add / response-add](#request-add--response-add)
* [request-del / response-del](#request-del--response-del)
* [request-replace / response-replace](#request-replace--response-replace)
* [request-replace-regex / response-replace-regex](#request-replace-regex--response-replace-regex)
* [使用 JavaScript 引擎重写](#使用-javascript-引擎重写)

HTTP 引擎

HTTP 重写

# HTTP 重写

HTTP 重写允许用户通过正则表达式匹配 URL，拒绝或者重定向 HTTP(S) 请求，常用于去广告，避免隐私跟踪等目的。

配置格式：

```
http:
  # HTTP(S) 重写，支持header、302、307、reject多种策略
  url-rewrite:
    - ^http://g\.cn https://www.google.com transparent
    - ^https?://www\.google\.cn https://www.google.com 302 # 直接返回一个 302 重定向的响应
    - ^https?://ad\.example - reject # 拒绝请求
  header-rewrite:
    - ^http://g\.cn request-add DNT 1
    - ^http://g\.cn request-del DNT
    - ^http://g\.cn request-replace DNT 1
    - ^http://g\.cn request-replace-regex User-Agent Go-http-client curl

    - ^http://g\.cn response-add DNT 1
    - ^http://g\.cn response-del DNT
    - ^http://g\.cn response-replace DNT 1
    - ^http://g\.cn response-replace-regex User-Agent Go-http-client curl
```

## URL 重写

### `transparent`

拦截并修改请求的 URL，效果类似透明代理，应用对此无感知，支持重定向 HTTP / HTTPS。

### `302 / 307`

HTTP 引擎会返回一个 3xx 状态码，并且会自动设置 Location 字段，以达到重定向的目的。

### `reject`

返回 404 响应，和空的响应 body。

### `reject-200`

返回 200 响应，和空的响应 body。

### `reject-img`

返回 200 响应，和 1px gif 的响应 body。

### `reject-dict`

返回 200 响应，和内容为 `{}` 的响应 body。

### `reject-array`

返回 200 响应，和内容为 `[]` 的响应 body。

## HTTP header 重写

header 重写允许用户增加、删除、替换 HTTP 请求 / 响应的任意 header。

### `request-add` / `response-add`

对 HTTP 请求 / 响应新增 header。

### `request-del` / `response-del`

对 HTTP 请求 / 响应删除 header。

### `request-replace` / `response-replace`

对 HTTP 请求 / 响应替换 header 的值。

### `request-replace-regex` / `response-replace-regex`

对 HTTP 请求 / 响应通过正则表达式替换 header 的值。

## 使用 JavaScript 引擎重写

如果上述功能无法满足需求，请参考[使用 JavaScript 引擎重写 HTTP](/script/rewrite-requests)。

Last updated on 2023年3月16日

[强制 HTTP 引擎](/http-engine/force-http-engine "强制 HTTP 引擎")[语法与接口](/script/syntax-and-interface "语法与接口")

---

# 语法与接口

[Stash 用户文档易用且强劲的网络工具](/)

* [Stash 简介](/)
* [快速上手](/get-started)
* 更新日志

  + [iOS](/release-notes/ios)
* 分流规则

  + [规则类型](/rules/rule-types)
  + [规则集合](/rules/rule-set)
* 代理协议

  + [协议类型](/proxy-protocols/proxy-types)
  + [策略组](/proxy-protocols/proxy-groups)
  + [远程代理集](/proxy-protocols/proxy-providers)
  + [延迟测试](/proxy-protocols/proxy-benchmark)
* 配置文件

  + [配置样例](/configuration/example-config)
  + [覆写配置（Override）](/configuration/override)
  + [策略组图标](/configuration/proxy-group-icon)
* HTTP 引擎

  + [简介](/http-engine/intro)
  + [MitM](/http-engine/mitm)
  + [强制 HTTP 引擎](/http-engine/force-http-engine)
  + [HTTP 重写](/http-engine/rewrite)
* JavsScript 脚本

  + [语法与接口](/script/syntax-and-interface)
  + [改写 HTTP](/script/rewrite-requests)
  + [面板（Tile）](/script/tile)
  + [定时任务](/script/scheduled-tasks)
* 功能介绍

  + [内置 DNS 服务](/features/dns-server)
  + [为局域网设备提供代理](/features/provide-proxy-to-lan-device)
  + [服务提供商订阅](/features/service-provider-subscription)
  + [网络性能增强](/features/network-performance-enhance)
  + [按需启动](/features/on-demand)
* [Stash Mac](/stash-mac)
* 常见问题

  + [编写高效配置](/faq/effective-stash)
  + [防止代理被检测](/faq/proxy-detected)
  + [授权与激活](/faq/license-activation)
  + [TestFlight 相关](/faq/testflight)
  + [IPv6 兼容性](/faq/ipv6-compatible)
  + [URL Schema](/faq/url-schema)
  + [越狱修改内存限制](/faq/jailbreak-ios-memory-limit)
  + [无法安装帮助程序 (Helper)](/faq/stash-mac-helper)
  + [Stash 与其他 VPN 冲突](/faq/conflict-with-vpn)

On This Page

* [基础方法](#基础方法)
* [$done(value)](#donevalue)
* [持久化存储](#持久化存储)
* [HTTP Client](#http-client)

JavsScript 脚本

语法与接口

# 语法与接口

## 基础方法

* `$script.name`：脚本名称
* `$script.type`：脚本类型，如 `request`, `response` 和 `tile`
* `$script.startTime`：脚本开始运行的时间
* `$environment["stash-build"]`：Stash Build 编号
* `$environment["stash-version"]`：Stash 版本号
* `$environment.language`：Stash 运行语言
* `$environment.system`：Stash 运行系统 (iOS / macOS)
* `$argument`：运行参数
* `$done(value)`：结束脚本运行，释放资源
* `$notification.post(title, subtitle, body)`：发送 iOS 通知
* `console.log(value)`：输出日志，脚本日志会输出到单独的文件
* `setTimeout(callback, delay)`：延迟执行回调函数

## `$done(value)`

⚠️

对于所有脚本，在结束时候必须调用 `$done(value)` 方法释放资源。

## 持久化存储

* `$persistentStore.write(value, key)`：写入持久化存储
* `$persistentStore.read(key)`：读取持久化存储

## HTTP Client

* `$httpClient.get(url<String>, callback<Function>)`
* `$httpClient.get(request<Object>, callback<Function>)`

同样地，还有：

* `$httpClient.post()`
* `$httpClient.put()`
* `$httpClient.delete()`
* `$httpClient.head()`
* `$httpClient.options()`
* `$httpClient.patch()`

请求的超时为 5 秒，可以通过设置 `X-Stash-Selected-Proxy` 指定请求的使用的代理，或设置 `binary-mode` 开启二进制模式，例如：

```
$httpClient.get('http://httpbin.org/get', (error, response, data) => {
  if (error) {
    console.log(error)
  } else {
    console.log(data)
  }
})

const yourProxyName = 'a fancy name with 😄'

$httpClient.post(
  {
    url: 'http://httpbin.org/post',
    headers: {
      'X-Header-Key': 'headerValue',
      'X-Stash-Selected-Proxy': encodeURIComponent(yourProxyName),
    },
    body: '{}', // can be object or string
    timeout: 5,
    insecure: false,
    'binary-mode': true,
    'auto-cookie': true,
    'auto-redirect': true,
  },
  (error, response, data) => {
    if (error) {
      console.log(error)
    } else {
      console.log(data)
    }
  }
)
```

Last updated on 2024年5月30日

[HTTP 重写](/http-engine/rewrite "HTTP 重写")[改写 HTTP](/script/rewrite-requests "改写 HTTP")

---

# 改写 HTTP

[Stash 用户文档易用且强劲的网络工具](/)

* [Stash 简介](/)
* [快速上手](/get-started)
* 更新日志

  + [iOS](/release-notes/ios)
* 分流规则

  + [规则类型](/rules/rule-types)
  + [规则集合](/rules/rule-set)
* 代理协议

  + [协议类型](/proxy-protocols/proxy-types)
  + [策略组](/proxy-protocols/proxy-groups)
  + [远程代理集](/proxy-protocols/proxy-providers)
  + [延迟测试](/proxy-protocols/proxy-benchmark)
* 配置文件

  + [配置样例](/configuration/example-config)
  + [覆写配置（Override）](/configuration/override)
  + [策略组图标](/configuration/proxy-group-icon)
* HTTP 引擎

  + [简介](/http-engine/intro)
  + [MitM](/http-engine/mitm)
  + [强制 HTTP 引擎](/http-engine/force-http-engine)
  + [HTTP 重写](/http-engine/rewrite)
* JavsScript 脚本

  + [语法与接口](/script/syntax-and-interface)
  + [改写 HTTP](/script/rewrite-requests)
  + [面板（Tile）](/script/tile)
  + [定时任务](/script/scheduled-tasks)
* 功能介绍

  + [内置 DNS 服务](/features/dns-server)
  + [为局域网设备提供代理](/features/provide-proxy-to-lan-device)
  + [服务提供商订阅](/features/service-provider-subscription)
  + [网络性能增强](/features/network-performance-enhance)
  + [按需启动](/features/on-demand)
* [Stash Mac](/stash-mac)
* 常见问题

  + [编写高效配置](/faq/effective-stash)
  + [防止代理被检测](/faq/proxy-detected)
  + [授权与激活](/faq/license-activation)
  + [TestFlight 相关](/faq/testflight)
  + [IPv6 兼容性](/faq/ipv6-compatible)
  + [URL Schema](/faq/url-schema)
  + [越狱修改内存限制](/faq/jailbreak-ios-memory-limit)
  + [无法安装帮助程序 (Helper)](/faq/stash-mac-helper)
  + [Stash 与其他 VPN 冲突](/faq/conflict-with-vpn)

On This Page

* [配置格式](#配置格式)
* [Request Object](#request-object)
* [Response Object](#response-object)
* [$done(value)](#donevalue)

JavsScript 脚本

改写 HTTP

# 改写 HTTP

用户可以通过 JavaScript 脚本修改流经 Stash 的 HTTP 请求、响应。

## 配置格式

```
http:
  script:
    - match: url-you-want-to-match
      name: your-fancy-script
      type: response # request / response
      require-body: true
      timeout: 20
      argument: ''
      binary-mode: false
      max-size: 1048576 # 1MB

script-providers:
  your-fancy-script:
    url: https://your-fancy-script.com/your-fancy-script.js
    interval: 86400
```

参数：

* `match`: 脚本匹配的 URL 正则表达式。
* `type`: 脚本类型，可选值为 `request` 或 `response`。
* `require-body`: 是否需要请求体 / 响应体，在脚本中处理 body 需要消耗更多的内存空间，仅在必要时启用。
* `timeout`: 脚本执行超时时间，单位为秒。
* `argument`: 脚本执行时的参数，类型为 `string`。
* `binary-mode`：二进制模式，`body` 会以 `Uint8Array` 而不是 `string` 传递给脚本。
* `max-size`：单位为字节，body 超过这个大小的请求不会触发脚本。

💡

二进制模式仅在 Stash iOS 2.0.2 以及之后的版本支持。

## Request Object

* `$request.url`：请求 URL
* `$request.method`：请求方法
* `$request.headers`：请求头
* `$request.body`：请求体，仅在 `require-body: true` 时有，根据是否开启二进制模式，可以为 `string` 或者 `Uint8Array`

## Response Object

* `$request.url`：请求 URL
* `$request.method`：请求方法
* `$request.headers`：请求头
* `$response.status`：响应状态码
* `$response.headers`：响应头
* `$response.body`：响应体，仅在 `require-body: true` 时有，根据是否开启二进制模式，可以为 `string` 或者 `Uint8Array`

## `$done(value)`

⚠️

对于所有脚本，在结束时候必须调用 `$done(value)` 方法释放资源。

对于 request 类型的脚本，调用 `$done(object)` 可以改写 HTTP 请求，`object` 可以包含下述字段：

* `url`：修改请求的 URL
* `headers`：修改请求的 headers
* `body`：修改请求的 body
* `response`：替换 HTTP 响应，不再实际发出 HTTP 请求

你可以调用 `$done()` 来打断请求，或者 `$done({})` 不修改请求的任何内容。

对于 response 类型的脚本，调用 `$done(object)` 可以改写 HTTP 响应，`object` 可以包含下述字段：

* `status`：修改响应的状态码
* `headers`：修改响应的 headers
* `body`：修改响应的 body

你可以调用 `$done()` 来打断请求，或者 `$done({})` 不修改响应的任何内容。

Last updated on 2024年4月6日

[语法与接口](/script/syntax-and-interface "语法与接口")[面板（Tile）](/script/tile "面板（Tile）")

---

# 面板 (Tile)

[Stash 用户文档易用且强劲的网络工具](/)

* [Stash 简介](/)
* [快速上手](/get-started)
* 更新日志

  + [iOS](/release-notes/ios)
* 分流规则

  + [规则类型](/rules/rule-types)
  + [规则集合](/rules/rule-set)
* 代理协议

  + [协议类型](/proxy-protocols/proxy-types)
  + [策略组](/proxy-protocols/proxy-groups)
  + [远程代理集](/proxy-protocols/proxy-providers)
  + [延迟测试](/proxy-protocols/proxy-benchmark)
* 配置文件

  + [配置样例](/configuration/example-config)
  + [覆写配置（Override）](/configuration/override)
  + [策略组图标](/configuration/proxy-group-icon)
* HTTP 引擎

  + [简介](/http-engine/intro)
  + [MitM](/http-engine/mitm)
  + [强制 HTTP 引擎](/http-engine/force-http-engine)
  + [HTTP 重写](/http-engine/rewrite)
* JavsScript 脚本

  + [语法与接口](/script/syntax-and-interface)
  + [改写 HTTP](/script/rewrite-requests)
  + [面板（Tile）](/script/tile)
  + [定时任务](/script/scheduled-tasks)
* 功能介绍

  + [内置 DNS 服务](/features/dns-server)
  + [为局域网设备提供代理](/features/provide-proxy-to-lan-device)
  + [服务提供商订阅](/features/service-provider-subscription)
  + [网络性能增强](/features/network-performance-enhance)
  + [按需启动](/features/on-demand)
* [Stash Mac](/stash-mac)
* 常见问题

  + [编写高效配置](/faq/effective-stash)
  + [防止代理被检测](/faq/proxy-detected)
  + [授权与激活](/faq/license-activation)
  + [TestFlight 相关](/faq/testflight)
  + [IPv6 兼容性](/faq/ipv6-compatible)
  + [URL Schema](/faq/url-schema)
  + [越狱修改内存限制](/faq/jailbreak-ios-memory-limit)
  + [无法安装帮助程序 (Helper)](/faq/stash-mac-helper)
  + [Stash 与其他 VPN 冲突](/faq/conflict-with-vpn)

On This Page

* [配置格式](#配置格式)
* [语法与接口](#语法与接口)
* [$done(value)](#donevalue)

JavsScript 脚本

面板（Tile）

# 面板 (Tile)

用户可以通过 JavaScript 脚本控制 Stash 首页的 Tile 面板。

## 配置格式

```
tiles:
  - name: your-fancy-script
    interval: 600
    title: 'Awesome Tile'
    content: 'This is Super Cool'
    icon: 'theatermasks.circle.fill' # 或 https://stash.ws/amazing.png
    backgroundColor: '#663399'

script-providers:
  your-fancy-script:
    url: https://your-fancy-script.com/your-fancy-script.js
    interval: 86400
```

参数：

* `argument`: 可选，脚本执行时的参数，类型为 `string`。
* `title`: 可选，脚本第一次运行前的标题默认值。
* `content`: 可选，脚本第一次运行前的内容默认值。
* `icon`: 可选，脚本第一次运行前的图标默认值。图标支持 `SF Symbols` 或以 `http` 开头的远程图片。
* `backgroundColor`: 可选，脚本第一次运行前的背景颜色默认值。
* `url`: 可选，脚本第一次运行前的跳转 URL 。

以上部分字段可被 `$done(object)` 覆盖更新。

⚠️

更多关于 `SF Symbols` 详情请参考 [Apple
Developer (opens in a new tab)](https://developer.apple.com/sf-symbols/) 。

## 语法与接口

请参考 [JavaScript 脚本语法与接口](/http-engine/script#%E8%AF%AD%E6%B3%95%E4%B8%8E%E6%8E%A5%E5%8F%A3) 。

例子

```
$httpClient.get('https://api.my-ip.io/ip', function (error, response, data) {
  $done({
    title: '当前 IP 地址',
    content: data,
    backgroundColor: '#663399',
    icon: 'network',
  })
})
```

### `$done(value)`

⚠️

对于所有脚本，在结束时候必须调用 `$done(value)` 方法释放资源。

对于 Tile 类型的脚本，调用 `$done(object)` 可以更新 Tile 面板内容，`object` 可以包含下述字段：

* `title`: 可选，新的 Tile 标题。
* `content`: 可选，新的 Tile 内容。
* `icon`: 可选，新的 Tile 图标。
* `backgroundColor`: 可选，新的 Tile 背景颜色。
* `url`: 可选，新的跳转 URL 。

以上字段如为空则不更新。你可以直接调用 `$done({})` 不修改任何内容。

Last updated on 2023年3月16日

[改写 HTTP](/script/rewrite-requests "改写 HTTP")[定时任务](/script/scheduled-tasks "定时任务")

---

# 定时任务

[Stash 用户文档易用且强劲的网络工具](/)

* [Stash 简介](/)
* [快速上手](/get-started)
* 更新日志

  + [iOS](/release-notes/ios)
* 分流规则

  + [规则类型](/rules/rule-types)
  + [规则集合](/rules/rule-set)
* 代理协议

  + [协议类型](/proxy-protocols/proxy-types)
  + [策略组](/proxy-protocols/proxy-groups)
  + [远程代理集](/proxy-protocols/proxy-providers)
  + [延迟测试](/proxy-protocols/proxy-benchmark)
* 配置文件

  + [配置样例](/configuration/example-config)
  + [覆写配置（Override）](/configuration/override)
  + [策略组图标](/configuration/proxy-group-icon)
* HTTP 引擎

  + [简介](/http-engine/intro)
  + [MitM](/http-engine/mitm)
  + [强制 HTTP 引擎](/http-engine/force-http-engine)
  + [HTTP 重写](/http-engine/rewrite)
* JavsScript 脚本

  + [语法与接口](/script/syntax-and-interface)
  + [改写 HTTP](/script/rewrite-requests)
  + [面板（Tile）](/script/tile)
  + [定时任务](/script/scheduled-tasks)
* 功能介绍

  + [内置 DNS 服务](/features/dns-server)
  + [为局域网设备提供代理](/features/provide-proxy-to-lan-device)
  + [服务提供商订阅](/features/service-provider-subscription)
  + [网络性能增强](/features/network-performance-enhance)
  + [按需启动](/features/on-demand)
* [Stash Mac](/stash-mac)
* 常见问题

  + [编写高效配置](/faq/effective-stash)
  + [防止代理被检测](/faq/proxy-detected)
  + [授权与激活](/faq/license-activation)
  + [TestFlight 相关](/faq/testflight)
  + [IPv6 兼容性](/faq/ipv6-compatible)
  + [URL Schema](/faq/url-schema)
  + [越狱修改内存限制](/faq/jailbreak-ios-memory-limit)
  + [无法安装帮助程序 (Helper)](/faq/stash-mac-helper)
  + [Stash 与其他 VPN 冲突](/faq/conflict-with-vpn)

On This Page

* [Script / 定时脚本](#script--定时脚本)

JavsScript 脚本

定时任务

# 定时任务

Stash 可以在后台执行定时任务，目前仅支持执行 JavaScript 脚本，定时任务需要依赖 Network Extension（VPN） 在已连接状态。

## Script / 定时脚本

Stash 可以在后台定时执行 JavaScript 脚本，以实现自动化的任务，执行的结果可通过系统通知或记录到持久化存储。

JavaScript 脚本的语法和接口请参考 [JavaScript 脚本](/http-engine/script)。

定时脚本通过 cron 表达式指定执行时间、间隔，cron 表达式的语法请参考[这里 (opens in a new tab)](https://crontab.guru/)。

```
cron:
  script:
    - name: your-script-name
      cron: '*/5 * * * *' # at every 5th minute
      argument: '{ "key": true }' # optional
      timeout: 10 # optional

    - name: your-script-name
      cron: '0 20 * * *' # at 20:00
      argument: '{ "key": false }' # optional
      timeout: 15 # optional

script-providers:
  your-script-name:
    url: https://example.com/your-script.js
    interval: 86400
```

💡

你可以在多个场景引用同一个脚本，并通过环境变量判断事件来源（如 HTTP
改写、定时任务）。

Last updated on 2023年3月16日

[面板（Tile）](/script/tile "面板（Tile）")[内置 DNS 服务](/features/dns-server "内置 DNS 服务")

---

# 内置 DNS 服务

[Stash 用户文档易用且强劲的网络工具](/)

* [Stash 简介](/)
* [快速上手](/get-started)
* 更新日志

  + [iOS](/release-notes/ios)
* 分流规则

  + [规则类型](/rules/rule-types)
  + [规则集合](/rules/rule-set)
* 代理协议

  + [协议类型](/proxy-protocols/proxy-types)
  + [策略组](/proxy-protocols/proxy-groups)
  + [远程代理集](/proxy-protocols/proxy-providers)
  + [延迟测试](/proxy-protocols/proxy-benchmark)
* 配置文件

  + [配置样例](/configuration/example-config)
  + [覆写配置（Override）](/configuration/override)
  + [策略组图标](/configuration/proxy-group-icon)
* HTTP 引擎

  + [简介](/http-engine/intro)
  + [MitM](/http-engine/mitm)
  + [强制 HTTP 引擎](/http-engine/force-http-engine)
  + [HTTP 重写](/http-engine/rewrite)
* JavsScript 脚本

  + [语法与接口](/script/syntax-and-interface)
  + [改写 HTTP](/script/rewrite-requests)
  + [面板（Tile）](/script/tile)
  + [定时任务](/script/scheduled-tasks)
* 功能介绍

  + [内置 DNS 服务](/features/dns-server)
  + [为局域网设备提供代理](/features/provide-proxy-to-lan-device)
  + [服务提供商订阅](/features/service-provider-subscription)
  + [网络性能增强](/features/network-performance-enhance)
  + [按需启动](/features/on-demand)
* [Stash Mac](/stash-mac)
* 常见问题

  + [编写高效配置](/faq/effective-stash)
  + [防止代理被检测](/faq/proxy-detected)
  + [授权与激活](/faq/license-activation)
  + [TestFlight 相关](/faq/testflight)
  + [IPv6 兼容性](/faq/ipv6-compatible)
  + [URL Schema](/faq/url-schema)
  + [越狱修改内存限制](/faq/jailbreak-ios-memory-limit)
  + [无法安装帮助程序 (Helper)](/faq/stash-mac-helper)
  + [Stash 与其他 VPN 冲突](/faq/conflict-with-vpn)

On This Page

* [自定义上游 DNS 服务器](#自定义上游-dns-服务器)
* [基于域名的自定义 DNS 服务](#基于域名的自定义-dns-服务)
* [自定义 Hosts](#自定义-hosts)
* [DNS 查询跟随规则](#dns-查询跟随规则)

功能介绍

内置 DNS 服务

# 内置 DNS 服务

## 自定义上游 DNS 服务器

Stash 支持同时配置多个 DNS 服务器。在进行查询时，Stash 会并发请求所有服务器，并采用最快响应的结果。Stash 支持以下 DNS 协议：

* 使用系统提供的 DNS：`system`
* DNS over UDP：`8.8.8.8` 或 `udp://8.8.8.8`
* DNS over TCP：`tcp://8.8.8.8`
* [DNS over TLS (opens in a new tab)](https://www.rfc-editor.org/rfc/rfc7858)：`tls://8.8.8.8:853` 或 `dot://8.8.8.8:853`
* [DNS over HTTPS (opens in a new tab)](https://www.rfc-editor.org/rfc/rfc8484)：`https://1.1.1.1/dns-query` 或 `doh://1.1.1.1/dns-query`
* DNS over HTTP/3：`http3://1.1.1.1/dns-query` 或 `doh3://1.1.1.1/dns-query`
* [DNS over QUIC (opens in a new tab)](https://www.rfc-editor.org/rfc/rfc9250)：`quic://dns.adguard.com:853` 或 `doq://dns.adguard.com:853`

`default-nameserver` 将用于解析 DNS 服务的域名，仅支持填写 DNS 服务器的 IP 地址。

```
dns:
  # 以下填写的 DNS 服务器将用于解析 DNS 服务的域名
  # 仅填写 DNS 服务器的 IP 地址
  default-nameserver:
    - 223.5.5.5
    - 114.114.114.114
  # 支持 UDP / TCP / DoT / DoH / DoQ 协议的 DNS 服务，可以指明具体的连接端口号。
  # 所有 DNS 请求将直接发送到服务器，不经过任何代理。
  # Stash 会使用最先获得的解析记录回复 DNS 请求
  nameserver:
    # 不建议配置超过 2 个 DNS 服务器，会增加系统功耗
    - https://doh.pub/dns-query
    - https://dns.alidns.com/dns-query
    - quic://dns.adguard.com:853
    - doq://test.dns.nextdns.io:853
    - system # 使用 iOS 系统 DNS

  # 跳过证书验证，解决部分兼容性问题 https://help.nextdns.io/t/g9hdkjz
  skip-cert-verify: true

  # DNS 查询跟随代理规则
  follow-rule: false
```

Stash 会对 DNS 查询使用 LRU 算法进行本地缓存。当本地缓存过期时，Stash 会继续沿用缓存结果，并在后台静默更新记录，这会有效降低 DNS 缓存过期引发的请求延迟。

## 基于域名的自定义 DNS 服务

`nameserver-policy` 可以对指定域名使用特定的 DNS 服务器。

```
dns:
  # 对部分域名使用单独的 DNS 服务器
  nameserver-policy:
    'www.baidu.com': 114.114.114.114
    '+.internal.crop.com': system
```

## 自定义 Hosts

```
# 支持通配符域名 (例如: *.clash.dev, *.foo.*.example.com )
# 不使用通配符的域名优先级高于使用通配符的域名 (例如: foo.example.com > *.example.com > .example.com )
# 注意: +.foo.com 的效果等同于 .foo.com 和 foo.com
hosts:
  '*.clash.dev': 127.0.0.1
  '.dev': 127.0.0.1
  'alpha.clash.dev': '::1'
```

## DNS 查询跟随规则

默认情况下，Stash 发出的 DNS 查询均会直接出站，而不经由任何代理规则转发。开启 `follow-rule` 选项后，Stash 会根据代理规则进行 DNS 查询的转发。

⚠️

绝大部分场景下，不需要开启此配置。DNS 查询由代理转发后，可能会破坏云服务商的 CDN 全球优化策略，导致静态资源加载缓慢。DNS 查询请求进入 Stash 网络引擎，也会导致轻微的延迟上升。

请仅在必要时开启此配置。

⚠️

由于连接代理服务器可能需要进行 DNS 解析，DNS 查询由代理转发后，会存在递归查询的问题。开启此配置前请确保满足以下其中一项条件：

* 转发 DNS 请求的代理地址为 IP 地址，而不是域名
* DNS 服务器地址为 IP 地址，而不是域名

Last updated on 2024年8月4日

[定时任务](/script/scheduled-tasks "定时任务")[为局域网设备提供代理](/features/provide-proxy-to-lan-device "为局域网设备提供代理")

---

# 为局域网设备提供代理

[Stash 用户文档易用且强劲的网络工具](/)

* [Stash 简介](/)
* [快速上手](/get-started)
* 更新日志

  + [iOS](/release-notes/ios)
* 分流规则

  + [规则类型](/rules/rule-types)
  + [规则集合](/rules/rule-set)
* 代理协议

  + [协议类型](/proxy-protocols/proxy-types)
  + [策略组](/proxy-protocols/proxy-groups)
  + [远程代理集](/proxy-protocols/proxy-providers)
  + [延迟测试](/proxy-protocols/proxy-benchmark)
* 配置文件

  + [配置样例](/configuration/example-config)
  + [覆写配置（Override）](/configuration/override)
  + [策略组图标](/configuration/proxy-group-icon)
* HTTP 引擎

  + [简介](/http-engine/intro)
  + [MitM](/http-engine/mitm)
  + [强制 HTTP 引擎](/http-engine/force-http-engine)
  + [HTTP 重写](/http-engine/rewrite)
* JavsScript 脚本

  + [语法与接口](/script/syntax-and-interface)
  + [改写 HTTP](/script/rewrite-requests)
  + [面板（Tile）](/script/tile)
  + [定时任务](/script/scheduled-tasks)
* 功能介绍

  + [内置 DNS 服务](/features/dns-server)
  + [为局域网设备提供代理](/features/provide-proxy-to-lan-device)
  + [服务提供商订阅](/features/service-provider-subscription)
  + [网络性能增强](/features/network-performance-enhance)
  + [按需启动](/features/on-demand)
* [Stash Mac](/stash-mac)
* 常见问题

  + [编写高效配置](/faq/effective-stash)
  + [防止代理被检测](/faq/proxy-detected)
  + [授权与激活](/faq/license-activation)
  + [TestFlight 相关](/faq/testflight)
  + [IPv6 兼容性](/faq/ipv6-compatible)
  + [URL Schema](/faq/url-schema)
  + [越狱修改内存限制](/faq/jailbreak-ios-memory-limit)
  + [无法安装帮助程序 (Helper)](/faq/stash-mac-helper)
  + [Stash 与其他 VPN 冲突](/faq/conflict-with-vpn)

On This Page

* [HTTP 代理与 SOCKS 代理](#http-代理与-socks-代理)
* [通过个人热点提供代理](#通过个人热点提供代理)
* [Stash tvOS & Stash Mac 网关模式](#stash-tvos--stash-mac-网关模式)

功能介绍

为局域网设备提供代理

# 为局域网设备提供代理

Stash iOS、Stash tvOS 与 Stash Mac 均支持为局域网设备提供代理服务。

* Stash iOS 支持提供 HTTP 代理和 SOCKS 代理
* Stash tvOS 和 Stash Mac 支持提供 HTTP 代理、SOCKS 代理和透明代理（网关模式）

💡

网关模式可以为局域网内设备提供透明代理，也常称为旁路由或增强模式。

## HTTP 代理与 SOCKS 代理

Stash iOS 与 Stash Mac 均默认在 7890 端口提供 HTTP 代理与 SOCKS 代理服务。开启「允许局域网连接」后，局域网设备可通过 7890 端口访问 Stash 提供的代理服务。

例如局域网内 IP 地址为 `192.168.1.10` 的设备运行着 Stash，可通过以下命令为 shell 配置代理：

```
export https_proxy=http://192.168.1.10:7890
export http_proxy=http://192.168.1.10:7890
export all_proxy=socks5h://192.168.1.10:7890
```

## 通过个人热点提供代理

在 iPhone/iPad 等设备开启个人热点后，运行 Stash 可为连接至个人热点的设备提供 HTTP 代理或 SOCKS 代理服务，此功能同样需要开启「允许局域网连接」。

## Stash tvOS & Stash Mac 网关模式

* Stash tvOS 仅支持在 [支持 Thread 的 Apple TV (opens in a new tab)](https://support.apple.com/en-hk/HT210213) 上启用透明代理
* Stash Mac 启用透明代理需要开启「增强模式」

假设局域网内 IP 地址为 `192.168.1.10` 的设备运行着 Stash，为局域网设备提供代理需进行如下设置：

1. 将局域网内设备的网关配置为 `192.168.1.10`
2. DNS 设置为 `198.18.0.2`
3. 保持 IP 地址和子网掩码不变

启用网关模式的 Stash 可代理 TCP 和 UDP 流量，并会简单响应 ICMP 的 Echo Reply。

💡

若 Apple TV 休眠一段时间后旁路由无响应，请根据 Apple 官方指引排查 Apple TV
是否已设置为家居中枢。

Last updated on 2025年4月6日

[内置 DNS 服务](/features/dns-server "内置 DNS 服务")[服务提供商订阅](/features/service-provider-subscription "服务提供商订阅")

---

# 服务提供商订阅

[Stash 用户文档易用且强劲的网络工具](/)

* [Stash 简介](/)
* [快速上手](/get-started)
* 更新日志

  + [iOS](/release-notes/ios)
* 分流规则

  + [规则类型](/rules/rule-types)
  + [规则集合](/rules/rule-set)
* 代理协议

  + [协议类型](/proxy-protocols/proxy-types)
  + [策略组](/proxy-protocols/proxy-groups)
  + [远程代理集](/proxy-protocols/proxy-providers)
  + [延迟测试](/proxy-protocols/proxy-benchmark)
* 配置文件

  + [配置样例](/configuration/example-config)
  + [覆写配置（Override）](/configuration/override)
  + [策略组图标](/configuration/proxy-group-icon)
* HTTP 引擎

  + [简介](/http-engine/intro)
  + [MitM](/http-engine/mitm)
  + [强制 HTTP 引擎](/http-engine/force-http-engine)
  + [HTTP 重写](/http-engine/rewrite)
* JavsScript 脚本

  + [语法与接口](/script/syntax-and-interface)
  + [改写 HTTP](/script/rewrite-requests)
  + [面板（Tile）](/script/tile)
  + [定时任务](/script/scheduled-tasks)
* 功能介绍

  + [内置 DNS 服务](/features/dns-server)
  + [为局域网设备提供代理](/features/provide-proxy-to-lan-device)
  + [服务提供商订阅](/features/service-provider-subscription)
  + [网络性能增强](/features/network-performance-enhance)
  + [按需启动](/features/on-demand)
* [Stash Mac](/stash-mac)
* 常见问题

  + [编写高效配置](/faq/effective-stash)
  + [防止代理被检测](/faq/proxy-detected)
  + [授权与激活](/faq/license-activation)
  + [TestFlight 相关](/faq/testflight)
  + [IPv6 兼容性](/faq/ipv6-compatible)
  + [URL Schema](/faq/url-schema)
  + [越狱修改内存限制](/faq/jailbreak-ios-memory-limit)
  + [无法安装帮助程序 (Helper)](/faq/stash-mac-helper)
  + [Stash 与其他 VPN 冲突](/faq/conflict-with-vpn)

On This Page

* [定时更新配置](#定时更新配置)
* [展示服务信息](#展示服务信息)

功能介绍

服务提供商订阅

# 服务提供商订阅

Stash 支持由服务提供商管理的配置，可以定时更新配置文件，并显示服务剩余流量、过期信息。

## 定时更新配置

在配置文件的**首行**加入如下注释，Stash 会将配置认定为服务提供商管理的配置，该配置会定时从指定的 URL 获取新版本。目前检查更新的间隔为 12 小时，用户可以在设置页面更改这个配置。

```
#SUBSCRIBED https://proxy.service/stash/config
```

## 展示服务信息

服务提供商可以通过 HTTP Response Header 提供服务信息，包括：上行流量、下行流量、流量总量、过期时间。格式为：

```
Subscription-Userinfo: upload=%f; download=%f; total=%f; expire=%f
```

服务信息会被 Stash 解析，并在 App 首页显示。

Stash 会首先采用定时更新配置 URL 中的服务信息，如果没有定时更新 URL，则会使用配置文件中的 `proxy-providers` 中的 `url`，该字段可以在可视化编辑页面设置。

💡

Stash 会优先使用 HEAD 方法获取服务信息以降低流量消耗。

Last updated on 2023年9月24日

[为局域网设备提供代理](/features/provide-proxy-to-lan-device "为局域网设备提供代理")[网络性能增强](/features/network-performance-enhance "网络性能增强")

---

# 网络性能增强

[Stash 用户文档易用且强劲的网络工具](/)

* [Stash 简介](/)
* [快速上手](/get-started)
* 更新日志

  + [iOS](/release-notes/ios)
* 分流规则

  + [规则类型](/rules/rule-types)
  + [规则集合](/rules/rule-set)
* 代理协议

  + [协议类型](/proxy-protocols/proxy-types)
  + [策略组](/proxy-protocols/proxy-groups)
  + [远程代理集](/proxy-protocols/proxy-providers)
  + [延迟测试](/proxy-protocols/proxy-benchmark)
* 配置文件

  + [配置样例](/configuration/example-config)
  + [覆写配置（Override）](/configuration/override)
  + [策略组图标](/configuration/proxy-group-icon)
* HTTP 引擎

  + [简介](/http-engine/intro)
  + [MitM](/http-engine/mitm)
  + [强制 HTTP 引擎](/http-engine/force-http-engine)
  + [HTTP 重写](/http-engine/rewrite)
* JavsScript 脚本

  + [语法与接口](/script/syntax-and-interface)
  + [改写 HTTP](/script/rewrite-requests)
  + [面板（Tile）](/script/tile)
  + [定时任务](/script/scheduled-tasks)
* 功能介绍

  + [内置 DNS 服务](/features/dns-server)
  + [为局域网设备提供代理](/features/provide-proxy-to-lan-device)
  + [服务提供商订阅](/features/service-provider-subscription)
  + [网络性能增强](/features/network-performance-enhance)
  + [按需启动](/features/on-demand)
* [Stash Mac](/stash-mac)
* 常见问题

  + [编写高效配置](/faq/effective-stash)
  + [防止代理被检测](/faq/proxy-detected)
  + [授权与激活](/faq/license-activation)
  + [TestFlight 相关](/faq/testflight)
  + [IPv6 兼容性](/faq/ipv6-compatible)
  + [URL Schema](/faq/url-schema)
  + [越狱修改内存限制](/faq/jailbreak-ios-memory-limit)
  + [无法安装帮助程序 (Helper)](/faq/stash-mac-helper)
  + [Stash 与其他 VPN 冲突](/faq/conflict-with-vpn)

On This Page

* [并发 DNS 查询](#并发-dns-查询)
* [乐观 DNS 缓存（Optimistic DNS）](#乐观-dns-缓存optimistic-dns)
* [并发连接](#并发连接)
* [混合使用多个网络](#混合使用多个网络)

功能介绍

网络性能增强

# 网络性能增强

Stash 在网络连接的每一层面进行了性能优化，致力于提供低延迟、高吞吐的访问体验。

💡

部分功能需要在「网络设置」中手动启用。

## 并发 DNS 查询

Stash 允许用户配置多个 DNS 服务器。在进行查询时，Stash 会并发请求所有服务器，并采用最快响应的结果。

## 乐观 DNS 缓存（Optimistic DNS）

Stash 使用 LRU 算法对 DNS 查询进行本地缓存。当本地缓存过期时，Stash 会继续使用缓存结果，并在后台静默更新记录，从而有效降低因 DNS 缓存过期引发的请求延迟。

## 并发连接

在域名拥有多个 A / AAAA 记录的情况下，Stash 会并发向所有 IP 发起 TCP 连接，并选择最快握手成功的结果。这在访问 CDN 时，可以避免单节点失效，提供较好的表现。

## 混合使用多个网络

在 Wi-Fi / 蜂窝网络（Cellular）/ 有线网络同时可用的情况下，Stash 会尝试同时使用多个网络建立连接，并选择最快握手成功的结果。此功能可以与「并发连接」同时使用，能在弱网和网络切换的场景下降低连接超时的概率。

Last updated on 2024年8月4日

[服务提供商订阅](/features/service-provider-subscription "服务提供商订阅")[按需启动](/features/on-demand "按需启动")

---

# 按需启动

[Stash 用户文档易用且强劲的网络工具](/)

* [Stash 简介](/)
* [快速上手](/get-started)
* 更新日志

  + [iOS](/release-notes/ios)
* 分流规则

  + [规则类型](/rules/rule-types)
  + [规则集合](/rules/rule-set)
* 代理协议

  + [协议类型](/proxy-protocols/proxy-types)
  + [策略组](/proxy-protocols/proxy-groups)
  + [远程代理集](/proxy-protocols/proxy-providers)
  + [延迟测试](/proxy-protocols/proxy-benchmark)
* 配置文件

  + [配置样例](/configuration/example-config)
  + [覆写配置（Override）](/configuration/override)
  + [策略组图标](/configuration/proxy-group-icon)
* HTTP 引擎

  + [简介](/http-engine/intro)
  + [MitM](/http-engine/mitm)
  + [强制 HTTP 引擎](/http-engine/force-http-engine)
  + [HTTP 重写](/http-engine/rewrite)
* JavsScript 脚本

  + [语法与接口](/script/syntax-and-interface)
  + [改写 HTTP](/script/rewrite-requests)
  + [面板（Tile）](/script/tile)
  + [定时任务](/script/scheduled-tasks)
* 功能介绍

  + [内置 DNS 服务](/features/dns-server)
  + [为局域网设备提供代理](/features/provide-proxy-to-lan-device)
  + [服务提供商订阅](/features/service-provider-subscription)
  + [网络性能增强](/features/network-performance-enhance)
  + [按需启动](/features/on-demand)
* [Stash Mac](/stash-mac)
* 常见问题

  + [编写高效配置](/faq/effective-stash)
  + [防止代理被检测](/faq/proxy-detected)
  + [授权与激活](/faq/license-activation)
  + [TestFlight 相关](/faq/testflight)
  + [IPv6 兼容性](/faq/ipv6-compatible)
  + [URL Schema](/faq/url-schema)
  + [越狱修改内存限制](/faq/jailbreak-ios-memory-limit)
  + [无法安装帮助程序 (Helper)](/faq/stash-mac-helper)
  + [Stash 与其他 VPN 冲突](/faq/conflict-with-vpn)

On This Page

* [保持 Stash 开启](#保持-stash-开启)
* [按需连接](#按需连接)

功能介绍

按需启动

# 按需启动

## 保持 Stash 开启

启用此选项后，Stash 将保持持续运行状态，您只能通过 Stash App 内的停止按钮来关闭 Stash。

✅

即使在系统重新启动后，Stash 也能自动开启。

## 按需连接

如果您希望在特定的网络环境下停用 Stash，可以通过配置按需连接，使 Stash 在不同的情况下自动启动或禁用。

例如，启用按需连接后，关闭蜂窝数据按钮，Stash 将不会在蜂窝数据网络下启用。

您还可以在某些 Wi-Fi 网络下停用 Stash，例如在包含透明代理的路由器网络中，以防止流量被重复代理。

只需将 Wi-Fi 的 SSID 填入排除 SSIDs 列表中，Stash 将不会在该 SSID 的网络下启用。

Last updated on 2024年8月4日

[网络性能增强](/features/network-performance-enhance "网络性能增强")[Stash Mac](/stash-mac "Stash Mac")

---

# Stash Mac

[Stash 用户文档易用且强劲的网络工具](/)

* [Stash 简介](/)
* [快速上手](/get-started)
* 更新日志

  + [iOS](/release-notes/ios)
* 分流规则

  + [规则类型](/rules/rule-types)
  + [规则集合](/rules/rule-set)
* 代理协议

  + [协议类型](/proxy-protocols/proxy-types)
  + [策略组](/proxy-protocols/proxy-groups)
  + [远程代理集](/proxy-protocols/proxy-providers)
  + [延迟测试](/proxy-protocols/proxy-benchmark)
* 配置文件

  + [配置样例](/configuration/example-config)
  + [覆写配置（Override）](/configuration/override)
  + [策略组图标](/configuration/proxy-group-icon)
* HTTP 引擎

  + [简介](/http-engine/intro)
  + [MitM](/http-engine/mitm)
  + [强制 HTTP 引擎](/http-engine/force-http-engine)
  + [HTTP 重写](/http-engine/rewrite)
* JavsScript 脚本

  + [语法与接口](/script/syntax-and-interface)
  + [改写 HTTP](/script/rewrite-requests)
  + [面板（Tile）](/script/tile)
  + [定时任务](/script/scheduled-tasks)
* 功能介绍

  + [内置 DNS 服务](/features/dns-server)
  + [为局域网设备提供代理](/features/provide-proxy-to-lan-device)
  + [服务提供商订阅](/features/service-provider-subscription)
  + [网络性能增强](/features/network-performance-enhance)
  + [按需启动](/features/on-demand)
* [Stash Mac](/stash-mac)
* 常见问题

  + [编写高效配置](/faq/effective-stash)
  + [防止代理被检测](/faq/proxy-detected)
  + [授权与激活](/faq/license-activation)
  + [TestFlight 相关](/faq/testflight)
  + [IPv6 兼容性](/faq/ipv6-compatible)
  + [URL Schema](/faq/url-schema)
  + [越狱修改内存限制](/faq/jailbreak-ios-memory-limit)
  + [无法安装帮助程序 (Helper)](/faq/stash-mac-helper)
  + [Stash 与其他 VPN 冲突](/faq/conflict-with-vpn)

On This Page

* [原生应用](#原生应用)
* [基于进程的规则](#基于进程的规则)
* [网关模式](#网关模式)

Stash Mac

# Stash Mac

Stash Mac 包含 iOS 版本的所有功能。此外，由于专为 macOS 平台设计，Stash Mac 将支持比 iOS 版本更多的功能。

## 原生应用

Stash Mac 专为 macOS 平台设计，原生支持 Intel / Apple Silicon 两种架构的 Mac。此外，支持开机启动、菜单栏快捷操作、键盘快捷键等一系列 macOS 原生交互。

## 基于进程的规则

由于 macOS 的开放设计，Stash Mac 可以为进程指定独立的分流规则。在 Stash Dashboard 中，您可以查看每个本地 TCP / UDP 连接对应的进程信息，甚至可以利用 Stash 构建您个人的网络防火墙。

## 网关模式

在局域网中有多个设备？Stash Mac 支持网关模式，只需将局域网中设备的网关指向运行 Stash 增强模式的 macOS，即可提供无缝的透明代理体验。Stash Mac 已经为作为路由网关做好了充分准备，[点击这里了解更多](/features/provide-proxy-to-lan-device)。

[想要购买？点击这里了解 Stash Mac 的价格 (opens in a new tab)](https://stash.ws/macos/pricing/)

Last updated on 2024年8月4日

[按需启动](/features/on-demand "按需启动")[编写高效配置](/faq/effective-stash "编写高效配置")

---

# 编写高效的配置文件

[Stash 用户文档易用且强劲的网络工具](/)

* [Stash 简介](/)
* [快速上手](/get-started)
* 更新日志

  + [iOS](/release-notes/ios)
* 分流规则

  + [规则类型](/rules/rule-types)
  + [规则集合](/rules/rule-set)
* 代理协议

  + [协议类型](/proxy-protocols/proxy-types)
  + [策略组](/proxy-protocols/proxy-groups)
  + [远程代理集](/proxy-protocols/proxy-providers)
  + [延迟测试](/proxy-protocols/proxy-benchmark)
* 配置文件

  + [配置样例](/configuration/example-config)
  + [覆写配置（Override）](/configuration/override)
  + [策略组图标](/configuration/proxy-group-icon)
* HTTP 引擎

  + [简介](/http-engine/intro)
  + [MitM](/http-engine/mitm)
  + [强制 HTTP 引擎](/http-engine/force-http-engine)
  + [HTTP 重写](/http-engine/rewrite)
* JavsScript 脚本

  + [语法与接口](/script/syntax-and-interface)
  + [改写 HTTP](/script/rewrite-requests)
  + [面板（Tile）](/script/tile)
  + [定时任务](/script/scheduled-tasks)
* 功能介绍

  + [内置 DNS 服务](/features/dns-server)
  + [为局域网设备提供代理](/features/provide-proxy-to-lan-device)
  + [服务提供商订阅](/features/service-provider-subscription)
  + [网络性能增强](/features/network-performance-enhance)
  + [按需启动](/features/on-demand)
* [Stash Mac](/stash-mac)
* 常见问题

  + [编写高效配置](/faq/effective-stash)
  + [防止代理被检测](/faq/proxy-detected)
  + [授权与激活](/faq/license-activation)
  + [TestFlight 相关](/faq/testflight)
  + [IPv6 兼容性](/faq/ipv6-compatible)
  + [URL Schema](/faq/url-schema)
  + [越狱修改内存限制](/faq/jailbreak-ios-memory-limit)
  + [无法安装帮助程序 (Helper)](/faq/stash-mac-helper)
  + [Stash 与其他 VPN 冲突](/faq/conflict-with-vpn)

On This Page

* [配置合理的 DNS 服务器](#配置合理的-dns-服务器)
* [使用规则集合](#使用规则集合)
* [通过代理转发时禁用 QUIC 协议](#通过代理转发时禁用-quic-协议)

常见问题

编写高效配置

# 编写高效的配置文件

由于 iOS Network Extension 在 iOS 14 限制使用 15 MB 内存，在 iOS 15+ 限制使用 50 MB 内存，不合理的配置文件可能会导致 Stash 被 iOS 关闭。以下是一些建议，帮助您编写高效的配置文件。

## 配置合理的 DNS 服务器

Stash 会同时向所有配置的 DNS 服务器发起查询，并通过 LRU 算法缓存 DNS 查询结果。在移动设备上，建议配置 1 到 2 个 DNS 服务器即可满足需求。

* 使用 DoH、DoT、DoQ 协议比传统基于 UDP 的查询更消耗系统资源，且延迟通常更高
* Stash 会使用 Fake IP 来避免需要代理的请求进行本地 DNS 查询。对于中国用户，建议使用国内 DNS 服务器，配置 8.8.8.8 / 1.1.1.1 等国外 DNS 服务不会带来实际收益

## 使用规则集合

对于去广告、按 IP 地理信息分流等需要大量规则的场景，建议使用 `domain` 或 `ipcidr` 类型的[规则集合](/rules/rule-set)，这能有效降低内存占用并提高匹配速度。

⚠️

不建议使用大量 `classical`
类型的规则集合。此类规则只能进行顺序匹配，会显著增加匹配耗时和 Stash
的内存占用。

## 通过代理转发时禁用 QUIC 协议

HTTP3/QUIC 协议基于 UDP，在某些代理协议中 UDP 转发效率较低。您可以通过 [Script Shortcuts](/rules/rule-types#script) 来禁用 QUIC 协议：

```
script:
  shortcuts:
    quic: network == 'udp' and dst_port == 443

rules:
  - GEOIP,CN,DIRECT
  - SCRIPT,quic,REJECT
  - MATCH,PROXY
```

Last updated on 2025年4月6日

[Stash Mac](/stash-mac "Stash Mac") [防止代理被检测](/faq/proxy-detected " 防止代理被检测")

---

# 防止代理被检测

[Stash 用户文档易用且强劲的网络工具](/)

* [Stash 简介](/)
* [快速上手](/get-started)
* 更新日志

  + [iOS](/release-notes/ios)
* 分流规则

  + [规则类型](/rules/rule-types)
  + [规则集合](/rules/rule-set)
* 代理协议

  + [协议类型](/proxy-protocols/proxy-types)
  + [策略组](/proxy-protocols/proxy-groups)
  + [远程代理集](/proxy-protocols/proxy-providers)
  + [延迟测试](/proxy-protocols/proxy-benchmark)
* 配置文件

  + [配置样例](/configuration/example-config)
  + [覆写配置（Override）](/configuration/override)
  + [策略组图标](/configuration/proxy-group-icon)
* HTTP 引擎

  + [简介](/http-engine/intro)
  + [MitM](/http-engine/mitm)
  + [强制 HTTP 引擎](/http-engine/force-http-engine)
  + [HTTP 重写](/http-engine/rewrite)
* JavsScript 脚本

  + [语法与接口](/script/syntax-and-interface)
  + [改写 HTTP](/script/rewrite-requests)
  + [面板（Tile）](/script/tile)
  + [定时任务](/script/scheduled-tasks)
* 功能介绍

  + [内置 DNS 服务](/features/dns-server)
  + [为局域网设备提供代理](/features/provide-proxy-to-lan-device)
  + [服务提供商订阅](/features/service-provider-subscription)
  + [网络性能增强](/features/network-performance-enhance)
  + [按需启动](/features/on-demand)
* [Stash Mac](/stash-mac)
* 常见问题

  + [编写高效配置](/faq/effective-stash)
  + [防止代理被检测](/faq/proxy-detected)
  + [授权与激活](/faq/license-activation)
  + [TestFlight 相关](/faq/testflight)
  + [IPv6 兼容性](/faq/ipv6-compatible)
  + [URL Schema](/faq/url-schema)
  + [越狱修改内存限制](/faq/jailbreak-ios-memory-limit)
  + [无法安装帮助程序 (Helper)](/faq/stash-mac-helper)
  + [Stash 与其他 VPN 冲突](/faq/conflict-with-vpn)

常见问题

防止代理被检测

# 防止代理被检测

部分应用程序可能会检测系统是否使用代理软件，从而禁止用户在代理环境下使用。Stash 提供了「仅使用 Tunnel 代理」模式来防止应用程序检测代理程序，该选项将禁用 Stash Proxy，使得所有 HTTP(S) 请求亦会交由 Stash Tunnel 进行处理，以改善和某些应用的兼容性问题。

1. 在 Stash 的设置页面，选择「网络设置」
2. 打开「仅使用 Tunnel 代理」

💡

开启这个选项会使得 Stash HTTP Engine 失效 ，导致 HTTP
改写功能失效。避免该问题，请参考 [Force HTTP
Engine](/http-engine/force-http-engine)。

Last updated on 2023年10月29日

[编写高效配置](/faq/effective-stash "编写高效配置")[授权与激活](/faq/license-activation "授权与激活")

---

# 授权与激活

[Stash 用户文档易用且强劲的网络工具](/)

* [Stash 简介](/)
* [快速上手](/get-started)
* 更新日志

  + [iOS](/release-notes/ios)
* 分流规则

  + [规则类型](/rules/rule-types)
  + [规则集合](/rules/rule-set)
* 代理协议

  + [协议类型](/proxy-protocols/proxy-types)
  + [策略组](/proxy-protocols/proxy-groups)
  + [远程代理集](/proxy-protocols/proxy-providers)
  + [延迟测试](/proxy-protocols/proxy-benchmark)
* 配置文件

  + [配置样例](/configuration/example-config)
  + [覆写配置（Override）](/configuration/override)
  + [策略组图标](/configuration/proxy-group-icon)
* HTTP 引擎

  + [简介](/http-engine/intro)
  + [MitM](/http-engine/mitm)
  + [强制 HTTP 引擎](/http-engine/force-http-engine)
  + [HTTP 重写](/http-engine/rewrite)
* JavsScript 脚本

  + [语法与接口](/script/syntax-and-interface)
  + [改写 HTTP](/script/rewrite-requests)
  + [面板（Tile）](/script/tile)
  + [定时任务](/script/scheduled-tasks)
* 功能介绍

  + [内置 DNS 服务](/features/dns-server)
  + [为局域网设备提供代理](/features/provide-proxy-to-lan-device)
  + [服务提供商订阅](/features/service-provider-subscription)
  + [网络性能增强](/features/network-performance-enhance)
  + [按需启动](/features/on-demand)
* [Stash Mac](/stash-mac)
* 常见问题

  + [编写高效配置](/faq/effective-stash)
  + [防止代理被检测](/faq/proxy-detected)
  + [授权与激活](/faq/license-activation)
  + [TestFlight 相关](/faq/testflight)
  + [IPv6 兼容性](/faq/ipv6-compatible)
  + [URL Schema](/faq/url-schema)
  + [越狱修改内存限制](/faq/jailbreak-ios-memory-limit)
  + [无法安装帮助程序 (Helper)](/faq/stash-mac-helper)
  + [Stash 与其他 VPN 冲突](/faq/conflict-with-vpn)

On This Page

* [Stash on iOS](#stash-on-ios)
* [不能通过 TestFlight 激活 Stash ？](#不能通过-testflight-激活-stash-)
* [Stash on macOS](#stash-on-macos)
* [Stash 已损坏？](#stash-已损坏)
* [重置激活数量](#重置激活数量)

常见问题

授权与激活

# 授权与激活

为了防止商业化的账号共享等盗版行为，目前 Stash 对每个购买凭证 (License) 有设备使用数量限制。

💡

为保障您的账户信息安全，设备列表和反激活按钮仅限在已激活的设备上显示。

## Stash on iOS

在 iOS App Store 销售的每个 Stash 授权限制最多可在 6 台设备上同时使用，包括 iOS、iPadOS、macOS (Apple silicon)。你可以在「工具 - 系统信息」(Stash V2) 或「设置 - 诊断」(Stash V1) 查看已激活设备，并反激活不再使用的设备。

### 不能通过 TestFlight 激活 Stash ？

由于 AppStore Receipt 购买凭证仅存于通过商店下载的 Stash 。如您在使用 TestFlight 过程中被其他设备反激活或者因长时间无法连接激活服务器，可能会出现此提示。

您可以重新通过 AppStore 下载正式版的 Stash 覆盖安装，即可激活。激活成功后，如有需要可升级到 TestFlight 版本继续使用。

## Stash on macOS

每个 Stash Mac 个人版 (Personal) 最多可在 3 台设备上同时使用，而家庭版和终身版 (Family & LifeTime) 最多可在 6 台设备上同时使用。你可以在「控制面板 - 设置 - 授权」查看已激活设备，并反激活不再使用的设备。

### Stash 已损坏？

部分杀毒软件或清理软件可能会导致 Stash 无法正常运行或激活，请确保没有使用这一类软件阻止或清理 Stash Mac 。如 Stash 被清理，可能会出现此提示。

您可以 [点击此处 (opens in a new tab)](https://mac-release-static.stash.ws/Stash-latest.zip) 重新下载 Stash Mac 覆盖安装以修复此问题。

## 重置激活数量

如果您遇到「激活服务器拒绝，已达到最大的设备数量」且确认激活设备数量没有超过限制，请发送电子邮件到 [info@stash.ws](mailto:info@stash.ws) 说明情况，我们会第一时间处理。

Last updated on 2023年8月3日

[防止代理被检测](/faq/proxy-detected " 防止代理被检测")[TestFlight 相关](/faq/testflight "TestFlight 相关")

---

# TestFlight 相关问题

[Stash 用户文档易用且强劲的网络工具](/)

* [Stash 简介](/)
* [快速上手](/get-started)
* 更新日志

  + [iOS](/release-notes/ios)
* 分流规则

  + [规则类型](/rules/rule-types)
  + [规则集合](/rules/rule-set)
* 代理协议

  + [协议类型](/proxy-protocols/proxy-types)
  + [策略组](/proxy-protocols/proxy-groups)
  + [远程代理集](/proxy-protocols/proxy-providers)
  + [延迟测试](/proxy-protocols/proxy-benchmark)
* 配置文件

  + [配置样例](/configuration/example-config)
  + [覆写配置（Override）](/configuration/override)
  + [策略组图标](/configuration/proxy-group-icon)
* HTTP 引擎

  + [简介](/http-engine/intro)
  + [MitM](/http-engine/mitm)
  + [强制 HTTP 引擎](/http-engine/force-http-engine)
  + [HTTP 重写](/http-engine/rewrite)
* JavsScript 脚本

  + [语法与接口](/script/syntax-and-interface)
  + [改写 HTTP](/script/rewrite-requests)
  + [面板（Tile）](/script/tile)
  + [定时任务](/script/scheduled-tasks)
* 功能介绍

  + [内置 DNS 服务](/features/dns-server)
  + [为局域网设备提供代理](/features/provide-proxy-to-lan-device)
  + [服务提供商订阅](/features/service-provider-subscription)
  + [网络性能增强](/features/network-performance-enhance)
  + [按需启动](/features/on-demand)
* [Stash Mac](/stash-mac)
* 常见问题

  + [编写高效配置](/faq/effective-stash)
  + [防止代理被检测](/faq/proxy-detected)
  + [授权与激活](/faq/license-activation)
  + [TestFlight 相关](/faq/testflight)
  + [IPv6 兼容性](/faq/ipv6-compatible)
  + [URL Schema](/faq/url-schema)
  + [越狱修改内存限制](/faq/jailbreak-ios-memory-limit)
  + [无法安装帮助程序 (Helper)](/faq/stash-mac-helper)
  + [Stash 与其他 VPN 冲突](/faq/conflict-with-vpn)

常见问题

TestFlight 相关

# TestFlight 相关问题

Stash 通过在 TestFlight 分发 Beta 版本进行灰度测试。所有购买用户均可申请参与 TestFlight 测试。在 **App Store 安装的 Stash** 内，您可以在「设置 - 更多设置」中输入邮箱，即可收到 TestFlight 发出的邀请。

💡

在安装 TestFlight 版本之前，请到「工具 - 系统信息」(Stash V2) 或「设置 -
诊断」(Stash V1) 确认当前设备授权的有效状态。由于 Apple 沙盒的限制，目前无法在
TestFlight 版本进行设备激活。

* 由于 Apple 的限制，TestFlight 最多允许 10000 个账号参与。Stash Network Ltd. 保留移除不活跃账号的权利。
* 申请 TestFlight 的 Apple ID 可以与购买账号不同，但每个购买账号在同一时间只能拥有一个 TestFlight 名额。重复申请时，旧名额会被移除。
* 由于 Stash 并没有在中国区上架，请不要使用中国区的 Apple ID 申请 TestFlight。使用中国区的 Apple ID 可能会遇到「所请求的 App 不可用或不存在」的问题。
* TestFlight 属于 Beta（测试）版本性质。在体验新功能的同时可能会存在 Bug 或者不稳定情况。请根据自己的实际情况切换至 App Store 商店版或 TestFlight 测试版。

Last updated on 2024年8月4日

[授权与激活](/faq/license-activation "授权与激活")[IPv6 兼容性](/faq/ipv6-compatible "IPv6 兼容性")

---

# IPv6 兼容性

[Stash 用户文档易用且强劲的网络工具](/)

* [Stash 简介](/)
* [快速上手](/get-started)
* 更新日志

  + [iOS](/release-notes/ios)
* 分流规则

  + [规则类型](/rules/rule-types)
  + [规则集合](/rules/rule-set)
* 代理协议

  + [协议类型](/proxy-protocols/proxy-types)
  + [策略组](/proxy-protocols/proxy-groups)
  + [远程代理集](/proxy-protocols/proxy-providers)
  + [延迟测试](/proxy-protocols/proxy-benchmark)
* 配置文件

  + [配置样例](/configuration/example-config)
  + [覆写配置（Override）](/configuration/override)
  + [策略组图标](/configuration/proxy-group-icon)
* HTTP 引擎

  + [简介](/http-engine/intro)
  + [MitM](/http-engine/mitm)
  + [强制 HTTP 引擎](/http-engine/force-http-engine)
  + [HTTP 重写](/http-engine/rewrite)
* JavsScript 脚本

  + [语法与接口](/script/syntax-and-interface)
  + [改写 HTTP](/script/rewrite-requests)
  + [面板（Tile）](/script/tile)
  + [定时任务](/script/scheduled-tasks)
* 功能介绍

  + [内置 DNS 服务](/features/dns-server)
  + [为局域网设备提供代理](/features/provide-proxy-to-lan-device)
  + [服务提供商订阅](/features/service-provider-subscription)
  + [网络性能增强](/features/network-performance-enhance)
  + [按需启动](/features/on-demand)
* [Stash Mac](/stash-mac)
* 常见问题

  + [编写高效配置](/faq/effective-stash)
  + [防止代理被检测](/faq/proxy-detected)
  + [授权与激活](/faq/license-activation)
  + [TestFlight 相关](/faq/testflight)
  + [IPv6 兼容性](/faq/ipv6-compatible)
  + [URL Schema](/faq/url-schema)
  + [越狱修改内存限制](/faq/jailbreak-ios-memory-limit)
  + [无法安装帮助程序 (Helper)](/faq/stash-mac-helper)
  + [Stash 与其他 VPN 冲突](/faq/conflict-with-vpn)

常见问题

IPv6 兼容性

# IPv6 兼容性

在绝大多数情况下，您无需手动启用 IPv6。Stash 会根据 iOS / macOS 系统返回的 IPv4 / IPv6 状态，自动选择最佳的连接策略。当 IPv4 / IPv6 都可用时，Stash 会同时向 IPv4 / IPv6 发起 TCP 握手，并选择第一个成功握手的连接进行后续数据传输。

在代理服务器支持 IPv6 的情况下，由于 Stash 使用 Fake IP 机制，通常会尽可能地向代理服务器转发域名而不是 IP 请求。此时 IPv4 / IPv6 的选择取决于代理服务器。

由于 Fake IP 机制的存在，Stash Tunnel 的大部分情况下会接受 Fake IP 的路由，并由 Stash 将 Fake IP 反查域名，**Stash Tunnel 默认仅启用 IPv4**。对于大多数 HTTP(S) 请求，即使直接输入 IPv6 地址，由于存在 HTTP 代理，请求并不会经过 Stash Tunnel。在上述两种机制下，Stash 默认支持：

* 通过域名访问仅支持 IPv6 的服务器
* 直接通过 IP 访问仅支持 IPv6 的网站

对于直接通过 IPv6 访问且经由 Stash Tunnel 的情况（如 SSH、FTP 等），需要开启「网络设置 - 启用 Tunnel IPv6 路由」。**请注意，在网络环境不支持 IPv6 的情况下开启该功能，可能会导致兼容性问题。**

Last updated on 2024年8月4日

[TestFlight 相关](/faq/testflight "TestFlight 相关")[URL Schema](/faq/url-schema "URL Schema")

---

# URL Schema

[Stash 用户文档易用且强劲的网络工具](/)

* [Stash 简介](/)
* [快速上手](/get-started)
* 更新日志

  + [iOS](/release-notes/ios)
* 分流规则

  + [规则类型](/rules/rule-types)
  + [规则集合](/rules/rule-set)
* 代理协议

  + [协议类型](/proxy-protocols/proxy-types)
  + [策略组](/proxy-protocols/proxy-groups)
  + [远程代理集](/proxy-protocols/proxy-providers)
  + [延迟测试](/proxy-protocols/proxy-benchmark)
* 配置文件

  + [配置样例](/configuration/example-config)
  + [覆写配置（Override）](/configuration/override)
  + [策略组图标](/configuration/proxy-group-icon)
* HTTP 引擎

  + [简介](/http-engine/intro)
  + [MitM](/http-engine/mitm)
  + [强制 HTTP 引擎](/http-engine/force-http-engine)
  + [HTTP 重写](/http-engine/rewrite)
* JavsScript 脚本

  + [语法与接口](/script/syntax-and-interface)
  + [改写 HTTP](/script/rewrite-requests)
  + [面板（Tile）](/script/tile)
  + [定时任务](/script/scheduled-tasks)
* 功能介绍

  + [内置 DNS 服务](/features/dns-server)
  + [为局域网设备提供代理](/features/provide-proxy-to-lan-device)
  + [服务提供商订阅](/features/service-provider-subscription)
  + [网络性能增强](/features/network-performance-enhance)
  + [按需启动](/features/on-demand)
* [Stash Mac](/stash-mac)
* 常见问题

  + [编写高效配置](/faq/effective-stash)
  + [防止代理被检测](/faq/proxy-detected)
  + [授权与激活](/faq/license-activation)
  + [TestFlight 相关](/faq/testflight)
  + [IPv6 兼容性](/faq/ipv6-compatible)
  + [URL Schema](/faq/url-schema)
  + [越狱修改内存限制](/faq/jailbreak-ios-memory-limit)
  + [无法安装帮助程序 (Helper)](/faq/stash-mac-helper)
  + [Stash 与其他 VPN 冲突](/faq/conflict-with-vpn)

On This Page

* [link.stash.ws](#linkstashws)
* [导入配置文件](#导入配置文件)
* [导入远程覆写](#导入远程覆写)
* [导入图标集](#导入图标集)
* [开关 Stash](#开关-stash)
* [开启 Stash](#开启-stash)
* [关闭 Stash](#关闭-stash)
* [切换开关](#切换开关)

常见问题

URL Schema

# URL Schema

Stash 支持使用 URL Schema `stash://` 和 `clash://` 来控制 Stash， 包含的 URL **需要 Encode 。**

### link.stash.ws

除了上述的 URL Schema 之外，Stash 还支持使用 `https://link.stash.ws` 标准 URL 来控制，格式为 `https://link.stash.ws/command/url`，包含的 URL **不含 Schema 且无需 Encode 。**

以一键安装 BoxJS 为例，

原 URL：`https://raw.githubusercontent.com/chavyleung/scripts/master/box/rewrite/boxjs.rewrite.stash.stoverride`

一键安装 URL：`https://link.stash.ws/install-override/raw.githubusercontent.com/chavyleung/scripts/master/box/rewrite/boxjs.rewrite.stash.stoverride`

💡

默认的远程 URL Schema 为 HTTPS ，如需使用 HTTP ，请加上参数 `?scheme=http`。

💡

如远程 URL 无法访问，链接将返回 `404`。

## 导入配置文件

* `stash://install-config?url=${url-encoded}`
* `clash://install-config?url=${url-encoded}`
* `https://link.stash.ws/install-config/example.com/stash.yaml`

## 导入远程覆写

* `stash://install-override?url=${url-encoded}`
* `clash://install-override?url=${url-encoded}`
* `https://link.stash.ws/install-override/example.com/stash.stoverride`

## 导入图标集

* `stash://install-icon-set?url=${url-encoded}`
* `clash://install-icon-set?url=${url-encoded}`
* `https://link.stash.ws/install-icon-set/example.com/stash.json`

## 开关 Stash

### 开启 Stash

* `stash://start`
* `clash://start`
* `https://link.stash.ws/start`

### 关闭 Stash

* `stash://stop`
* `clash://stop`
* `https://link.stash.ws/stop`

### 切换开关

* `stash://toggle`
* `clash://toggle`
* `https://link.stash.ws/toggle`

Last updated on 2023年6月3日

[IPv6 兼容性](/faq/ipv6-compatible "IPv6 兼容性")[越狱修改内存限制](/faq/jailbreak-ios-memory-limit "越狱修改内存限制")

---

# 越狱 iOS 系统内存限制修改

[Stash 用户文档易用且强劲的网络工具](/)

* [Stash 简介](/)
* [快速上手](/get-started)
* 更新日志

  + [iOS](/release-notes/ios)
* 分流规则

  + [规则类型](/rules/rule-types)
  + [规则集合](/rules/rule-set)
* 代理协议

  + [协议类型](/proxy-protocols/proxy-types)
  + [策略组](/proxy-protocols/proxy-groups)
  + [远程代理集](/proxy-protocols/proxy-providers)
  + [延迟测试](/proxy-protocols/proxy-benchmark)
* 配置文件

  + [配置样例](/configuration/example-config)
  + [覆写配置（Override）](/configuration/override)
  + [策略组图标](/configuration/proxy-group-icon)
* HTTP 引擎

  + [简介](/http-engine/intro)
  + [MitM](/http-engine/mitm)
  + [强制 HTTP 引擎](/http-engine/force-http-engine)
  + [HTTP 重写](/http-engine/rewrite)
* JavsScript 脚本

  + [语法与接口](/script/syntax-and-interface)
  + [改写 HTTP](/script/rewrite-requests)
  + [面板（Tile）](/script/tile)
  + [定时任务](/script/scheduled-tasks)
* 功能介绍

  + [内置 DNS 服务](/features/dns-server)
  + [为局域网设备提供代理](/features/provide-proxy-to-lan-device)
  + [服务提供商订阅](/features/service-provider-subscription)
  + [网络性能增强](/features/network-performance-enhance)
  + [按需启动](/features/on-demand)
* [Stash Mac](/stash-mac)
* 常见问题

  + [编写高效配置](/faq/effective-stash)
  + [防止代理被检测](/faq/proxy-detected)
  + [授权与激活](/faq/license-activation)
  + [TestFlight 相关](/faq/testflight)
  + [IPv6 兼容性](/faq/ipv6-compatible)
  + [URL Schema](/faq/url-schema)
  + [越狱修改内存限制](/faq/jailbreak-ios-memory-limit)
  + [无法安装帮助程序 (Helper)](/faq/stash-mac-helper)
  + [Stash 与其他 VPN 冲突](/faq/conflict-with-vpn)

常见问题

越狱修改内存限制

# 越狱 iOS 系统内存限制修改

Jetsam 在 iOS 中负责监控内存并进行 OOM kill。在系统默认配置中，不同类型的进程有不同的内存限制。在 iOS 14 及之前的系统中，Network Extension 的内存限制为 15 MB；而在 iOS 15 及以后，Network Extension 的内存限制增加到了 50 MB。

对于越狱用户，可以修改这个值以允许 Network Extension 使用更多内存。这个配置文件存放在 `/System/Library/LaunchDaemons/com.apple.jetsamproperties.{Model}.plist`。

打开任意一个文件后搜索 `com.apple.networkextension.packet-tunnel` 这个键即可找到 Network Extension 的限制。建议将其修改为 50 到 100 之间的任意数值。`ActiveHardMemoryLimit` 和 `InactiveHardMemoryLimit` 都需要修改。

```
<key>com.apple.networkextension.packet-tunnel</key>
<dict>
    <key>ActiveHardMemoryLimit</key>
    <integer>50</integer>
    <key>InactiveHardMemoryLimit</key>
    <integer>50</integer>
    <key>JetsamPriority</key>
    <integer>14</integer>
</dict>
```

* 在操作前务必备份数据。
* 不同手机的 Model 可能各不相同，也可能存在多个类似文件，如果不确定本机匹配的 Model，可以尝试修改所有相关文件。
* 修改后，需重启 iOS 系统才能生效。

您可以在 [github.com/eycorsican/jetsamproperties (opens in a new tab)](https://github.com/eycorsican/jetsamproperties) 项目中获取更多信息。

Last updated on 2024年8月4日

[URL Schema](/faq/url-schema "URL Schema")[无法安装帮助程序 (Helper)](/faq/stash-mac-helper "无法安装帮助程序 (Helper)")

---

# 无法安装 Stash Mac 帮助程序 (Helper)

[Stash 用户文档易用且强劲的网络工具](/)

* [Stash 简介](/)
* [快速上手](/get-started)
* 更新日志

  + [iOS](/release-notes/ios)
* 分流规则

  + [规则类型](/rules/rule-types)
  + [规则集合](/rules/rule-set)
* 代理协议

  + [协议类型](/proxy-protocols/proxy-types)
  + [策略组](/proxy-protocols/proxy-groups)
  + [远程代理集](/proxy-protocols/proxy-providers)
  + [延迟测试](/proxy-protocols/proxy-benchmark)
* 配置文件

  + [配置样例](/configuration/example-config)
  + [覆写配置（Override）](/configuration/override)
  + [策略组图标](/configuration/proxy-group-icon)
* HTTP 引擎

  + [简介](/http-engine/intro)
  + [MitM](/http-engine/mitm)
  + [强制 HTTP 引擎](/http-engine/force-http-engine)
  + [HTTP 重写](/http-engine/rewrite)
* JavsScript 脚本

  + [语法与接口](/script/syntax-and-interface)
  + [改写 HTTP](/script/rewrite-requests)
  + [面板（Tile）](/script/tile)
  + [定时任务](/script/scheduled-tasks)
* 功能介绍

  + [内置 DNS 服务](/features/dns-server)
  + [为局域网设备提供代理](/features/provide-proxy-to-lan-device)
  + [服务提供商订阅](/features/service-provider-subscription)
  + [网络性能增强](/features/network-performance-enhance)
  + [按需启动](/features/on-demand)
* [Stash Mac](/stash-mac)
* 常见问题

  + [编写高效配置](/faq/effective-stash)
  + [防止代理被检测](/faq/proxy-detected)
  + [授权与激活](/faq/license-activation)
  + [TestFlight 相关](/faq/testflight)
  + [IPv6 兼容性](/faq/ipv6-compatible)
  + [URL Schema](/faq/url-schema)
  + [越狱修改内存限制](/faq/jailbreak-ios-memory-limit)
  + [无法安装帮助程序 (Helper)](/faq/stash-mac-helper)
  + [Stash 与其他 VPN 冲突](/faq/conflict-with-vpn)

On This Page

* [macOS 13 Ventura](#macos-13-ventura)
* [修复步骤](#修复步骤)

常见问题

无法安装帮助程序 (Helper)

# 无法安装 Stash Mac 帮助程序 (Helper)

部分用户可能会遇到反复提示需要安装帮助程序 (Helper) 的情况。Stash 需要使用管理员权限安装一个帮助程序，否则 Stash 将无法设置系统代理。

⚠️

部分杀毒软件或清理软件可能会导致 Stash Helper
无法正常运行，请确保没有使用这一类软件阻止或清理 Stash Mac 。

## macOS 13 Ventura

在 macOS 13 苹果引入了新的后台权限管理，如错误配置此项会引起 Stash Helper 无法正常运行。

* 在 Mac 的「系统设置」 - 「通用」 - 「登陆项」 - 「允许在后台」，请确保 `Stash` 或 `Stash Networks Limited` 等开关为启用状态。

## 修复步骤

如执行上述操作后依然无法安装 Stash Helper ，请尝试参照以下步骤修复：

1. 打开终端 (Terminal)。
2. 运行以下命令移除 Helper （需输入系统密码并按回车键）。

```
sudo rm -rf /Library/PrivilegedHelperTools/ws.stash.app.mac.daemon.helper
```

3. 运行以下命令启用 Helper （需输入系统密码并按回车键）。

```
sudo /bin/launchctl load -w /Library/LaunchDaemons/ws.stash.app.mac.daemon.helper.plist
```

如提示 `service already loaded` 或 `Operation already in progress` ，无需理会。

4. 重启电脑。
5. 打开 Stash ，重新安装帮助程序（需输入系统密码）。

至此，您的 Stash Helper 已修复。如果仍然不能正常工作，请与 [info@stash.ws](mailto:info@stash.ws) 联系。

Last updated on 2023年8月1日

[越狱修改内存限制](/faq/jailbreak-ios-memory-limit "越狱修改内存限制")[Stash 与其他 VPN 冲突](/faq/conflict-with-vpn "Stash 与其他 VPN 冲突")

---

# Stash 与其他 VPN 的冲突解决方法

[Stash 用户文档易用且强劲的网络工具](/)

* [Stash 简介](/)
* [快速上手](/get-started)
* 更新日志

  + [iOS](/release-notes/ios)
* 分流规则

  + [规则类型](/rules/rule-types)
  + [规则集合](/rules/rule-set)
* 代理协议

  + [协议类型](/proxy-protocols/proxy-types)
  + [策略组](/proxy-protocols/proxy-groups)
  + [远程代理集](/proxy-protocols/proxy-providers)
  + [延迟测试](/proxy-protocols/proxy-benchmark)
* 配置文件

  + [配置样例](/configuration/example-config)
  + [覆写配置（Override）](/configuration/override)
  + [策略组图标](/configuration/proxy-group-icon)
* HTTP 引擎

  + [简介](/http-engine/intro)
  + [MitM](/http-engine/mitm)
  + [强制 HTTP 引擎](/http-engine/force-http-engine)
  + [HTTP 重写](/http-engine/rewrite)
* JavsScript 脚本

  + [语法与接口](/script/syntax-and-interface)
  + [改写 HTTP](/script/rewrite-requests)
  + [面板（Tile）](/script/tile)
  + [定时任务](/script/scheduled-tasks)
* 功能介绍

  + [内置 DNS 服务](/features/dns-server)
  + [为局域网设备提供代理](/features/provide-proxy-to-lan-device)
  + [服务提供商订阅](/features/service-provider-subscription)
  + [网络性能增强](/features/network-performance-enhance)
  + [按需启动](/features/on-demand)
* [Stash Mac](/stash-mac)
* 常见问题

  + [编写高效配置](/faq/effective-stash)
  + [防止代理被检测](/faq/proxy-detected)
  + [授权与激活](/faq/license-activation)
  + [TestFlight 相关](/faq/testflight)
  + [IPv6 兼容性](/faq/ipv6-compatible)
  + [URL Schema](/faq/url-schema)
  + [越狱修改内存限制](/faq/jailbreak-ios-memory-limit)
  + [无法安装帮助程序 (Helper)](/faq/stash-mac-helper)
  + [Stash 与其他 VPN 冲突](/faq/conflict-with-vpn)

常见问题

Stash 与其他 VPN 冲突

# Stash 与其他 VPN 的冲突解决方法

为避免 Stash 与其他 VPN 之间发生冲突，您可以通过绑定网卡的方式进行设置。请[参考此处](/proxy-protocols/proxy-types#direct-with-specified-interface)。

Last updated on 2024年8月4日

[无法安装帮助程序 (Helper)](/faq/stash-mac-helper "无法安装帮助程序 (Helper)")

---

