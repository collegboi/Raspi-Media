<?php
	
	$action = $_GET["action"];
	
	$jsonArray = array();
	
	if($action == null) {
	
		$jsonArray = array(
			"error"=>"no paramters"
			);
	}
	
	if($action == "movie") {
	
	
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
	
	} else if ($action == "tv") {
		
		$tv = $_GET["tv"];
		$season = $_GET["season"];
		$episode = $_GET["episode"];
		$avil = $_GET["avail"];
		$dbAction = $_GET["db"];
		
		
		exec("python server.py ".$tv." ".$season." ".$episode." ".$avil." ".$dbAction, $output);
		
		var_dump($output);
	}
	
	
	echo json_encode($jsonArray);


?>
