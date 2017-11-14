<?php
error_reporting(0);
define('LOG_FILENAME', 'log.txt');	
function waf() {
    if (!function_exists('getallheaders')) {
        function getallheaders() {
            foreach ($_SERVER as $name => $value) {
                if (substr($name, 0, 5) == 'HTTP_') $headers[str_replace(' ', '-', ucwords(strtolower(str_replace('_', ' ', substr($name, 5))))) ] = $value;
            }
            return $headers;
        }
    }
    $get = $_GET;
    $post = $_POST;
    $cookie = $_COOKIE;
    $header = getallheaders();
    $files = $_FILES;
    $ip = $_SERVER["REMOTE_ADDR"];
    $method = $_SERVER['REQUEST_METHOD'];
    $filepath = $_SERVER["SCRIPT_NAME"];
    //rewirte shell which uploaded by others, you can do more
    foreach ($_FILES as $key => $value) {
        $files[$key]['content'] = file_get_contents($_FILES[$key]['tmp_name']);
        file_put_contents($_FILES[$key]['tmp_name'], "virink");
    }
    unset($header['Accept']); //fix a bug
    $input = array(
        "Get" => $get,
        "Post" => $post,
        "Cookie" => $cookie,
        "File" => $files,
        "Header" => $header
    );
    //deal with
    $pattern = "select|insert|update|delete|and|or|\'|\/\*|\*|\.\.\/|\.\/|union|into|load_file|outfile|dumpfile|sub|hex";
    $pattern.= "|file_put_contents|fwrite|curl|system|eval|assert";
    $pattern.= "|passthru|exec|system|chroot|scandir|chgrp|chown|shell_exec|proc_open|proc_get_status|popen|ini_alter|ini_restore";
    $pattern.= "|`|dl|openlog|syslog|readlink|symlink|popepassthru|stream_socket_server|assert|pcntl_exec";
    $vpattern = explode("|", $pattern);
    $bool = false;
    foreach ($input as $k => $v) {
        foreach ($vpattern as $value) {
            foreach ($v as $kk => $vv) {
                if (preg_match("/$value/i", $vv)) {
                    $bool = true;
                    logging($input);
                    break;
                }
            }
            if ($bool) break;
        }
        if ($bool) break;
    }
}
function logging($var) {
	date_default_timezone_set("Asia/Shanghai");//修正时间为中国准确时间
	$time=date("Y-m-d H:i:s");//将时间赋值给变量$time
    file_put_contents(LOG_FILENAME, "\r\n\r\n\r\n" . $time . "\r\n" . print_r($var, true) , FILE_APPEND);
    // die() or unset($_GET) or unset($_POST) or unset($_COOKIE);
    
}
waf();
?>
