#!/usr/bin/perl

use utf8;
use strict;
use warnings;

use Test::More;

my $pattern = qr/\p{Hangul}/;

sub length_considering_multibyte_character {
	my $str = shift;
	$str =~ s/$pattern/AA/g;
	return length $str;
}



is( length_considering_multibyte_character("world"), 5 );
is( length_considering_multibyte_character("한글"), 4 );
done_testing();
