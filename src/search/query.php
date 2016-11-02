<?php
	$query = $_POST['query'];
	//echo $query;
	//$query = "'";
	require 'vendor/autoload.php';

	$client = new MongoDB\Client("mongodb://localhost:27017");
	$collection = $client->selectCollection('bigdata','indiceinv');

	$results = $collection->findOne( ['Palabra' => $query] );

	for ($i=0; $i < 10; $i++) { 
		$queryResult[$i] = $results['docs'][$i]['nombre'];
	}
	echo json_encode($queryResult);
	/*
	for ($i=0; $i < 10; $i++) { 
		$data[$i]= $i;
	}
	echo json_encode($data);*/
?>
