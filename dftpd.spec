Summary: standalone ftp server
Name: dftpd
Version: 1.3
Release: 1
Copyright: GPL
Source: dftpd-1.3.tar.gz
Group: Networking/Daemons

%description
A versatile, easily configurable ftp server featuring web
based administration. Requires no modifications to system
configuration files.

%description -l pl
Wielofunkcyjny, ³atwy w konfiguracji serwer ftp, którym administracja
odbywa siê za pomoc± interfejsu WWW. Nie wymaga modyfikacji plików
systemowych.

%build
make

%install
make install

%files
%doc README CHANGES TODO BUGS COPYING
/usr/local/dftpd
%dir /etc/dftpd
%dir /etc/dftpd/sview
/etc/dftpd/plugins
%config /etc/dftpd/dftpd.conf
%config /etc/dftpd/passwd.dftp
%config /etc/dftpd/group.dftp

%post
touch /etc/dftpd/utmp.dftp
chmod 0640 /etc/dftpd/utmp.dftp

%preun
rm -f /etc/dftpd/utmp.dftp
