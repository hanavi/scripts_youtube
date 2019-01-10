#!/usr/bin/perl

use strict;
use warnings;
use Path::Class;

# Find all the folders that actually have a dl url saved
my @files = glob("*/dl.url");

# For each dl file, change to the appropriate directory and download the new
# files
for my $file (@files)
{
    chomp($file);

    # Isolate the directory
    my $dir = dir($+) if $file =~ m~(.*)/.*~;

    # Skipping this one for a bit until it gets all downloaded to begin with
    if ($dir eq "premierdriver") {next;}

    print "\ndownloading $file into $dir\n";

    chdir $dir;

    # Get the name/date of the most recent file downloaded so we can set the
    # date to start downloading from (This might actually be unnesssary given
    # our other options)
    my $lastfile = qx(ls -t |grep -v "dl.url" |head -n 1);
    chomp($lastfile);
    my @stat = qx(stat "$lastfile");

    # Set the date (our error handling could be better here...)
    my $date = "NOT FOUND";
    for my $line (@stat)
    {
        $date = $+ if $line =~ m/Change: ([0-9]{4}-[0-9]{2}-[0-9]{2}).*/;
        $date =~ s/-//g;
    }

    # Run the command!
    print "Downloading!\n";
    qx(youtube-dl --playlist-end 10 --dateafter $date -ci -a dl.url 1>&2);

    # Back to where we started
    chdir $dir->parent;
}
