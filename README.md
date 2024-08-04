# lookup IP info from visitors.cgi

This little script goes through the ips.txt file created and filled by the visitors.cgi script and shows every entry with a button which links to its own and shows info on the ip in the entry. 

Info contains index number, ip address, country, city and organization name.

## installation

copy the ipinfo.cgi to your cgi-bin folder. If the ips.txt is in its standard place (the cgi-bin folder) then you don't have to change the $ips_file var in this script.

Place your ipinfo.css in the directory above cgi-bin (this should be the document root), if you place ipsinfo.css in this folder you don't have to change the $css_file var in this script.

Now enjoy!!