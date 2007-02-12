Summary:	Standalone FTP server
Summary(pl.UTF-8):	Samodzielny serwer FTP
Name:		dftpd
Version:	1.3
Release:	1
License:	GPL
Group:		Networking/Daemons
Source0:	http://www.karico.fi/dpfs/files/%{name}-%{version}.tar.gz
# Source0-md5:	d03fa11049f1b09c019615e9ad2df58d
Patch0:		%{name}-fix.patch
URL:		http://www.karico.fi/dpfs/
BuildRequires:	ncurses-devel
Requires(post):	fileutils
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A versatile, easily configurable FTP server featuring web based
administration. Requires no modifications to system configuration
files.

%description -l pl.UTF-8
Wielofunkcyjny, łatwy w konfiguracji serwer FTP, którym administracja
odbywa się za pomocą interfejsu WWW. Nie wymaga modyfikacji plików
systemowych.

%prep
%setup -q
%patch0 -p1

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} -I/usr/include/ncurses"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	BINDIR=$RPM_BUILD_ROOT%{_bindir} \
	CONFDIR=$RPM_BUILD_ROOT%{_sysconfdir}/dftpd \
	DOCSDIR="`pwd`/docs"

%clean
rm -rf $RPM_BUILD_ROOT

%post
touch /etc/dftpd/utmp.dftp
chmod 0640 /etc/dftpd/utmp.dftp

%files
%defattr(644,root,root,755)
%doc BUGS CHANGES README TODO
%attr(755,root,root) %{_bindir}/*
%dir %{_sysconfdir}/dftpd
%dir %{_sysconfdir}/dftpd/sview
%attr(755,root,root) %{_sysconfdir}/dftpd/plugins
%attr(640,root,root) %ghost %{_sysconfdir}/dftpd/utmp.dftp
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/dftpd/dftpd.conf
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/dftpd/passwd.dftp
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/dftpd/group.dftp
