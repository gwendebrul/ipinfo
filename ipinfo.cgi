#!/usr/bin/perl

# this first use declaration is needed by my server to correctly function
# comment out if needed
#use cPanelUserConfig;

use warnings;
use strict;
use CGI;
use HTTP::Tiny;
use JSON::PP;

my $cgi = CGI->new;

# fill in the location of the ips.txt file (default in cgi-bin)
my $ips_file = './ips.txt';

# ipinfo.css location on the server
my $css_file = "../ipinfo.css";

# index is the index number of the entry in ips.txt
my $index = 1;

# ip contains the ip address if it is set in the query 
# index_ip is the index number of the ip address in the ips.txt file
my $ip = "";
my $index_ip = 0;

print $cgi->header;

# set the viewport for nice layout on mobile
print '<meta name="viewport" content="width=device-width, initial-scale=1.0">';

# includes a css file into the document head part
print "<link type='text/css' rel='stylesheet' href='$css_file' />";

&has_params();
&begin_table();
&ips();
&end_table();

# This function checks if the ip and index parameter are included in the query
# if so then assign the query parameters to these vars (ip, index_ip)
# then call show_info
sub has_params () {
    if ($cgi->param('ip') && $cgi->param('index')) {
        $ip = $cgi->param('ip');
        $index_ip = $cgi->param('index');
        
        &show_info();
    }
}

# show_info makes a call to the ip-api server for information on the given ip address
# if the call is succesfull then show it's info (index, ip, country, city and org)
sub show_info () {
    my $response = HTTP::Tiny->new->get("http://ip-api.com/json/$ip?fields=58385");
    my $ip_info = decode_json $response->{content};

    if ($ip_info->{status} == "success") {
        print "<div id='result'>";
        print "<div>$index_ip</div>";
        print "<div>$ip</div>";
        print "<div>$ip_info->{country}</div>";
        print "<div>$ip_info->{city}</div>";
        print "<div>$ip_info->{org}</div>";
        print "</div>";
    }
}

# begin_table creaters the table with it's header
sub begin_table () {
    print "<div id='table'><table><thead><tr><th>Index</th><th>IP</th><th>link</th></tr></thead><tbody>";
}

# end_table closes the table of ip addresses in the ips.txt file
sub end_table () {
    print "</tbody></table></div>";
}

# ips loops through the ips.txt file and show it on screen in a table
sub ips () {
    open my $IPS,"<",$ips_file;

    while (<$IPS>) {
        # if the index is even then print tr below
        print "<tr class='even'>" if ($index % 2 == 0);

        # if index is uneven then just print a tr
        print "<tr>" if ($index % 2 != 0);
        print "<td>$index</td><td>$_</td><td><a href=\"ipinfo.cgi?ip=$_&index=$index\"><button>show info</button></a></td>";
        print "</tr>";
        $index++;
    }
}