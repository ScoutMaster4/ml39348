# Łukasz Maćkiewicz
# 39348
# 31B
# Zadanie na ocenę 3.0
#!/usr/bin/perl
if(@ARGV != undef){
  open (file, @ARGV[0]);
  @strings = <file>;
  $sumaGodzin = 0;
  $sumaGodzinLekcyjnych = 0;
  $dtstart = 0;
  $dtend = 0;
  #$licznik = 0;
  foreach $a (@strings) {
     if($a =~ /DTSTART/)
     {
       #$licznik++;
       $a =~ /\d*[T](\d{2})/;
       $dtstart = $1;
       #print "dtstart: $dtstart\n";
     }
     if($a =~ /DTEND/)
     {
       $a =~ /\d*[T](\d{2})/;
       $dtend = $1;
       #print "dtend: $dtend\n";
       $temp = ($dtend - $dtstart);
       #print "temp: $temp\n";

       $sumaGodzinLekcyjnych += $temp;
       $sumaGodzin += (45 * $temp)/60;
     }
   }
   print "suma godzin lekcyjnych: $sumaGodzinLekcyjnych\n";
   print "suma godzin: $sumaGodzin\n";
   #print "licznik: $licznik \n";
}
else
{
  print "nie podano stdin\n";
}
