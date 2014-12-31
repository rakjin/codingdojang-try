use strict;
use warnings;

my ($height, $width) = split / /, <>;

my $y = 0;
my @table = ();
while(<>) {
  my $x = 0;
  my @row = ();
  for my $altitude (split / /) {
    $altitude =~ s/\s//g;
    my $node = {
      "altitude" => $altitude,
      "adjacents" => [],
      "is_destination" => 0,
      };
    push @row, $node;
    if ($x > 0) {
      my $left = $row[$x-1];
      my $left_altitude = $left->{"altitude"};
      
      if ($altitude > $left_altitude) {
        push @{$node->{"adjacents"}}, $left;
      }
      elsif ($altitude < $left_altitude) {
        push @{$left->{"adjacents"}}, $node;
      }
    }
    if ($y > 0) {
      my $upper = $table[$y-1][$x];
      my $upper_altitude = $upper->{"altitude"};

      if ($altitude > $upper_altitude) {
        push @{$node->{"adjacents"}}, $upper;
      }
      elsif ($altitude < $upper_altitude) {
        push @{$upper->{"adjacents"}}, $node;
      }
    }
    $x++;
  }
  push @table, \@row;
  $y++;
}

my $first_node = $table[0][0];
my $last_node = $table[-1][-1];
$last_node->{"is_destination"} = 1;  


sub visit {
  my $node = shift;
  my $path = shift;

  if (grep /^$node$/, @{$path}) {
    return 0;
  }
  if ($node->{"is_destination"}) {
    return 1;
  }
  my $count = 0;
  push @{$path}, $node;
  for my $adjacent (@{$node->{"adjacents"}}) {
    $count += visit($adjacent, $path);
  }
  pop @{$path};
  return $count;
}


my $path = [];
my $count = visit($first_node, $path);
print ($count);
