<?php
	$file_str="/1111/.index.php";
	$method = "post";
	$passwd = "a";
	$ip="http://192.168.45.";
	for($i=1;$i<=30;$i++){
		echo $ip.$i.$file_str.",".$method .",".$passwd."<br>";
	}
?>
