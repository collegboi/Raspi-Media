<?php
	
	$movie = $_GET["movie"];
	$year = $_GET["year"];
	
	if($movie != null && $year != null) {
		
		exec("python moviesScrap.py ".$movie." ".$year, $output);
		//var_dump($output);
	
		//192.168.1.14:9091/transmission/rpc/ responded: "success"
		//$array = explode(':', $output);
	
		$jsonArray = array(
			"result"=>$output
			);
			
	} else {
		
		$jsonArray = array(
			"error"=>"name and year"
		);
	}
		
	echo json_encode($jsonArray);


?>
