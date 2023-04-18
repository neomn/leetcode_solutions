<?php

class TimeMap
{
    private $store;

    function __construct()
    {
        $this->store = [];
    }

    function set($key, $value, $timestamp)
    {
        $this->store[$key][] = [$timestamp => $value];
    }

    function get($key, $timestamp)
    {
        // $result = array_reduce($store[$key], function($item, $timestamp){

        //   retur

        // });
        return $this->store[$key];
    }
}

$timemap = new TimeMap();
$timemap->set('test', 'value 1', 1);
$timemap->set('test', 'value 2', 2);
$timemap->set('test', 'value 3', 3);

print_r($timemap->get('test', 2));
