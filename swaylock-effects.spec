%define gittag 1.7.0.0

Name:       swaylock-effects
Version:    %{gittag} 
Release:    0%{?dist}
Summary:    Swaylock, with fancy effects

License:    MIT
Source0:    https://github.com/jirutka/swaylock-effects/archive/refs/tags/v%{gittag}.tar.gz

BuildRequires:  gcc
BuildRequires:  meson >= 0.59.0
BuildRequires:  cmake
BuildRequires:  pam-devel
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-protocols) >= 1.25
BuildRequires:  pkgconfig(wayland-scanner) >= 1.15
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  bash-completion
BuildRequires:  fish
BuildRequires:  scdoc

%define program_name swaylock

%description
Swaylock-effects is a fork of swaylock which adds built-in screenshots and image manipulation effects like blurring. It's inspired by i3lock-color, although the feature sets aren't perfectly overlapping.

%prep
%autosetup -n %{name}-%{gittag}

%build
%meson
%meson_build

%install
%meson_install

%files
%license LICENSE
%doc README.md
%{_bindir}/%{program_name}
%{_mandir}/man1/%{program_name}.1*
%config(noreplace) %{_sysconfdir}/pam.d/%{program_name}

# Co-own completion directories
%dir %{_datadir}/bash-completion
%dir %{_datadir}/bash-completion/completions
%{_datadir}/bash-completion/completions/%{program_name}

%dir %{_datadir}/zsh
%dir %{_datadir}/zsh/site-functions
%{_datadir}/zsh/site-functions/_%{program_name}

%dir %{_datadir}/fish
%dir %{_datadir}/fish/vendor_completions.d
%{_datadir}/fish/vendor_completions.d/%{program_name}.fish


%changelog
* Fri Dec 15 2023 crashdummy <crashdummy@codepotatoes.de> - 1.7.0.0
- Initial package import
