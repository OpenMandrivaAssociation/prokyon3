%define name prokyon3
%define version 0.9.4
%define release %mkrel 4

Summary:   	An MP3/Ogg manager and tag editor
Name:      	%{name}
Version:   	%{version}
Release:   	%{release}
Source0:    	%{name}-%{version}.tar.bz2
Source1:   	%{name}_16.png.bz2
Source2:   	%{name}_32.png.bz2
Source3:   	%{name}_48.png.bz2
Patch0:		%{name}-%{version}-nl.po-patch
Patch1:     prokyon3-0.9.4.cpp.patch
Group: 	   	Sound
License:   	GPL
URL:       	http://%{name}.sourceforge.net/
Buildroot: 	%{_tmppath}/%{name}-buildroot
Requires:	MySQL-Max
Requires:	cdrecord
Requires:	mpg123
Requires:	normalize
Requires:	vorbis-tools
BuildRequires:	X11-devel
BuildRequires:	gettext-devel
BuildRequires:	libid3-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libmysql-devel
BuildRequires:	libogg-devel
BuildRequires:	qt3-devel
BuildRequires:	libvorbis-devel
BuildRequires:	zlib-devel
BuildRequires:  musicbrainz-devel
BuildRequires:  mad-devel
BuildRequires:  libflac++-devel

%description
Prokyon3 is a multithreaded MP3/Ogg manager and tag editor for Linux.
It was written in C++ using the Qt3 widget set and the MySQL database.
Prokyon3 can access MP3 files on harddisk, CDROM, SMB and NFS. 

Files can be played  using XMMS and can even be played when the
files are on CD as prokyon3 identifies CDs by content. 

The files view is customizable and favourite artists as well as sampler
soundtracks are supported. Prokyon3 also offers an editor for ID3 tags
and has been designed to support tagging for multiple files en masse.

Prokyon3 key features are:

     * multithreaded                                              
     * manages files on harddisk/CDROM or over network        
     * search the database by artist, song, album, filename...	  
     * very comfortable editor for ID3 tags			  
     * manages favorite artists and sampler/soundtracks
     * plays and enqueues MP3 files with XMMS or any other player           
     * uses MySQL as database back end
     * configuration editor and database wizard
     * access files over SMB and NFS                
     * play-list editor                                            
     * support for Ogg/Vorbis

%prep
%setup -q
%patch0 -p1 -b .nl-fix
%patch1 -p0 -b .cpp-fix

%build
[ -f "/usr/bin/moc" ] || export PATH="${PATH}:%_libdir/qt3/bin"

%configure --with-qtdir="%_prefix/lib/qt3" --with-qt-libs="%_prefix/lib/qt3/%_lib"

%make

%install
rm -rf ${RPM_BUILD_ROOT}

%makeinstall

%find_lang %{name}

# Icons
install -d ${RPM_BUILD_ROOT}{%_miconsdir,%_liconsdir}
bzcat %{SOURCE1} > ${RPM_BUILD_ROOT}%{_miconsdir}/%{name}.png
bzcat %{SOURCE2} > ${RPM_BUILD_ROOT}%{_iconsdir}/%{name}.png
bzcat %{SOURCE3} > ${RPM_BUILD_ROOT}%{_liconsdir}/%{name}.png

# Install menu entry


mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
cat > $RPM_BUILD_ROOT%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=Prokyon3
Comment=%{summary}
Exec=%{_bindir}/%{name} 
Icon=%{name}
Terminal=false
Type=Application
StartupNotify=true
Categories=Audio;X-MandrivaLinux-Multimedia-Sound;
EOF

%clean
rm -rf ${RPM_BUILD_ROOT}

%post
%{update_menus}

%postun
%{clean_menus}

%files -f %{name}.lang
%defattr(-, root, root)
%doc COPYING INSTALL NEWS README

%{_bindir}/%{name}
%{_bindir}/prokburn

%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/images
%{_datadir}/%{name}/images/*.png

%dir %{_datadir}/%{name}/html/
%dir %{_datadir}/%{name}/html/manual_one_file/
%{_datadir}/%{name}/html/manual_one_file/index.html
%{_datadir}/%{name}/html/manual_one_file/index_fr.html

%dir %{_datadir}/%{name}/html/manual_one_file/images/
%dir %{_datadir}/%{name}/html/manual_one_file/images/docbook/
%{_datadir}/%{name}/html/manual_one_file/images/docbook/*.png

%{_datadir}/applications/mandriva-%{name}.desktop

%{_iconsdir}/%{name}.png
%{_miconsdir}/%{name}.png
%{_liconsdir}/%{name}.png

