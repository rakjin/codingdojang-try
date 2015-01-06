#!/usr/bin/perl

use utf8;
use strict;
use warnings;

use Test::More;

my $pattern_hangul = qr/\p{Hangul}/;
my $pattern_xmlchar = qr/&#\d+;/;
my $pattern = qr/$pattern_hangul|$pattern_xmlchar/;

sub length_considering_multibyte_character {
	my $str = shift;
	$str =~ s/$pattern/AA/g;
	return length $str;
}

sub trim_tail {
	my ($str, $ellipsis, $desired_length) = @_;

	if (length_considering_multibyte_character($str) <= $desired_length) {
		return $str;
	}

	return "";
}


is( length_considering_multibyte_character("world"), 5 );
is( length_considering_multibyte_character("한글"), 4 );
is( length_considering_multibyte_character("&#12345;"), 2 );
is( length_considering_multibyte_character("&#abcde;"), 8 );
is( length_considering_multibyte_character("&#;"), 3 );
is( length_considering_multibyte_character("&#&#12345;;"), 5 );
is( length_considering_multibyte_character("&#&#12345;;큐"), 7 );
is( trim_tail("12345", "..", 5), '12345');
is( trim_tail("한글", "..", 5), '한글');
is( trim_tail("한글", "..", 4), '한글');
is( trim_tail("한&#12345;글", "..", 6), '한&#12345;글');
TODO: {
	local $TODO = "trim tail";
	is( trim_tail("1234567890", "..", 5), "123.." );
}
done_testing();
