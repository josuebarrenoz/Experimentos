<?php
class User extends account {
    public function __construct($name, $password, $email, $document){
        parent::__construct($name, $password, $email, $document);
    }
}
?>