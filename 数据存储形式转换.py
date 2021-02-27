set_time_limit (0);
$mongo_connect = new Mongo();
$mongo = $mongo_connect->script->script_5;
$mongo_info = $mongo->find();
$mysql_connect = mysql_connect('127.0.0.1','root','zhiyingbao');
mysql_select_db('artical', $mysql_connect);
mysql_query("SET NAMES utf8"); 
foreach ($mongo_info as $v){
   if(empty($v['title'])){
      $v['title'] = ". ";
   }
   if(empty($v['desc'])){
      $v['desc'] = ". ";
   }
   if(empty($v['content'])){
      $v['content'] = ". ";
   }
   if(empty($v['tag'])){
      $v['tag'] = ". ";
   }
   $sql = "INSERT INTO `script`.`artical_2` (`title`, `desc`, 
`content`, `tag`) VALUES ('".$v['title']."', '".$v['desc']."', '".$v['content']."', '".$v['tag']."');";
   $res = mysql_query($sql, $mysql_connect);
   if($res){
      echo "success!<br />";
   }else{
      echo "fail!<br />";
    }
 }
