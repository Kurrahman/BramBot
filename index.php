<!DOCTYPE html>
<html>
<head>
	<title>BramBot</title>
	<!-- menghubungkan dengan file css -->
	<link rel="stylesheet" type="text/css" href="style.css">
	<!-- menghubungkan dengan file jquery -->
	<script type="text/javascript" src="jquery.js"></script>
</head>
<body>
<div class="content">
	<header>
		<h1 class="judul">BramBot</h1>
		<h3 class="deskripsi">Berbicara dengan Bram tapi sebagai Bot</h3>
	</header>

	<div class="badan">
		<?php
			$img = 0;
			$history = array("Bram : Silahkan ajukan pertanyaan");
			$quest = NULL;
			$files = glob('sprite/*');
			$output = array("misal", "coba", "sembarang");
			include "halaman/home.php";
		?>	
	</div>
</div>
</body>
</html>