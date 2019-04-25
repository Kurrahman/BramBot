<div class="halaman">
	<?php
		if ($_SERVER["REQUEST_METHOD"] == "POST"){
			$tmp = "You : ";
			$tmp = $tmp.$_POST["quest"];
			array_push($history, $tmp);
			$tmp = $_POST["quest"];
			$command = 'source/main.py';
			$output = shell_exec('python '.$command. ' 2 "' .$tmp. '"');
			$arrstr = explode(';',$output);
			$tmp = 'Bram : '.$arrstr[0];
			array_push($history, $tmp);
			if (count($arrstr) == 2){
				if ((int)$arrstr[1] > 90){
					$img = 2;
				}
				else if ((int)$arrstr[1] > 50){
					$img = 0;
				}
				else{
					$img = 1;
				}
			}
			else{
				$img = 1;
			}
		}
		else{
			if ($_SERVER["REQUEST_METHOD"] == "POST") {
				$quest = $_POST["quest"];
			}
		}
		echo '<img src="' . $files[$img] . '" class="images" /><br>';
		foreach ($history as $text){
			echo $text;
			echo "<br>";
		}
	?>
	<form method = "post">
		<input type = "text" name = "quest">
	</form>
</div>