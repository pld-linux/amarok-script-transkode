# TODO:
# - find out BR's
# - cleanup
#
%define		scriptname	transkode
%define		_id		27512
Summary:	Transkode amaroK Script
Summary(pl.UTF-8):	Skrypt Transkode dla amaroKa
Name:		amarok-script-transkode
Version:	0.5
Release:	0.1
License:	GPL
Group:		X11/Applications/Multimedia
#Source0:	http://download.kde.org/khotnewstuff/amarokscripts/downloads/%{scriptname}-%{version}.tar.bz2
Source0:	%{scriptname}-%{version}.tar.bz2
# Source0-md5:	018e59de11ac70d22f51cb0b82d33070
Patch0:		%{name}-x86_64.patch
URL:		http://www.kde-apps.org/content/show.php?content=%{_id}
Requires:	amarok >= 1.3
Requires:	taglib >= 1.4
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_scriptdir %{_datadir}/apps/amarok/scripts

%description
This script allows of transcoding media files from inside of amarok
between many formats.

The best thing about it, is that it allows converting files in process
of copying music to a media player, thus making it possible to keep
songs in a loosless format, like FLAC, on the computer, and convert it
on the fly to Ogg/MP3 to the audio player.

%description -l pl.UTF-8
Ten skrypt pozwala na przekodowywanie plików z poziomu amaroka
pomiędzy wieloma formatami.

Najlepszą rzeczą związaną z tym skryptem jest to, iż pozwala na
konwertowanie plików w procesie przegrywania muzyki na odtwarzacz
audio, tym samym pozwalając na trzymanie piosenek w bezstratnym
formacie, jak FLAC, na komputerze i konwertowanie w locie do Ogg/MP3
na odtwarzacz audio.

%prep
%setup -q -n %{scriptname}-%{version}
%ifarch %{x8664} alpha ia64 ppc64 s390x sparc64
%patch0 -p1
%endif

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_scriptdir}/%{scriptname},%{_desktopdir}/kde}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

mv -f $RPM_BUILD_ROOT{%{_datadir}/applnk/Utilities,%{_desktopdir}/kde}/transkode.desktop

# FIXME: install kde HTML in %{_kdedocdir}
%find_lang transcode --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f transcode.lang
%defattr(644,root,root,755)
%dir %{_scriptdir}/%{scriptname}
# README must be here in %files, not in %doc
%{_scriptdir}/%{scriptname}/README
%attr(755,root,root) %{_bindir}/transkode
%attr(755,root,root) %{_scriptdir}/%{scriptname}/transkode
%{_scriptdir}/%{scriptname}/transkode.spec
%{_scriptdir}/%{scriptname}/defaultsrc
%{_datadir}/apps/transkode
%{_datadir}/config/transkoderc
%{_desktopdir}/kde/transkode.desktop
%{_iconsdir}/hicolor/*/apps/transkode.png
