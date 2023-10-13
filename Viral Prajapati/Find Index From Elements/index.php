<?php

$list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14];
$numFind = 11;
$index = array_search($numFind, $list);

if ($index !== false) {
    echo "Index: $index";
} else {
    echo "Element not found";
}

?>