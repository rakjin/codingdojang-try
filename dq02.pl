#!/usr/bin/perl

use utf8;
use strict;
use warnings;

use Test::More;

my $pattern = qr/\p{Hangul}|&#[0-9]+;/;

sub length_considering_multibyte_character {
	my $str = shift;
	$str =~ s/$pattern/AA/g;
	return length $str;
}



is( length_considering_multibyte_character("world"), 5 );
is( length_considering_multibyte_character("한글"), 4 );
is( length_considering_multibyte_character("&#12345;"), 2 );
is( length_considering_multibyte_character("&#abcde;"), 8 );
is( length_considering_multibyte_character("&#;"), 3 );
is( length_considering_multibyte_character("&#&#12345;;"), 5 );
is( length_considering_multibyte_character("&#&#12345;;큐"), 7 );
done_testing();
