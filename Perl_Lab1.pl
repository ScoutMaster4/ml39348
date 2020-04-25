# Łukasz Maćkiewicz
# 39348
# 31B
# Zadanie na ocenę 3.0
#!/usr/bin/perl
use Cwd;
if(@ARGV != undef){
$sciezka = @ARGV[0];
@tab = ();
#print "sciezka wykryta: $sciezka\n";

opendir ($dh, $sciezka) or die "blad '$sciezka': $!";
while($plik = readdir $dh)
{
  push(@tab, $plik);
  #print "$plik \n" unless ($plik eq '.' or $plik eq '..');
}
@sort = sort @tab;

for($i = 0; $i < scalar @sort; $i++)
{
  print "@sort[$i] \n" unless (@sort[$i] eq '.' or @sort[$i] eq '..');
}
closedir ($dh);
}
else
{
  $cwd = getcwd;
  #print "sciezka wykryta: $cwd \n";
  opendir ($dh, $cwd) or die "blad '$cwd': $!";
  while($plik = readdir $dh)
  {
    push(@tab, $plik);
    #print "$plik \n" unless ($plik eq '.' or $plik eq '..');
  }
  @sort = sort @tab;

  for($i = 0; $i < scalar @sort; $i++)
  {
    print "@sort[$i] \n" unless (@sort[$i] eq '.' or @sort[$i] eq '..');
  }
  closedir ($dh);
}
