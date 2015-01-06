#!/usr/bin/perl

use strict;
use warnings;

use Test::More;

sub length_considering_multibyte_character {
	my $str = shift;
	return length $str;
}



is( length_considering_multibyte_character("world"), 5 );
TODO: {
	local $TODO = 'considering length of a hangul char as 2';
	is( length_considering_multibyte_character("한글"), 4 );
}
done_testing();
