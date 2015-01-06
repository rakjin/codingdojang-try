#!/usr/bin/perl

use utf8;
use strict;
use warnings;

use Test::More;
use Encode qw(encode decode);

use constant MULTIBYTE_CHARACTER_SIZE => 2;

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

	my @result = ();
	my $output_length = 0;
	my $ellipsis_length = length_considering_multibyte_character($ellipsis);
	$desired_length -= $ellipsis_length;

	while ($output_length < $desired_length) {
		if ($str =~ s/^($pattern)//) {
			if ($output_length + MULTIBYTE_CHARACTER_SIZE <= $desired_length) {
				push @result, $1;
			}
			$output_length += MULTIBYTE_CHARACTER_SIZE;
		}
		elsif ($str =~ s/^(((?!($pattern)).)+)//) {
			my $found = substr($1, 0, $desired_length - $output_length);
			push @result, $found;
			$output_length += length $found;
		}
		else {
			print "\t\tnot expected\n";
		}
	}
	push @result, $ellipsis;
	return join '', @result;
}

sub test {
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
	is( trim_tail("1234567890", "..", 5), "123.." );
	is( trim_tail("한글12345", "..", 5), "한.." );
	is( trim_tail("123한글12345", "..", 7), "123한.." );
	is( trim_tail("123한글12345", "..", 8), "123한.." );
	is( trim_tail("a한a글a한a한a", "..", 12), "a한a글a한a.." );
	is( trim_tail("a한a글a한a한a", "(...더보기)", 12), "a(...더보기)" );
	done_testing();
}

sub process_stdin {
	while (<>) {
		chomp;
		my ($str, $ellipsis, $desired_length) = split /\//;
		$str = decode('utf-8', $str);
		$ellipsis = decode('utf-8', $ellipsis);
		my $result = trim_tail($str, $ellipsis, $desired_length);
		print encode('utf-8', "$result\n");
	}
}

sub main {
	if ( -t STDIN and not @ARGV ) {
		test;
	}
	else {
		process_stdin;
	}
}

main;
