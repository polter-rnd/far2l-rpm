%global commit 3d66329bda549ec572c12def3dc8395e68b6ecf8
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%bcond_without gui
%if %{with gui}
Name: far2l
Conflicts: far2l-tty
%else
Name: far2l-tty
Conflicts: far2l
%endif
Version: 2.6.5
Release: 3.git%{shortcommit}%{?dist}

Summary: Linux port of FAR v2

Group: File tools
License: GPLv2
Url: https://github.com/elfmz/far2l

Source0: https://github.com/elfmz/far2l/archive/%{commit}/far2l-%{shortcommit}.tar.gz

BuildRequires: cmake gcc-c++
%if %{with gui}
BuildRequires: (wxGTK-devel >= 3.0 or wxGTK3-devel)
BuildRequires: libX11-devel
BuildRequires: libXi-devel
%endif
BuildRequires: xerces-c-devel
BuildRequires: uchardet-devel
BuildRequires: libssh-devel
BuildRequires: openssl-devel
BuildRequires: libsmbclient-devel
BuildRequires: libxml2-devel
%if ! 0%{?rhel} || 0%{?rhel} < 9
# libnfs is not in EPEL since RHEL 9
BuildRequires: libnfs-devel
%endif
%if ! 0%{?fedora} || 0%{?fedora} >= 42
# libnfs requires gnutls since Fedora 42
BuildRequires: gnutls-devel
%endif
BuildRequires: neon-devel
BuildRequires: libarchive-devel
BuildRequires: libicu-devel
BuildRequires: perl-interpreter
BuildRequires: perl-open

%description
Linux fork of FAR Manager v2
BETA VERSION.
Use on your own risk!

License: GNU/GPLv2

Used code from projects:
 - FAR for Windows
 - WINE
 - ANSICON
 - Portable UnRAR
 - 7z ANSI-C Decoder


%prep
%autosetup -n far2l-%{commit}

%build
%set_build_flags
%if %{with gui}
cmake -DUSEWX=yes \
    -DCMAKE_C_FLAGS_RELEASE:STRING="-DNDEBUG" \
    -DCMAKE_CXX_FLAGS_RELEASE:STRING="-DNDEBUG" \
    -DCMAKE_VERBOSE_MAKEFILE:BOOL=ON \
    -DCMAKE_INSTALL_PREFIX:PATH=%{_prefix} \
    -DICU_MODE=build .
%else
cmake -DUSEWX=no \
    -DCMAKE_C_FLAGS_RELEASE:STRING="-DNDEBUG" \
    -DCMAKE_CXX_FLAGS_RELEASE:STRING="-DNDEBUG" \
    -DCMAKE_VERBOSE_MAKEFILE:BOOL=ON \
    -DCMAKE_INSTALL_PREFIX:PATH=%{_prefix} \
    -DICU_MODE=build .
%endif
%make_build

%install
%make_install

%if ! %{with gui}
    # Do not install GUI desktop files for tty-only version
    rm -f %{buildroot}%{_datadir}/applications/far2l.desktop
    rm -f %{buildroot}%{_datadir}/applications/far2ledit.desktop
    # Do not install GUI icons for tty-only version
    rm -f %{buildroot}%{_datadir}/icons/far2l-wx.svg
    rm -f %{buildroot}%{_datadir}/icons/far2ledit-wx.svg
    rm -f %{buildroot}%{_datadir}/icons/hicolor/1024x1024/apps/far2l-wx.svg
    rm -f %{buildroot}%{_datadir}/icons/hicolor/1024x1024/apps/far2ledit-wx.svg
    rm -f %{buildroot}%{_datadir}/icons/hicolor/128x128/apps/far2l-wx.svg
    rm -f %{buildroot}%{_datadir}/icons/hicolor/128x128/apps/far2ledit-wx.svg
    rm -f %{buildroot}%{_datadir}/icons/hicolor/16x16/apps/far2l-wx.svg
    rm -f %{buildroot}%{_datadir}/icons/hicolor/16x16/apps/far2ledit-wx.svg
    rm -f %{buildroot}%{_datadir}/icons/hicolor/192x192/apps/far2l-wx.svg
    rm -f %{buildroot}%{_datadir}/icons/hicolor/192x192/apps/far2ledit-wx.svg
    rm -f %{buildroot}%{_datadir}/icons/hicolor/24x24/apps/far2l-wx.svg
    rm -f %{buildroot}%{_datadir}/icons/hicolor/24x24/apps/far2ledit-wx.svg
    rm -f %{buildroot}%{_datadir}/icons/hicolor/256x256/apps/far2l-wx.svg
    rm -f %{buildroot}%{_datadir}/icons/hicolor/256x256/apps/far2ledit-wx.svg
    rm -f %{buildroot}%{_datadir}/icons/hicolor/32x32/apps/far2l-wx.svg
    rm -f %{buildroot}%{_datadir}/icons/hicolor/32x32/apps/far2ledit-wx.svg
    rm -f %{buildroot}%{_datadir}/icons/hicolor/48x48/apps/far2l-wx.svg
    rm -f %{buildroot}%{_datadir}/icons/hicolor/48x48/apps/far2ledit-wx.svg
    rm -f %{buildroot}%{_datadir}/icons/hicolor/512x512/apps/far2l-wx.svg
    rm -f %{buildroot}%{_datadir}/icons/hicolor/512x512/apps/far2ledit-wx.svg
    rm -f %{buildroot}%{_datadir}/icons/hicolor/64x64/apps/far2l-wx.svg
    rm -f %{buildroot}%{_datadir}/icons/hicolor/64x64/apps/far2ledit-wx.svg
    rm -f %{buildroot}%{_datadir}/icons/hicolor/72x72/apps/far2l-wx.svg
    rm -f %{buildroot}%{_datadir}/icons/hicolor/72x72/apps/far2ledit-wx.svg
    rm -f %{buildroot}%{_datadir}/icons/hicolor/96x96/apps/far2l-wx.svg
    rm -f %{buildroot}%{_datadir}/icons/hicolor/96x96/apps/far2ledit-wx.svg
%else
    # Do not install TTY desktop files for GUI version
    rm -f %{buildroot}%{_datadir}/applications/far2l-tty.desktop
    rm -f %{buildroot}%{_datadir}/applications/far2ledit-tty.desktop
    # Do not install TTY icons for GUI version
    rm -f %{buildroot}%{_datadir}/icons/far2l.svg
    rm -f %{buildroot}%{_datadir}/icons/far2ledit.svg
    rm -f %{buildroot}%{_datadir}/icons/hicolor/1024x1024/apps/far2l.svg
    rm -f %{buildroot}%{_datadir}/icons/hicolor/1024x1024/apps/far2ledit.svg
    rm -f %{buildroot}%{_datadir}/icons/hicolor/128x128/apps/far2l.svg
    rm -f %{buildroot}%{_datadir}/icons/hicolor/128x128/apps/far2ledit.svg
    rm -f %{buildroot}%{_datadir}/icons/hicolor/16x16/apps/far2l.svg
    rm -f %{buildroot}%{_datadir}/icons/hicolor/16x16/apps/far2ledit.svg
    rm -f %{buildroot}%{_datadir}/icons/hicolor/192x192/apps/far2l.svg
    rm -f %{buildroot}%{_datadir}/icons/hicolor/192x192/apps/far2ledit.svg
    rm -f %{buildroot}%{_datadir}/icons/hicolor/24x24/apps/far2l.svg
    rm -f %{buildroot}%{_datadir}/icons/hicolor/24x24/apps/far2ledit.svg
    rm -f %{buildroot}%{_datadir}/icons/hicolor/256x256/apps/far2l.svg
    rm -f %{buildroot}%{_datadir}/icons/hicolor/256x256/apps/far2ledit.svg
    rm -f %{buildroot}%{_datadir}/icons/hicolor/32x32/apps/far2l.svg
    rm -f %{buildroot}%{_datadir}/icons/hicolor/32x32/apps/far2ledit.svg
    rm -f %{buildroot}%{_datadir}/icons/hicolor/48x48/apps/far2l.svg
    rm -f %{buildroot}%{_datadir}/icons/hicolor/48x48/apps/far2ledit.svg
    rm -f %{buildroot}%{_datadir}/icons/hicolor/512x512/apps/far2l.svg
    rm -f %{buildroot}%{_datadir}/icons/hicolor/512x512/apps/far2ledit.svg
    rm -f %{buildroot}%{_datadir}/icons/hicolor/64x64/apps/far2l.svg
    rm -f %{buildroot}%{_datadir}/icons/hicolor/64x64/apps/far2ledit.svg
    rm -f %{buildroot}%{_datadir}/icons/hicolor/72x72/apps/far2l.svg
    rm -f %{buildroot}%{_datadir}/icons/hicolor/72x72/apps/far2ledit.svg
    rm -f %{buildroot}%{_datadir}/icons/hicolor/96x96/apps/far2l.svg
    rm -f %{buildroot}%{_datadir}/icons/hicolor/96x96/apps/far2ledit.svg
%endif

%files
%{_bindir}/far2l
%{_bindir}/far2ledit
%{_prefix}/lib/far2l/
%{_datadir}/far2l/
%if %{with gui}
%{_datadir}/applications/far2l.desktop
%{_datadir}/applications/far2ledit.desktop
%{_datadir}/icons/far2l-wx.svg
%{_datadir}/icons/far2ledit-wx.svg
%{_datadir}/icons/hicolor/1024x1024/apps/far2l-wx.svg
%{_datadir}/icons/hicolor/1024x1024/apps/far2ledit-wx.svg
%{_datadir}/icons/hicolor/128x128/apps/far2l-wx.svg
%{_datadir}/icons/hicolor/128x128/apps/far2ledit-wx.svg
%{_datadir}/icons/hicolor/16x16/apps/far2l-wx.svg
%{_datadir}/icons/hicolor/16x16/apps/far2ledit-wx.svg
%{_datadir}/icons/hicolor/192x192/apps/far2l-wx.svg
%{_datadir}/icons/hicolor/192x192/apps/far2ledit-wx.svg
%{_datadir}/icons/hicolor/24x24/apps/far2l-wx.svg
%{_datadir}/icons/hicolor/24x24/apps/far2ledit-wx.svg
%{_datadir}/icons/hicolor/256x256/apps/far2l-wx.svg
%{_datadir}/icons/hicolor/256x256/apps/far2ledit-wx.svg
%{_datadir}/icons/hicolor/32x32/apps/far2l-wx.svg
%{_datadir}/icons/hicolor/32x32/apps/far2ledit-wx.svg
%{_datadir}/icons/hicolor/48x48/apps/far2l-wx.svg
%{_datadir}/icons/hicolor/48x48/apps/far2ledit-wx.svg
%{_datadir}/icons/hicolor/512x512/apps/far2l-wx.svg
%{_datadir}/icons/hicolor/512x512/apps/far2ledit-wx.svg
%{_datadir}/icons/hicolor/64x64/apps/far2l-wx.svg
%{_datadir}/icons/hicolor/64x64/apps/far2ledit-wx.svg
%{_datadir}/icons/hicolor/72x72/apps/far2l-wx.svg
%{_datadir}/icons/hicolor/72x72/apps/far2ledit-wx.svg
%{_datadir}/icons/hicolor/96x96/apps/far2l-wx.svg
%{_datadir}/icons/hicolor/96x96/apps/far2ledit-wx.svg
%else
%{_datadir}/applications/far2l-tty.desktop
%{_datadir}/applications/far2ledit-tty.desktop
%{_datadir}/icons/far2l.svg
%{_datadir}/icons/far2ledit.svg
%{_datadir}/icons/hicolor/1024x1024/apps/far2l.svg
%{_datadir}/icons/hicolor/1024x1024/apps/far2ledit.svg
%{_datadir}/icons/hicolor/128x128/apps/far2l.svg
%{_datadir}/icons/hicolor/128x128/apps/far2ledit.svg
%{_datadir}/icons/hicolor/16x16/apps/far2l.svg
%{_datadir}/icons/hicolor/16x16/apps/far2ledit.svg
%{_datadir}/icons/hicolor/192x192/apps/far2l.svg
%{_datadir}/icons/hicolor/192x192/apps/far2ledit.svg
%{_datadir}/icons/hicolor/24x24/apps/far2l.svg
%{_datadir}/icons/hicolor/24x24/apps/far2ledit.svg
%{_datadir}/icons/hicolor/256x256/apps/far2l.svg
%{_datadir}/icons/hicolor/256x256/apps/far2ledit.svg
%{_datadir}/icons/hicolor/32x32/apps/far2l.svg
%{_datadir}/icons/hicolor/32x32/apps/far2ledit.svg
%{_datadir}/icons/hicolor/48x48/apps/far2l.svg
%{_datadir}/icons/hicolor/48x48/apps/far2ledit.svg
%{_datadir}/icons/hicolor/512x512/apps/far2l.svg
%{_datadir}/icons/hicolor/512x512/apps/far2ledit.svg
%{_datadir}/icons/hicolor/64x64/apps/far2l.svg
%{_datadir}/icons/hicolor/64x64/apps/far2ledit.svg
%{_datadir}/icons/hicolor/72x72/apps/far2l.svg
%{_datadir}/icons/hicolor/72x72/apps/far2ledit.svg
%{_datadir}/icons/hicolor/96x96/apps/far2l.svg
%{_datadir}/icons/hicolor/96x96/apps/far2ledit.svg
%endif
%{_datadir}/bash-completion/completions/far2l
%{_mandir}/man1/far2l.*
%lang(ru) %{_mandir}/ru/man1/far2l.*

%changelog
* Wed Oct 29 2025 Pavel Artsishevsky <polter.rnd@gmail.com> 2.6.5-3.git3d66329
- do not install TTY icons and desktop files for GUI version

* Mon Oct 6 2025 Pavel Artsishevsky <polter.rnd@gmail.com> 2.6.5-2.git3d66329
- add new icons for GUI version
- bump upstream commit (3d66329)

* Sat Apr 5 2025 Pavel Artsishevsky <polter.rnd@gmail.com> 2.6.5-1.gitfb42f6f
- bump upstream commit (fb42f6f)
- bump version to 2.6.5

* Mon Feb 17 2025 Pavel Artsishevsky <polter.rnd@gmail.com> 2.6.4-4.gitb57e232
- fix missing help pages

* Mon Feb 17 2025 Pavel Artsishevsky <polter.rnd@gmail.com> 2.6.4-3.gitb57e232
- bump upstream commit (b57e232)
- fix compilation error on Fedora 42

* Sat Feb 15 2025 Pavel Artsishevsky <polter.rnd@gmail.com> 2.6.4-2.git3a4dfaf
- bump upstream commit (3a4dfaf)

* Sat Jan 4 2025 Pavel Artsishevsky <polter.rnd@gmail.com> 2.6.4-1.git9fb2133
- bump upstream commit (9fb2133)
- bump version to 2.6.4
- remove obsolete build dependencies (pcre2)

* Wed Oct 30 2024 Pavel Artsishevsky <polter.rnd@gmail.com> 2.6.3-2.gitc35f97e
- bump upstream commit (c35f97e)

* Tue Aug 13 2024 Pavel Artsishevsky <polter.rnd@gmail.com> 2.6.3-1.gita045fe5
- bump upstream commit (a045fe5)
- bump version to 2.6.3

* Sat Jul 20 2024 Pavel Artsishevsky <polter.rnd@gmail.com> 2.6.2-1.git9ce5dea
- bump upstream commit (9ce5dea)
- remove obsolete build dependencies

* Sat May 18 2024 Pavel Artsishevsky <polter.rnd@gmail.com> 2.6.1-2.git2068c46
- bump upstream commit (2068c46)
- remove obsolete build dependencies

* Sat Apr 13 2024 Pavel Artsishevsky <polter.rnd@gmail.com> 2.6.1-1.git0b52136
- bump upstream commit (0b52136)
- bump version to 2.6.1

* Thu Mar 14 2024 Pavel Artsishevsky <polter.rnd@gmail.com> 2.6.0-2.git3a39598
- bump upstream commit (3a39598)

* Mon Feb 26 2024 Pavel Artsishevsky <polter.rnd@gmail.com> 2.6.0-1.git69cb147
- bump upstream commit (69cb147)
- bump version to 2.6.0

* Thu Dec 07 2023 Pavel Artsishevsky <polter.rnd@gmail.com> 2.5.3-beta
- bump upstream commit (d8b279a)

* Tue Nov 14 2023 Pavel Artsishevsky <polter.rnd@gmail.com> 2.5.3-beta
- bump upstream commit (851edd2)

* Fri Oct 20 2023 Pavel Artsishevsky <polter.rnd@gmail.com> 2.5.2-beta
- bump upstream commit (cf7ecd1)

* Thu Sep 28 2023 Pavel Artsishevsky <polter.rnd@gmail.com> 2.5.2-beta
- bump upstream commit (2e7d52f)

* Wed Sep 27 2023 Pavel Artsishevsky <polter.rnd@gmail.com> 2.5.2-beta
- bump upstream commit (49ff9c1)

* Mon Aug 14 2023 icesvz <icesvz@gmail.com> 2.5.1-beta
- bump upstream commit (fe3da21)

* Sun Aug 13 2023 icesvz <icesvz@gmail.com> 2.5.1-beta
- force _fortify_level 2 to prevent F38 crashing

* Sat Jul 8 2023 Pavel Artsishevsky <polter.rnd@gmail.com> 2.5.1-beta
- bump upstream commit (5ee6a40)

* Mon May 29 2023 Pavel Artsishevsky <polter.rnd@gmail.com> 2.5.1-beta
- bump upstream commit (88acded)

* Mon May 8 2023 Pavel Artsishevsky <polter.rnd@gmail.com> 2.5.0-beta
- bump upstream commit (12b9e9e)

* Thu Apr 13 2023 Pavel Artsishevsky <polter.rnd@gmail.com> 2.5.0-beta
- bump upstream commit (b2f956f)

* Mon Apr 3 2023 Pavel Artsishevsky <polter.rnd@gmail.com> 2.5.0-beta
- bump upstream commit (8fa9210)

* Wed Mar 29 2023 Pavel Artsishevsky <polter.rnd@gmail.com> 2.5.0-beta
- bump upstream commit (7016f96)

* Tue Mar 28 2023 Pavel Artsishevsky <polter.rnd@gmail.com> 2.5.0-beta
- bump upstream commit (39489dd)
- add support for RHEL9 (remove libnfs dependency)
- add man pages

* Tue Dec 20 2022 Pavel Artsishevsky <polter.rnd@gmail.com> 2.4.1-beta
- bump upstream commit (0c3eaa7)

* Fri Dec 16 2022 Pavel Artsishevsky <polter.rnd@gmail.com> 2.4.1-beta
- bump upstream commit (3a233d6)

* Sun Dec 04 2022 Pavel Artsishevsky <polter.rnd@gmail.com> 2.4.1-beta
- bump upstream commit (0fd2e7d)

* Wed Nov 30 2022 Pavel Artsishevsky <polter.rnd@gmail.com> 2.4.1-beta
- bump upstream commit (8150a21)

* Wed Nov 23 2022 Pavel Artsishevsky <polter.rnd@gmail.com> 2.4.1-beta
- bump upstream commit (e37a3a4)
- remove patch from VPROFi (no more compatible with upstream)

* Mon Aug 29 2022 Pavel Artsishevsky <polter.rnd@gmail.com> 2.4-beta
- bump upstream commit (e4088e6)

* Thu Jul 28 2022 Pavel Artsishevsky <polter.rnd@gmail.com> 2.4-beta
- bump upstream commit (920f22a)
- add changes from VPROFi <v.l.snake.2000@gmail.com>

* Tue Jul 5 2022 Pavel Artsishevsky <polter.rnd@gmail.com> 2.4-beta
- bump upstream commit (78c2802)
- require wxGTK3 or wxGTK (which is 3.1 on Fedora)

* Mon Apr 11 2022 Pavel Artsishevsky <polter.rnd@gmail.com> 2.4-beta
- bump upstream commit (bcac692)

* Mon Apr 11 2022 Pavel Artsishevsky <polter.rnd@gmail.com> 2.3
- add pure console version (far2l-tty)

* Thu Sep 2 2021 Pavel Artsishevsky <polter.rnd@gmail.com> 2.3
- updated build requirements
- bump upstream commit

* Wed Jul 1 2020 Pavel Artsishevsky <polter.rnd@gmail.com> 2.0-alpha
- removed glib2
- added with plugin dependencies

* Sat Sep 15 2018 Anton Midyukov <antohami@altlinux.org> 2.0-alt3.89d986a
- rebuilt with libwxGTK3.0

* Sat Jul 07 2018 Vitaly Lipatov <lav@altlinux.ru> 2.0-alt2.89d986a
- new git build 89d986a

* Wed Jan 04 2017 Vitaly Lipatov <lav@altlinux.ru> 2.0-alt2.4d33a48
- new git build 4d33a48

* Sat Sep 24 2016 Vitaly Lipatov <lav@altlinux.ru> 2.0-alt1.4198cd5
- new git build 4198cd5

* Sat Aug 20 2016 Vitaly Lipatov <lav@altlinux.ru> 2.0-alt1
- initial build for ALT Linux Sisyphus
