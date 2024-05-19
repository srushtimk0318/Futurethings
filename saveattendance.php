<?php

    include_once('db.php');
    // $conn=mysqli_connect('localhost','root','','internship');

    // if( !$conn )
    // {
    //     die(mysqli_connect_error()); 
    // }

    // echo "Ok connected";

    $sql="insert into attendance(name,cdate,ctime) values('sushmitha',current_date(),current_time())";
    $res=execute( $sql );
    // $res=$conn->query($sql);


    // if( !$res )
    // {
    //     die( mysqli_error($conn)); 
    // }


    echo "<h2>Record got saved</h2>";

?>