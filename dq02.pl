#!/usr/bin/perl

use strict;
use warnings;

use Test::More;

sub length_considering_multibyte_character {
	my $str = shift;
	return length $str;
}



ok( length_considering_multibyte_character("world") == 5 );
done_testing();
