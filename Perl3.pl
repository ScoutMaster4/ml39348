#!/usr/bin/perl
package classA;
open (FH, ">file2.csv") or die "$!";
print FH "NAME, \t\tSCORE\n";
our @n;
our @s;
$l=0;
if(@ARGV != undef){
  open (file, @ARGV[0]);
  @strings = <file>;

  $matchN = "<a.*?href.*?users.*?>([^>]*?)<\/";
  $matchS = "<td.*?class.*?>([^>]*?)<\/td><\/tr";
  foreach $a (@strings) {
     if($a =~ /headerrow/)
     {
       (@n) = $a =~ /$matchN/g;
       (@s) = $a =~ /$matchS/g;
     }
   }

   for($i = 0; $i < scalar @n; $i++)
   {
     print FH "\"$n[$i]\", \"$s[$i]\"\n";
   }
}
else
{
  print "nie podano stdin\n";
}

close(FH);
