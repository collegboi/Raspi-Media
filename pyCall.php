<?php
	
	$carReg = $_GET["carReg"];
	
	exec("python scrap.py ".$carReg, $output);
	//var_dump($output);
	
	$data = explode(" ", trim($output[0]));
	
	$color = $data[0];
	
	$carData = substr(trim($output[0]), strlen($color)+1);
	
	$year = substr($carData, 0, 4);
	
	$car = substr($carData, 4);
	
	$carArray = explode(" ", trim($car));
	
	$make = $carArray[0];
	
	$count = strlen($make);
	
	$carDetail = substr($car, $count+1);
	
	
	$jsonArray = array(
		"year"=>trim($year),
		"detail"=>trim($carDetail),
		"make"=>trim($make),
		"color"=>trim($color)
	);
	
	echo json_encode($jsonArray);
	
	?>