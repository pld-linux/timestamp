Summary:	A pipe that timestamps lines
Summary(pl):	Potok dodaj±cy znaczniki czasowe do wszystkich linii
Name:		timestamp
Version:	1.1
Release:	1
License:	BSD
Group:		Applications/Text
Source0:	http://math.smsu.edu/~erik/files/%{name}-%{version}.tar.gz
# Source0-md5:	ba90e61f1f7641cd2acb2c4ff3ccd6b4
URL:		http://math.smsu.edu/~erik/software.php?id=95
BuildRequires:	autoconf
BuildRequires:	automake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Timestamp is a text-filtering pipe that marks each line with a timestamp.
The time is set when the first character of the line is received, and the
utility is capable of coping with CR repeats fairly well (it won't
over-write or update the timestamp).

%description -l pl
Timestamp to narzêdzie do modyfikowania tekstu w potoku, które dodaje
do ka¿dej linii znacznik czasowy. Znaczniki wskazuj± czas otrzymania
pierwszego znaku w linii. Timestamp dobrze radzi sobie z nadmiarowymi
znakami powrotu karetki (CR) - nie nadpisuje przy nich ani nie
aktualizuje znaczników.

%prep
%setup -q

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
cp -f /usr/share/automake/config.sub .
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man*/*
