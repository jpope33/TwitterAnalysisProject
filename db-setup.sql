drop database ssdi;
create database ssdi;

use ssdi;

create table twitter_results (
  twitterHandle varchar(30) not null primary key,
  tweetInfo varchar(1000) not null
);
