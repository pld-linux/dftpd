Summary:	Standalone ftp server
Summary(pl):	Samodzielny serwer ftp
Name:		dftpd
Version:	1.3
Release:	1
License:	GPL
Group:		Networking/Daemons
Source0:	http://www.karico.fi/dpfs/files/%{name}-%{version}.tar.gz
URL:		http://www.karico.fi/dpfs/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A versatile, easily configurable ftp server featuring web based
administration. Requires no modifications to system configuration
files.

%description -l pl
Wielofunkcyjny, ³atwy w konfiguracji serwer ftp, którym administracja
odbywa siê za pomoc± interfejsu WWW. Nie wymaga modyfikacji plików
systemowych.

%prep
%setup -q

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install

%clean
rm -rf $RPM_BUILD_ROOT

%post
touch /etc/dftpd/utmp.dftp
chmod 0640 /etc/dftpd/utmp.dftp

%preun
rm -f /etc/dftpd/utmp.dftp

%files
%defattr(644,root,root,755)
%doc README CHANGES TODO BUGS COPYING
%{_prefix}/local/dftpd
%dir %{_sysconfdir}/dftpd
%dir %{_sysconfdir}/dftpd/sview
%{_sysconfdir}/dftpd/plugins
%config %{_sysconfdir}/dftpd/dftpd.conf
%config %{_sysconfdir}/dftpd/passwd.dftp
%config %{_sysconfdir}/dftpd/group.dftp
