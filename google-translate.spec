Summary:	This application translates text via Google Translate engine
Summary(hu.UTF-8):	Ez az alkalmazás szövegeket fordít a Google Translate segítségével
Name:		google-translate
Version:	0961
Release:	0.1
License:	GPL v2
Group:		X11/Applications
Source0:	http://alexsnet.ru/wp-content/uploads/2009/02/astranslator-%{version}.zip
# Source0-md5:	6aa6863975f4a36712dcdc533521572e
URL:		http://alexsnet.ru/en/opensource/translator/
BuildRequires:	QtCore-devel
BuildRequires:	qt4-build >= 4.3.3-3
BuildRequires:	qt4-qmake >= 4.3.3-3
BuildRequires:	rpmbuild(macros) >= 1.129
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This application translates text via Google Translate engine.

%description -l hu.UTF-8
This application translates text via Google Translate engine.

%prep
%setup -q -c -n ASTranslator

%build
cd ASTranslator
qmake-qt4
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}
install ASTranslator/bin/Translator $RPM_BUILD_ROOT%{_bindir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
